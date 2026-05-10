import json
import time
import pandas as pd
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# Kafka configuration
KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "news_articles"

# Input file path (mounted via Docker volume)
INPUT_CSV = "/data/test_articles.csv"


def main():
    # Retry logic for Kafka connection
    max_retries = 30
    retry_count = 0
    producer = None
    
    while retry_count < max_retries and producer is None:
        try:
            print(f"Attempting to connect to Kafka (attempt {retry_count + 1}/{max_retries})...")
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_BROKER,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                request_timeout_ms=10000,
                retries=3
            )
            print("✅ Connected to Kafka successfully")
            break
        except NoBrokersAvailable:
            retry_count += 1
            if retry_count < max_retries:
                print(f"⏳ Kafka not ready yet, retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("❌ Could not connect to Kafka after 30 attempts")
                raise

    # Read CSV file
    df = pd.read_csv(INPUT_CSV)
    print(f"Loaded {len(df)} records from CSV")

    # Send each row as a Kafka message
    for _, row in df.iterrows():
        message = row.to_dict()
        producer.send(TOPIC_NAME, value=message)

    # Ensure all messages are sent
    producer.flush()
    producer.close()

    print("✅ All messages successfully sent to Kafka")


if __name__ == "__main__":
    main()
