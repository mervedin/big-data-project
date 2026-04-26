import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
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

    # Schema of Kafka message value (JSON)
    schema = StructType() \
        .add("title", StringType()) \
        .add("content", StringType()) \
        .add("source", StringType())

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
        .select("data.*")
    )

    # ✅ Reuse your existing batch logic here
    result_df = analyze_sentiment(parsed_df)

    # Write output as CSV (batch-style)
    query = (
        result_df.writeStream
        .format("csv")
        .option("path", OUTPUT_PATH)
        .option("checkpointLocation", "/tmp/checkpoints/sentiments")
        .outputMode("append")
        .trigger(once=True)   # ✅ MICRO-BATCH = BATCH
        .start()
    )

    query.awaitTermination()
    spark.stop()


if __name__ == "__main__":
    main()
