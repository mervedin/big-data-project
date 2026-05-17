import os
import json
import time
import requests
from kafka import KafkaProducer

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
TOPIC = "raw-news"

def fetch_news(query="technology", page_size=100):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("articles", [])

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    articles = fetch_news(query="AI technology business")
    for article in articles:
        producer.send(TOPIC, value=article)
        print(f"Sent: {article['title']}")

    producer.flush()
    print(f"Done — {len(articles)} articles sent to topic '{TOPIC}'")

if __name__ == "__main__":
    main()