from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="batch_kafka_spark_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",  # ✅ RUNS DAILY AT 00:00 UTC
    catchup=False,
    tags=["big-data", "batch", "ml-sentiment"],
) as dag:
    """
    Daily News Sentiment Analysis Pipeline:
    1. Fetch latest news from NewsAPI
    2. Send articles to Kafka
    3. Run Spark ML model for sentiment analysis (distilbert)
    4. Output CSV with results
    """

    # ✅ TASK 1: Fetch news and send to Kafka
    fetch_news = BashOperator(
        task_id="fetch_news_to_kafka",
        bash_command="""
        # Ensure the Kafka topic exists before sending
        docker exec $(docker ps -qf name=kafka) \
          kafka-topics --bootstrap-server kafka:9092 \
          --create --if-not-exists \
          --topic news_articles \
          --partitions 1 \
          --replication-factor 1 && \
        curl -X POST \
          'http://news-api:8000/search-and-send-to-kafka?query=technology&page_size=50' \
          -H 'Content-Type: application/json' \
          && echo "✅ News fetched and sent to Kafka"
        """,
        execution_timeout=timedelta(minutes=10),
    )

    # ✅ TASK 2: Run Spark ML sentiment analysis
    run_sentiment_analysis = BashOperator(
        task_id="run_ml_sentiment_analysis",
        bash_command="""
        # Find the host path of the project directory from this container's /project mount
        HOST_PROJECT_DIR=$(docker inspect $(hostname) --format '{{`{{ range .Mounts }}{{ if eq .Destination "/project" }}{{ .Source }}{{ end }}{{ end }}`}}')
        HOST_DATA_DIR="${HOST_PROJECT_DIR}/data"
        mkdir -p "${HOST_DATA_DIR}"
        echo "Writing results to host path: ${HOST_DATA_DIR}"
        docker run --rm \
          --network big-data-project_default \
          -v "${HOST_DATA_DIR}:/results" \
          big-data-project-spark-job:latest \
        && echo "ML sentiment analysis complete"
        """,
        execution_timeout=timedelta(minutes=30),
    )

    # Pipeline workflow
    fetch_news >> run_sentiment_analysis
