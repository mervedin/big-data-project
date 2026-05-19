# 📊 Big Data News Sentiment Analysis - System Architecture

## Overview
Batch processing pipeline that **automatically fetches news daily**, analyzes sentiment, and outputs results to CSV.

---

## 🏗️ Current Architecture (Consolidated)

```
┌─────────────────────────────────────────────────────────────────┐
│                    DAILY BATCH PIPELINE                         │
│                  (Airflow Scheduler: @daily)                    │
└─────────────────────────────────────────────────────────────────┘

Daily Trigger (00:00 UTC)
         ↓
┌───────────────────────────────────────┐
│  TASK 1: Fetch News                   │
│ services/news-api/main.py             │
│ - GET from NewsAPI.org                │
│ - POST /search-and-send-to-kafka      │
│ Input: Search query (technology)      │
│ Output: Articles → Kafka Topic        │
└───────────────────────────────────────┘
         ↓ (Kafka: news_articles)
┌───────────────────────────────────────┐
│  TASK 2: Sentiment Analysis           │
│ services/spark-job/spark_batch.py     │
│ - Read from Kafka                     │
│ - Process with sentiment_logic.py     │
│ - Output CSV                          │
│ Method: Keyword-based classification  │
│ (Alternative: ML model available)     │
└───────────────────────────────────────┘
         ↓
┌───────────────────────────────────────┐
│  OUTPUT: CSV Results                  │
│ Location: results/sentiments/         │
│ Columns: source, author, title,       │
│ description, url, published_at,       │
│ sentiment, fetched_at                 │
└───────────────────────────────────────┘
```

---

## 📁 Service Breakdown

### ✅ **ACTIVE SERVICES**

#### 1. **news-api** (FastAPI)
- **File**: `services/news-api/main.py`
- **Port**: 8001
- **Purpose**: Fetch news from NewsAPI.org and send to Kafka
- **Endpoints**:
  - `GET /headlines` - Fetch by country/category
  - `GET /search` - Search by keyword
  - `POST /search-and-send-to-kafka` - Fetch + send to Kafka
  - `POST /trigger-sentiment-analysis` - Run Spark job
- **Status**: 🟢 RUNNING & IN PIPELINE

#### 2. **kafka** (Confluent Kafka)
- **Purpose**: Message broker for article pipeline
- **Topic**: `news_articles`
- **Status**: 🟢 RUNNING & IN PIPELINE

#### 3. **spark-job** (Apache Spark)
- **File**: `services/spark-job/`
- **Purpose**: Process articles from Kafka and analyze sentiment
- **Components**:
  - `spark_batch.py` - Consumer logic
  - `sentiment_logic.py` - Sentiment classification
- **Method**: Keyword-based (fast, optimized for Spark)
- **Status**: 🟢 RUNNING & IN PIPELINE

#### 4. **airflow** + **postgres**
- **Purpose**: DAG orchestration and metadata storage
- **DAG File**: `dags/batch_pipeline_dag.py`
- **Schedule**: `@daily` (00:00 UTC)
- **UI**: `http://localhost:8080`
- **Status**: 🟢 RUNNING & IN PIPELINE

---

### ⚠️ **AVAILABLE BUT DEPRECATED**

#### 1. **python-app** (Standalone ML Pipeline)
- **File**: `services/python-app/batch_pipeline.py`
- **Model**: DistilBERT (`distilbert-base-uncased-finetuned-sst-2-english`)
- **Purpose**: ML-based sentiment analysis (more accurate than keywords)
- **Reason Deprecated**: Not integrated into Dockerized pipeline
- **Can Still Use Standalone**:
  ```bash
  # Run ML sentiment analysis on static CSV
  docker run -v ./data:/data -v ./results:/results python-app python batch_pipeline.py
  ```
- **Status**: ⚠️ AVAILABLE BUT NOT IN MAIN PIPELINE

#### 2. **kafka-producer**
- **File**: `services/kafka-producer/`
- **Purpose**: Sends static CSV test data to Kafka
- **Reason Deprecated**: Replaced by live news fetching from API
- **Status**: ⚠️ AVAILABLE FOR TESTING

#### 3. **spark** (Standalone)
- **Purpose**: Standalone Spark Master (not integrated)
- **Reason Deprecated**: Using containerized Spark jobs instead
- **Status**: ⚠️ NOT USED

#### 4. **nifi**
- **Purpose**: Data flow orchestration
- **Reason Deprecated**: Using Airflow DAG instead
- **Status**: ⚠️ NOT USED

---

## 🔄 Complete Data Flow

### **Step 1: Daily Trigger** (Airflow Scheduler)
```
⏰ Every day at 00:00 UTC
    ↓
👁️ Check if batch_pipeline_dag is scheduled
    ↓
📋 Start Task 1: fetch_news_to_kafka
```

