import os
import json
import requests
from kafka import KafkaProducer

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
TOPIC = "raw-news"

def fetch_news():
    response = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": "technology business",
            "pageSize": 100,
            "sortBy": "publishedAt",
            "language": "en",
            "apiKey": NEWS_API_KEY,
        }
    )
    response.raise_for_status()
    return response.json().get("articles", [])

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    articles = fetch_news()
    for article in articles:
        producer.send(TOPIC, value=article)
    
    producer.flush()
    print(f"Produced {len(articles)} articles to '{TOPIC}'")

if __name__ == "__main__":
    main()