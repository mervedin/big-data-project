import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, coalesce
from pyspark.sql.types import StructType, StringType

from sentiment_logic import analyze_sentiment


KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "news_articles"
OUTPUT_PATH = "/results/sentiments"


def main():
    # Pre-create the output directory so the volume mount is ready
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    spark = (
        SparkSession.builder
        .appName("KafkaSparkBatchSentiment")
        # Use committer algorithm v2: writes directly without the _temporary rename step,
        # avoiding FileNotFoundException on Docker-mounted volumes.
        .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
        .config("spark.hadoop.mapreduce.fileoutputcommitter.cleanup-failures.ignored", "true")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    # Schema of Kafka message value (JSON)
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

    # ✅ TRUE BATCH READ — no streaming, no checkpoints, no partition metadata issues
    kafka_df = (
        spark.read
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", TOPIC_NAME)
        .option("startingOffsets", "earliest")
        .option("endingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()
    )

    kafka_count = kafka_df.count()
    print(f"📨 Records read from Kafka topic '{TOPIC_NAME}': {kafka_count}")

    if kafka_count == 0:
        print("⚠️  No messages in Kafka topic. Exiting without writing output.")
        spark.stop()
        return

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
            col("data.published_at"),
            col("data.content"),
            col("data.fetched_at"),
            coalesce(col("data.content"), col("data.description"), col("data.title")).alias("text_to_analyze")
        )
    )

    parsed_count = parsed_df.count()
    print(f"✅ Records after JSON parsing: {parsed_count}")
    parsed_df.show(5, truncate=True)

    # Run DistilBERT sentiment analysis
    result_df = analyze_sentiment(parsed_df)

    # Write output as a single CSV file with header
    (
        result_df
        .coalesce(1)
        .write
        .mode("overwrite")
        .option("header", "true")
        .csv(OUTPUT_PATH)
    )

    print("✅ Sentiment analysis complete. Results saved to", OUTPUT_PATH)
    spark.stop()


if __name__ == "__main__":
    main()
