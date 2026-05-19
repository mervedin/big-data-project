64ef139d9487
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T15:41:24.273127+00:00/task_id=fetch_news_to_kafka/attempt=1.log
[2026-05-19, 15:41:25 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 15:41:25 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 15:41:25 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        curl -X POST           \'http://localhost:8001/search-and-send-to-kafka?query=technology&page_size=50\'           -H \'Content-Type: application/json\'           && echo "✅ News fetched and sent to Kafka"\n        ']
[2026-05-19, 15:41:25 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 15:41:25 UTC] {subprocess.py:93} INFO -   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
[2026-05-19, 15:41:25 UTC] {subprocess.py:93} INFO -                                  Dload  Upload   Total   Spent    Left  Speed
[2026-05-19, 15:41:25 UTC] {subprocess.py:93} INFO - 
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
[2026-05-19, 15:41:25 UTC] {subprocess.py:93} INFO - curl: (7) Failed to connect to localhost port 8001 after 0 ms: Couldn't connect to server
[2026-05-19, 15:41:25 UTC] {subprocess.py:97} INFO - Command exited with return code 7
[2026-05-19, 15:41:25 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
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
airflow.exceptions.AirflowException: Bash command failed. The command returned a non-zero exit code 7.
[2026-05-19, 15:41:25 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=fetch_news_to_kafka, run_id=manual__2026-05-19T15:41:24.273127+00:00, execution_date=20260519T154124, start_date=20260519T154125, end_date=20260519T154125
[2026-05-19, 15:41:25 UTC] {taskinstance.py:340} ▶ Post task execution logs