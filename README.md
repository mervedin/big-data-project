# 📰 Big Data News Sentiment Analysis

A daily batch pipeline that automatically fetches news, runs **DistilBERT ML sentiment analysis** via Apache Spark, and outputs results to CSV — orchestrated by Apache Airflow and transported through Apache Kafka.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Building & Running](#building--running)
- [Using the Pipeline](#using-the-pipeline)
- [Viewing Results](#viewing-results)
- [Stopping the Stack](#stopping-the-stack)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Make sure the following are installed on your machine:

| Tool | Version | Download |
|------|---------|----------|
| Docker Desktop | ≥ 24.x | https://www.docker.com/products/docker-desktop |
| Docker Compose | ≥ 2.x (bundled with Docker Desktop) | — |
| NewsAPI key | Free tier | https://newsapi.org/register |

> **Windows users**: Enable WSL 2 backend in Docker Desktop settings for best performance.

---

## Project Structure

```
big-data-project/
├── docker-compose.yml          # Defines all services
├── .env                        # Secret keys & config (you create this)
├── dags/
│   └── batch_pipeline_dag.py   # Airflow DAG (daily schedule)
├── services/
│   ├── news-api/               # FastAPI: fetches news → Kafka
│   ├── spark-job/              # Spark + DistilBERT sentiment analysis
│   ├── kafka-producer/         # (deprecated) static CSV producer
│   └── python-app/             # (deprecated) standalone ML pipeline
└── results/                    # Output CSVs written here (auto-created)
```

---

## Environment Setup

### 1. Get a NewsAPI Key

Sign up for free at [https://newsapi.org/register](https://newsapi.org/register).

### 2. Create the `.env` file

Copy the example below and fill in your values:

```env
# NewsAPI credentials
NEWS_API_KEY=your_newsapi_key_here

# PostgreSQL (used by Airflow metadata)
DB_HOST=postgres
DB_PORT=5432
DB_NAME=news_sentiment
DB_USER=postgres
DB_PASSWORD=YourPassword123
```

> ⚠️ Never commit `.env` to version control. It is (and should remain) in `.gitignore`.

### 3. Create the results directory

```bash
mkdir results
```

---

## Building & Running

### Step 1 — Build all Docker images

This builds the `news-api` and `spark-job` images from their Dockerfiles:

```bash
docker compose build
```

To rebuild a single service (e.g., after changing `sentiment_logic.py`):

```bash
docker compose build spark-job
```

> ⏳ The first build of `spark-job` takes several minutes — it downloads PyTorch and the DistilBERT model weights (~250 MB).

---

### Step 2 — Initialize Airflow (first time only)

This creates the Airflow database schema and the default `admin` user:

```bash
docker compose run --rm airflow-init
```

You should see:
```
Admin user admin created
```

---

### Step 3 — Start all services

```bash
docker compose up -d
```

This starts:

| Service | URL | Purpose |
|---------|-----|---------|
| `airflow-webserver` | http://localhost:8080 | DAG management UI |
| `news-api` | http://localhost:8001 | News fetch API + Swagger docs |
| `kafka` | localhost:9092 | Message broker |
| `zookeeper` | localhost:2181 | Kafka coordination |
| `postgres` | localhost:5432 | Airflow metadata DB |
| `nifi` | http://localhost:8443 | (available, not in pipeline) |

Check all containers are running:

```bash
docker compose ps
```

---

### Step 4 — Verify services are healthy

```bash
# Check news-api
curl http://localhost:8001/health

# Check Airflow
curl http://localhost:8080/health
```

---

## Using the Pipeline

### Option A — Automated Daily Run (Airflow)

1. Open **http://localhost:8080** (login: `admin` / `admin`)
2. Find the DAG called **`batch_kafka_spark_pipeline`**
3. Toggle it **ON** (the slider on the left)
4. It will run automatically at **00:00 UTC every day**
5. To run immediately: click the DAG → **Trigger DAG ▶**

---

### Option B — Manual API Trigger

**Step 1**: Fetch news and send to Kafka:

```bash
curl -X POST "http://localhost:8001/search-and-send-to-kafka?query=technology&page_size=50"
```

**Step 2**: Run DistilBERT sentiment analysis:

```bash
curl -X POST "http://localhost:8001/trigger-sentiment-analysis"
```

> ⏳ The Spark + DistilBERT job takes ~2–5 minutes depending on article count.

---

### Option C — Run Spark Job Directly

```bash
docker run --rm \
  --network big-data-project_default \
  -v "$(pwd)/results:/results" \
  big-data-project-spark-job:latest
```

**Windows (Command Prompt):**

```cmd
docker run --rm ^
  --network big-data-project_default ^
  -v "%cd%/results:/results" ^
  big-data-project-spark-job:latest
```

---

## Viewing Results

Results are written to `results/sentiments/` as CSV files:

```bash
# Linux / macOS / WSL
cat results/sentiments/part-*.csv

# Windows (PowerShell)
Get-Content results\sentiments\part-*.csv
```

**Output columns:**

| Column | Description |
|--------|-------------|
| `source` | News source name (e.g. TechCrunch) |
| `author` | Article author |
| `title` | Article headline |
| `description` | Article summary |
| `url` | Full article URL |
| `published_at` | Publication timestamp |
| `sentiment` | `positive`, `negative`, or `neutral` |
| `fetched_at` | When the article was fetched |

**Example row:**
```
TechCrunch,John Doe,"New AI Breakthrough","OpenAI announces...",https://...,2026-05-19T10:30:00Z,positive,2026-05-19T12:00:00
```

---

## Stopping the Stack

Stop all containers (preserves data volumes):

```bash
docker compose down
```

Stop and **delete all data** (including Postgres metadata):

```bash
docker compose down -v
```

Remove built images (forces a full rebuild next time):

```bash
docker compose down --rmi local
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `news-api` returns 503 (Kafka unavailable) | Wait ~30s for Kafka to fully start, then retry |
| CSV is empty after Spark job | Clear stale checkpoint: `docker run --rm -v "$(pwd)/results:/results" busybox rm -rf /tmp/checkpoints/sentiments` |
| Airflow DAG not visible | Check `dags/` is mounted correctly; look at `docker compose logs airflow-scheduler` |
| DistilBERT model download fails | Ensure internet access from inside Docker; check `docker compose logs spark-job` |
| `docker compose build` fails for spark-job | Ensure Docker has ≥ 4 GB RAM allocated (Docker Desktop → Settings → Resources) |
| Port 8080 already in use | Change `"8080:8080"` in `docker-compose.yml` to e.g. `"8181:8080"` |
| NewsAPI returns 401 | Check `NEWS_API_KEY` is set correctly in `.env` |

### View logs for a specific service

```bash
docker compose logs -f news-api
docker compose logs -f spark-job
docker compose logs -f airflow-scheduler
```

---

## 🔧 Common Configuration Changes

**Change news search query or volume** — edit `dags/batch_pipeline_dag.py`:
```python
'http://localhost:8001/search-and-send-to-kafka?query=AI&page_size=100'
```

**Change schedule** — edit `dags/batch_pipeline_dag.py`:
```python
schedule_interval="@hourly"   # or "@weekly", "0 6 * * *", etc.
```

**Add sentiment keywords / swap models** — edit `services/spark-job/sentiment_logic.py`.
