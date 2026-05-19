from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import httpx
import os
from datetime import datetime, timedelta
from kafka import KafkaProducer
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="News Crawling API", version="1.0.0")

# Configuration
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your_api_key_here")
NEWS_API_BASE_URL = "https://newsapi.org/v2"
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = "news_articles"

# Kafka producer — lazy, reconnects on each call
kafka_producer = None

def get_kafka_producer():
    global kafka_producer
    if kafka_producer is None:
        try:
            kafka_producer = KafkaProducer(
                bootstrap_servers=KAFKA_BROKER,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                request_timeout_ms=10000,
            )
            logger.info("✅ Connected to Kafka")
        except Exception as e:
            logger.warning(f"⚠️ Kafka not available: {e}")
            kafka_producer = None
    return kafka_producer


# Pydantic models
class Article(BaseModel):
    source: str
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    image: Optional[str]
    published_at: str
    content: Optional[str]


class NewsResponse(BaseModel):
    status: str
    total_results: int
    articles: List[Article]


# Helper function to fetch from NewsAPI
async def fetch_from_newsapi(
    query: str = None,
    category: str = None,
    country: str = "us",
    sort_by: str = "publishedAt",
    page_size: int = 20,
):
    """Fetch news from NewsAPI.org"""
    async with httpx.AsyncClient() as client:
        if query:
            # Search endpoint
            url = f"{NEWS_API_BASE_URL}/everything"
            params = {
                "q": query,
                "sortBy": sort_by,
                "pageSize": page_size,
                "apiKey": NEWS_API_KEY,
            }
        else:
            # Top headlines endpoint
            url = f"{NEWS_API_BASE_URL}/top-headlines"
            params = {
                "country": country,
                "pageSize": page_size,
                "apiKey": NEWS_API_KEY,
            }
            if category:
                params["category"] = category

        try:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Error fetching from NewsAPI: {e}")
            raise


# Routes
@app.get("/", tags=["Health"])
async def root():
    return {
        "message": "News Crawling API",
        "version": "1.0.0",
        "endpoints": [
            "/docs",
            "/headlines",
            "/search",
            "/search-and-send-to-kafka",
        ],
    }


@app.get("/headlines", response_model=NewsResponse, tags=["News"])
async def get_headlines(
    country: str = Query("us", description="Country code (e.g., us, gb, fr)"),
    category: Optional[str] = Query(
        None,
        description="Category (business, entertainment, general, health, science, sports, technology)",
    ),
    page_size: int = Query(20, ge=1, le=100, description="Number of articles"),
):
    """Fetch top headlines from a specific country and optional category"""
    try:
        data = await fetch_from_newsapi(
            category=category, country=country, page_size=page_size
        )

        if data["status"] != "ok":
            raise HTTPException(status_code=400, detail=data.get("message", "Unknown error"))

        articles = [
            Article(
                source=article["source"]["name"],
                author=article.get("author"),
                title=article["title"],
                description=article.get("description"),
                url=article["url"],
                image=article.get("urlToImage"),
                published_at=article["publishedAt"],
                content=article.get("content"),
            )
            for article in data["articles"]
        ]

        return NewsResponse(
            status="success",
            total_results=data.get("totalResults", 0),
            articles=articles,
        )
    except Exception as e:
        logger.error(f"Error in /headlines: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search", response_model=NewsResponse, tags=["News"])
async def search_news(
    query: str = Query(..., description="Search query"),
    sort_by: str = Query(
        "publishedAt",
        description="Sort by: publishedAt, relevancy, popularity",
    ),
    page_size: int = Query(20, ge=1, le=100, description="Number of articles"),
):
    """Search for news articles by keyword"""
    try:
        data = await fetch_from_newsapi(
            query=query, sort_by=sort_by, page_size=page_size
        )

        if data["status"] != "ok":
            raise HTTPException(status_code=400, detail=data.get("message", "Unknown error"))

        articles = [
            Article(
                source=article["source"]["name"],
                author=article.get("author"),
                title=article["title"],
                description=article.get("description"),
                url=article["url"],
                image=article.get("urlToImage"),
                published_at=article["publishedAt"],
                content=article.get("content"),
            )
            for article in data["articles"]
        ]

        return NewsResponse(
            status="success",
            total_results=data.get("totalResults", 0),
            articles=articles,
        )
    except Exception as e:
        logger.error(f"Error in /search: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search-and-send-to-kafka", tags=["News"])
