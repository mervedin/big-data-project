import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, coalesce, lit
from pyspark.sql.types import StructType, StringType

from sentiment_logic import analyze_sentiment


KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "news_articles"
OUTPUT_PATH = "/results/sentiments"


def main():
    spark = (
        SparkSession.builder
        .appName("KafkaSparkBatchSentiment")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    # Create header file first
    header_path = f"{OUTPUT_PATH}/header.txt"
    try:
        with open(header_path, 'w') as f:
            f.write("source,author,title,description,url,published_at,sentiment,fetched_at\n")
    except Exception as e:
        print(f"Note: Could not write header file: {e}")

    # Schema of Kafka message value (JSON) - includes all fields from API
    schema = StructType() \
        .add("source", StringType()) \
        .add("author", StringType()) \
        .add("title", StringType()) \
        .add("description", StringType()) \
        .add("url", StringType()) \
        .add("image", StringType()) \
        .add("published_at", StringType()) \
        .add("content", StringType()) \
        .add("fetched_at", StringType())

    # Read from Kafka (batch-style using Structured Streaming)
    kafka_df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", TOPIC_NAME)
        .option("startingOffsets", "earliest")
        .load()
    )

    # Parse JSON messages
    parsed_df = (
        kafka_df
        .select(from_json(col("value").cast("string"), schema).alias("data"))
        .select(
            col("data.source"),
            col("data.author"),
            col("data.title"),
            col("data.description"),
            col("data.url"),
            col("data.image"),
            col("data.published_at"),
            col("data.content"),
            col("data.fetched_at"),
            # Use title first, fallback to description for sentiment analysis
            coalesce(col("data.content"), col("data.description"), col("data.title")).alias("text_to_analyze")
        )
    )

    # ✅ Reuse your existing batch logic here
    result_df = analyze_sentiment(parsed_df)

    # Coalesce to single file for easier viewing
    result_df_single = result_df.coalesce(1)

    # Write output as CSV (batch-style)
    query = (
        result_df_single.writeStream
        .format("csv")
        .option("path", OUTPUT_PATH)
        .option("header", "true")  # Include header row
        .option("checkpointLocation", "/tmp/checkpoints/sentiments")
        .outputMode("append")
        .trigger(once=True)   # ✅ MICRO-BATCH = BATCH
        .start()
    )

    query.awaitTermination()
    spark.stop()


if __name__ == "__main__":
    main()
