import json
import time
import pandas as pd
from kafka import KafkaProducer

# Kafka configuration
KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "news_articles"

# Input file path (mounted via Docker volume)
INPUT_CSV = "/data/test_articles.csv"


def main():
    # Create Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

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

    print("All messages successfully sent to Kafka")


if __name__ == "__main__":
    main()
