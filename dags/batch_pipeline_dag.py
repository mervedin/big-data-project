from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="batch_kafka_spark_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["big-data", "batch"],
) as dag:

    produce_to_kafka = BashOperator(
        task_id="produce_to_kafka",
        bash_command="""
        docker run --rm \
          --network big-data-project_default \
          -v /Users/mervedin/Desktop/big_data/big-data-project/data:/data \
          big-data-project-kafka-producer:latest
        """,
    )

    run_spark_job = BashOperator(
        task_id="run_spark_job",
        bash_command="""
        docker run --rm \
          --network big-data-project_default \
          -v /Users/mervedin/Desktop/big_data/big-data-project/results:/results \
          big-data-project-spark-job:latest
        """,
    )

    produce_to_kafka >> run_spark_job
