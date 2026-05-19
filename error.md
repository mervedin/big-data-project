


48cefd9f9118
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T15:56:10.093896+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 15:56:12 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 15:56:12 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 15:56:12 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        docker run --rm           --network big-data-project_default           -v /project/results:/results           big-data-project-spark-job:latest         && echo "✅ ML sentiment analysis complete"\n        ']
[2026-05-19, 15:56:12 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 15:56:12 UTC] {subprocess.py:93} INFO - docker: Error response from daemon: mounts denied:
[2026-05-19, 15:56:12 UTC] {subprocess.py:93} INFO - The path /project/results is not shared from the host and is not known to Docker.
[2026-05-19, 15:56:12 UTC] {subprocess.py:93} INFO - You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.
[2026-05-19, 15:56:12 UTC] {subprocess.py:93} INFO - See https://docs.docker.com/go/mac-file-sharing/ for more info.
[2026-05-19, 15:56:12 UTC] {subprocess.py:97} INFO - Command exited with return code 125
[2026-05-19, 15:56:12 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskinstance.py", line 762, in _execute_task
    result = _execute_callable(context=context, **execute_callable_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskinstance.py", line 733, in _execute_callable
    return ExecutionCallableRunner(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/utils/operator_helpers.py", line 252, in run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/baseoperator.py", line 406, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/operators/bash.py", line 249, in execute
    raise AirflowException(
airflow.exceptions.AirflowException: Bash command failed. The command returned a non-zero exit code 125.
[2026-05-19, 15:56:12 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=run_ml_sentiment_analysis, run_id=manual__2026-05-19T15:56:10.093896+00:00, execution_date=20260519T155610, start_date=20260519T155612, end_date=20260519T155612
[2026-05-19, 15:56:12 UTC] {taskinstance.py:340} ▶ Post task execution logs