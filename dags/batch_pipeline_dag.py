from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="batch_kafka_spark_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,          # manual trigger (recommended for course)
    catchup=False,
    tags=["big-data", "batch"],
) as dag:

    produce_to_kafka = BashOperator(
        task_id="produce_to_kafka",
        bash_command="docker-compose run --rm kafka-producer",
    )

    run_spark_job = BashOperator(
        task_id="run_spark_job",
        bash_command="docker-compose run --rm spark-job",
    )

    produce_to_kafka >> run_spark_job
