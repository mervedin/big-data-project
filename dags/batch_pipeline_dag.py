from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.http import SimpleHttpOperator
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
    schedule_interval="@daily",  # ✅ RUNS DAILY AT MIDNIGHT
    catchup=False,
    tags=["big-data", "batch", "news-sentiment"],
) as dag:

    # ✅ TASK 1: Fetch news from NewsAPI and send to Kafka
    fetch_and_send_news = SimpleHttpOperator(
        task_id="fetch_and_send_news",
        http_conn_id='http_default',
        endpoint='http://news-api:8000/search-and-send-to-kafka?query=technology&page_size=20',
        method='POST',
        headers={'Content-Type': 'application/json'},
    )

    # Alternative: Use BashOperator with curl if SimpleHttpOperator doesn't work
    # fetch_and_send_news = BashOperator(
    #     task_id="fetch_and_send_news",
    #     bash_command="""
    #     curl -X POST "http://news-api:8000/search-and-send-to-kafka?query=technology&page_size=20"
    #     """,
    # )

    # ✅ TASK 2: Run Spark sentiment analysis (with ML model)
    run_spark_sentiment = BashOperator(
        task_id="run_spark_sentiment_analysis",
        bash_command="""
        docker run --rm \
          --network big-data-project_default \
          -v /Users/mervedin/Desktop/big_data/big-data-project/results:/results \
          big-data-project-spark-job:latest
        """,
    )

    # ✅ Pipeline sequence
    fetch_and_send_news >> run_spark_sentiment