### **Step 2: Fetch News** (news-api)
```
🔗 Called via: curl -X POST "http://localhost:8001/search-and-send-to-kafka?query=technology&page_size=50"
    ↓
📰 NewsAPI.org returns 50 tech articles
    ↓
📝 Format each article:
   {
     "source": "TechCrunch",
     "author": "John Doe",
     "title": "New AI Breakthrough",
     "description": "...",
     "url": "https://...",
     "image": "https://...jpg",
     "published_at": "2026-05-16T...",
     "content": "Full article text...",
     "fetched_at": "2026-05-18T12:34:56"
   }
    ↓
🚀 Send to Kafka topic: "news_articles"
    ↓
✅ Response: {"articles_sent": 50, "status": "success"}
```

### **Step 3: Sentiment Analysis** (Spark Job)
```
📥 Spark reads from Kafka topic "news_articles"
    ↓
📊 Apply schema to parse JSON
    ↓
🔍 Extract text: content → description → title (priority order)
    ↓
🧭 Classify sentiment:
   Keyword Analysis:
   - Positive words: good, great, growth, success, improved...
   - Negative words: bad, terrible, loss, crash, decline...
   - Count: positive_count > negative_count → "positive"
   - Count: negative_count > positive_count → "negative"
   - Otherwise: "neutral"
    ↓
💾 Output 8 columns to CSV:
   source, author, title, description, url, published_at, sentiment, fetched_at
    ↓
📂 Save to: results/sentiments/part-*.csv
```

### **Step 4: View Results**
```
bash
cat results/sentiments/part-*.csv
```

**Example Output:**
```
TechCrunch,John Doe,"New AI Breakthrough","...",https://...,2026-05-16T10:30:00Z,positive,2026-05-18T12:34:56
Reuters,,,"Stock market rises...",https://...,2026-05-16T11:00:00Z,positive,2026-05-18T12:34:56
```

---

## 🚀 How to Use

### **Option 1: Manual API Call (Immediate)**
```bash
# Step 1: Fetch news
curl -X POST "http://localhost:8001/search-and-send-to-kafka?query=AI&page_size=20"

# Step 2: Analyze sentiment
curl -X POST "http://localhost:8001/trigger-sentiment-analysis"

# Step 3: View results
cat results/sentiments/part-*.csv
```

### **Option 2: Automated via Airflow (Daily)**
1. Open `http://localhost:8080`
2. Go to "DAGs" → "batch_kafka_spark_pipeline"
3. Click "Trigger DAG" or wait for daily schedule (00:00 UTC)
4. Monitor task execution
5. Results auto-saved to `results/sentiments/`

### **Option 3: Use ML Model (DistilBERT)**
```bash
# Run standalone ML sentiment analysis
docker run -v ./data:/data -v ./results:/results \
  big-data-project-python-app:latest \
  python batch_pipeline.py
```
- **Better accuracy** than keyword-based
- **Slower** (ML inference on every article)
- **Output**: `results/sentiments_YYYY-MM-DD.csv` + HTML report

---

## 📊 Code Audit Summary

| Component | Type | Status | Used | Notes |
|-----------|------|--------|------|-------|
| news-api | FastAPI | ✅ | Yes | Fetches live news |
| spark-job | Spark | ✅ | Yes | Sentiment analysis |
| airflow | Orchestration | ✅ | Yes | Scheduling & DAG |
| kafka | Broker | ✅ | Yes | Message transport |
| python-app | ML Model | ⚠️ | No | Available standalone |
| kafka-producer | Producer | ⚠️ | No | Static CSV testing |
| spark | Standalone | ❌ | No | Not needed |
| nifi | Flow Tool | ❌ | No | Using Airflow instead |

---

## 📝 Key Usage Scenarios

### **Scenario 1: Daily Automated Reporting**
- Schedule: Every day at 00:00 UTC
- News fetched: 50 latest tech articles
- Sentiment: Auto-classified
- Output: CSV for analysis

### **Scenario 2: On-Demand Analysis**
- Fetch via REST API
- Immediate results
- Manual trigger when needed

### **Scenario 3: Higher Accuracy ML**
- Use python-app with DistilBERT model
- Trade-off: Slower but more accurate
- Output includes confidence scores

---

## 🔧 Configuration

**Daily Schedule**: Edit `dags/batch_pipeline_dag.py`
```python
schedule_interval="@daily"  # Change to "@hourly", "@weekly", etc.
```

**News Source**: Edit `dags/batch_pipeline_dag.py`
```bash
query=technology&page_size=50  # Change search query or page size
```

**Sentiment Method**: Edit `services/spark-job/sentiment_logic.py`
- Add more keywords to improve accuracy
- Or integrate ML model for better classification

---

## 📞 Troubleshooting

| Issue | Solution |
|-------|----------|
| CSV empty | Clear checkpoint: `rm -rf /tmp/checkpoints/sentiments` |
| DAG not running | Check Airflow UI at http://localhost:8080/admin/airflow/graph |
| News API quota | Increase `page_size` or adjust query |
| Slow processing | Reduce `page_size` or use keyword-based only |

---

## 🎯 What's Next?

1. **Improve Sentiment**: Replace keywords with ML model
2. **Database Storage**: Save results to PostgreSQL instead of CSV
3. **Dashboard**: Visualize sentiment trends over time
4. **Alerting**: Send notifications for high-impact news
5. **Multi-language**: Support news in multiple languages