async def search_and_send_to_kafka(
    query: str = Query(..., description="Search query"),
    page_size: int = Query(10, ge=1, le=100, description="Number of articles"),
):
    """Search for news and send to Kafka for sentiment analysis"""
    producer = get_kafka_producer()
    if not producer:
        raise HTTPException(
            status_code=503,
            detail="Kafka service not available",
        )

    try:
        data = await fetch_from_newsapi(query=query, page_size=page_size)

        if data["status"] != "ok":
            raise HTTPException(status_code=400, detail=data.get("message", "Unknown error"))

        sent_count = 0
        for article in data["articles"]:
            message = {
                "source": article["source"]["name"],
                "author": article.get("author"),
                "title": article["title"],
                "description": article.get("description"),
                "url": article["url"],
                "image": article.get("urlToImage"),
                "published_at": article["publishedAt"],
                "content": article.get("content"),
                "fetched_at": datetime.now().isoformat(),
            }
            producer.send(KAFKA_TOPIC, value=message)
            sent_count += 1

        producer.flush()

        return {
            "status": "success",
            "message": f"✅ Sent {sent_count} articles to Kafka for sentiment analysis",
            "articles_sent": sent_count,
            "kafka_topic": KAFKA_TOPIC,
            "next_step": "Call POST /trigger-sentiment-analysis to analyze sentiment"
        }
    except Exception as e:
        logger.error(f"Error in /search-and-send-to-kafka: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/trigger-sentiment-analysis", tags=["Analysis"])
async def trigger_sentiment_analysis():
    """Trigger Spark sentiment analysis on Kafka messages"""
    import subprocess
    import os
    import glob
    
    try:
        # Remove old checkpoint to allow re-processing
        subprocess.run(
            ["rm", "-rf", "/tmp/checkpoints/sentiments"],
            capture_output=True
        )
        
        # Run Spark sentiment analysis
        logger.info("📊 Starting sentiment analysis job...")
        results_path = os.getenv("RESULTS_PATH", "/project/results")
        result = subprocess.run(
            [
                "docker", "run", "--rm",
                "--network", "big-data-project_default",
                "-v", f"{results_path}:/results",
                "big-data-project-spark-job:latest"
            ],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            # Post-process: Add headers to CSV file
            csv_dir = os.path.join(os.getenv("RESULTS_PATH", "/project/results"), "sentiments")
            csv_files = glob.glob(os.path.join(csv_dir, "part-*.csv"))
            
            if csv_files:
                # Read all CSV data
                all_data = []
                for csv_file in csv_files:
                    try:
                        with open(csv_file, 'r') as f:
                            all_data.extend(f.readlines())
                    except:
                        pass
                
                # Write back with header
                if all_data:
                    # Find first part file and write with header
                    first_file = csv_files[0]
                    with open(first_file, 'w') as f:
                        f.write("source,author,title,description,url,published_at,sentiment,fetched_at\n")
                        f.writelines(all_data)
                    
                    logger.info("✅ Added header to CSV file")
            
            logger.info("✅ Sentiment analysis completed successfully")
            return {
                "status": "success",
                "message": "✅ Sentiment analysis job completed",
                "output_path": "/results/sentiments"
            }
        else:
            logger.error(f"Spark job failed: {result.stderr}")
            return {
                "status": "error",
                "message": "Sentiment analysis job failed",
                "error": result.stderr
            }
            
    except subprocess.TimeoutExpired:
        logger.error("Sentiment analysis job timed out")
        return {
            "status": "error",
            "message": "Sentiment analysis job timed out after 120 seconds"
        }
    except Exception as e:
        logger.error(f"Error triggering sentiment analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    kafka_status = "connected" if kafka_producer else "disconnected"
    return {
        "status": "healthy",
        "kafka": kafka_status,
        "timestamp": datetime.now().isoformat(),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
