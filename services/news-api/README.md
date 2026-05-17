# News Crawling API

A FastAPI-based service for fetching news from free APIs and directing them into your sentiment analysis pipeline.

## Features

- ✅ Fetch top headlines by country and category
- ✅ Search news by keyword
- ✅ Automatic Kafka integration for real-time sentiment analysis
- ✅ Built-in API documentation (Swagger UI)
- ✅ Retry logic and error handling

## Setup

### 1. Get a Free NewsAPI Key

Sign up for a free account at [https://newsapi.org/register](https://newsapi.org/register)

Free tier includes:
- 500 requests/day
- 100 requests/minute rate limit
- 50,000+ news sources

### 2. Configure API Key

Add your NEWS_API_KEY to `.env`:

```bash
cp .env.example .env
# Edit .env and add your NEWS_API_KEY
```

### 3. Start the Service

```bash
docker-compose up -d news-api
```

The API will be available at: **http://localhost:8001**

## API Endpoints

### Interactive Documentation
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

### Endpoints

#### 1. Get Top Headlines by Country
```bash
curl "http://localhost:8001/headlines?country=us&category=technology&page_size=10"
```

**Query Parameters:**
- `country` (default: "us") - Country code: us, gb, fr, de, it, es...
- `category` (optional) - business, entertainment, general, health, science, sports, technology
- `page_size` (default: 20, max: 100) - Number of articles

#### 2. Search News by Keyword
```bash
curl "http://localhost:8001/search?query=artificial%20intelligence&sort_by=publishedAt&page_size=10"
```

**Query Parameters:**
- `query` **Required** - Search keywords
- `sort_by` (default: "publishedAt") - publishedAt, relevancy, popularity
- `page_size` (default: 20, max: 100)

#### 3. Search News AND Send to Kafka (for sentiment analysis)
```bash
curl -X POST "http://localhost:8001/search-and-send-to-kafka?query=stock%20market&page_size=15"
```

This endpoint:
1. Fetches news matching your query
2. Automatically sends each article to Kafka topic `news_articles`
3. Spark job will pick it up and perform sentiment analysis
4. Results will be available in your results directory

**Example Response:**
```json
{
  "status": "success",
  "message": "✅ Sent 15 articles to Kafka for sentiment analysis",
  "articles_sent": 15,
  "kafka_topic": "news_articles"
}
```

#### 4. Health Check
```bash
curl "http://localhost:8001/health"
```

Returns:
```json
{
  "status": "healthy",
  "kafka": "connected",
  "timestamp": "2026-05-16T10:30:45.123456"
}
```

## Usage Examples

### Example 1: Get UK Tech News
```bash
curl "http://localhost:8001/headlines?country=gb&category=technology"
```

### Example 2: Search and Analyze Market News
```bash
curl -X POST "http://localhost:8001/search-and-send-to-kafka?query=stock+market+crash&page_size=20"
```

This will fetch 20 articles about stock market crashes and send them to Kafka for real-time sentiment analysis by Spark.

### Example 3: Get Most Popular News
```bash
curl "http://localhost:8001/search?query=artificial%20intelligence&sort_by=popularity"
```

## Integration with Sentiment Analysis Pipeline

The news crawler API integrates seamlessly with your existing pipeline:

```
News API (fetch articles)
    ↓
Kafka (queue articles)
    ↓
Spark Job (sentiment analysis)
    ↓
Results (sentiment scores)
```

When you use the `/search-and-send-to-kafka` endpoint, articles go through the full sentiment analysis pipeline automatically.

## Response Format

All endpoints return articles in this format:

```json
{
  "status": "success",
  "total_results": 38,
  "articles": [
    {
      "source": "TechCrunch",
      "author": "John Doe",
      "title": "AI Breakthrough in Machine Learning",
      "description": "Researchers announce major breakthrough...",
      "url": "https://techcrunch.com/...",
      "image": "https://...",
      "published_at": "2026-05-16T10:30:00Z",
      "content": "Full article content..."
    }
  ]
}
```

## Error Handling

- **400 Bad Request**: Invalid query or API returned an error
- **500 Internal Server Error**: API service error
- **503 Service Unavailable**: Kafka not connected (for /search-and-send-to-kafka)

## Rate Limits

NewsAPI Free Tier:
- **500 requests per day**
- **100 requests per minute**

Plan your queries accordingly. For production use, consider upgrading to a paid NewsAPI plan.

## Troubleshooting

### "Kafka service not available"
Make sure Kafka is running:
```bash
docker-compose ps | grep kafka
```

### "API key invalid"
Check your `NEWS_API_KEY` in `.env` is correctly set.

### Rate limit exceeded
Wait before making more requests, or upgrade your NewsAPI plan.

## Next Steps

1. Start the service: `docker-compose up -d news-api`
2. Visit http://localhost:8001/docs to try the API
3. Execute `/search-and-send-to-kafka` to run articles through sentiment analysis
4. Check results in your `/results` directory
