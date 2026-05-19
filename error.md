

fe21570d499e
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T17:06:50.935179+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 17:06:52 UTC] {local_task_job_runner.py:123} ▼ Pre task execution logs
[2026-05-19, 17:06:52 UTC] {taskinstance.py:2612} INFO - Dependencies all met for dep_context=non-requeueable deps ti=<TaskInstance: batch_kafka_spark_pipeline.run_ml_sentiment_analysis manual__2026-05-19T17:06:50.935179+00:00 [queued]>
[2026-05-19, 17:06:52 UTC] {taskinstance.py:2612} INFO - Dependencies all met for dep_context=requeueable deps ti=<TaskInstance: batch_kafka_spark_pipeline.run_ml_sentiment_analysis manual__2026-05-19T17:06:50.935179+00:00 [queued]>
[2026-05-19, 17:06:52 UTC] {taskinstance.py:2865} INFO - Starting attempt 1 of 3
[2026-05-19, 17:06:52 UTC] {taskinstance.py:2888} INFO - Executing <Task(BashOperator): run_ml_sentiment_analysis> on 2026-05-19 17:06:50.935179+00:00
[2026-05-19, 17:06:52 UTC] {logging_mixin.py:190} WARNING - /home/airflow/.local/lib/python3.12/site-packages/airflow/task/task_runner/standard_task_runner.py:70 DeprecationWarning: This process (pid=212) is multi-threaded, use of fork() may lead to deadlocks in the child.
[2026-05-19, 17:06:52 UTC] {standard_task_runner.py:72} INFO - Started process 213 to run task
[2026-05-19, 17:06:52 UTC] {standard_task_runner.py:104} INFO - Running: ['airflow', 'tasks', 'run', 'batch_kafka_spark_pipeline', 'run_ml_sentiment_analysis', 'manual__2026-05-19T17:06:50.935179+00:00', '--job-id', '72', '--raw', '--subdir', 'DAGS_FOLDER/batch_pipeline_dag.py', '--cfg-path', '/tmp/tmp25y7hopv']
[2026-05-19, 17:06:52 UTC] {standard_task_runner.py:105} INFO - Job 72: Subtask run_ml_sentiment_analysis
[2026-05-19, 17:06:52 UTC] {logging_mixin.py:190} WARNING - /home/airflow/.local/lib/python3.12/site-packages/airflow/settings.py:209 DeprecationWarning: The sql_alchemy_conn option in [core] has been moved to the sql_alchemy_conn option in [database] - the old setting has been used, but please update your config.
[2026-05-19, 17:06:52 UTC] {task_command.py:467} INFO - Running <TaskInstance: batch_kafka_spark_pipeline.run_ml_sentiment_analysis manual__2026-05-19T17:06:50.935179+00:00 [running]> on host fe21570d499e
[2026-05-19, 17:06:52 UTC] {abstractoperator.py:778} ERROR - Exception rendering Jinja template for task 'run_ml_sentiment_analysis', field 'bash_command'. Template: '\n        # Find the host path of the project directory from this container\'s /project mount\n        HOST_PROJECT_DIR=$(docker inspect $(hostname) --format \'{{`{{ range .Mounts }}{{ if eq .Destination "/project" }}{{ .Source }}{{ end }}{{ end }}`}}\')\n        HOST_DATA_DIR="${HOST_PROJECT_DIR}/data"\n        mkdir -p "${HOST_DATA_DIR}"\n        echo "Writing results to host path: ${HOST_DATA_DIR}"\n        docker run --rm           --network big-data-project_default           -v "${HOST_DATA_DIR}:/results"           big-data-project-spark-job:latest         && echo "ML sentiment analysis complete"\n        '
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/abstractoperator.py", line 770, in _do_render_template_fields
    rendered_content = self.render_template(
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/template/templater.py", line 170, in render_template
    template = jinja_env.from_string(value)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 1108, in from_string
    return cls.from_code(self, self.compile(source), gs, None)
                               ^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 768, in compile
    self.handle_exception(source=source_hint)
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 939, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "<unknown>", line 3, in template
jinja2.exceptions.TemplateSyntaxError: unexpected char '`' at 158
[2026-05-19, 17:06:52 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskinstance.py", line 273, in _run_raw_task
    TaskInstance._execute_task_with_callbacks(
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskinstance.py", line 3114, in _execute_task_with_callbacks
    task_orig = self.render_templates(context=context, jinja_env=jinja_env)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskinstance.py", line 3533, in render_templates
    original_task.render_template_fields(context, jinja_env)
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/baseoperator.py", line 1419, in render_template_fields
    self._do_render_template_fields(self, self.template_fields, context, jinja_env, set())
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/abstractoperator.py", line 770, in _do_render_template_fields
    rendered_content = self.render_template(
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/airflow/template/templater.py", line 170, in render_template
    template = jinja_env.from_string(value)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 1108, in from_string
    return cls.from_code(self, self.compile(source), gs, None)
                               ^^^^^^^^^^^^^^^^^^^^
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 768, in compile
    self.handle_exception(source=source_hint)
  File "/home/airflow/.local/lib/python3.12/site-packages/jinja2/environment.py", line 939, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "<unknown>", line 3, in template
jinja2.exceptions.TemplateSyntaxError: unexpected char '`' at 158
[2026-05-19, 17:06:52 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=run_ml_sentiment_analysis, run_id=manual__2026-05-19T17:06:50.935179+00:00, execution_date=20260519T170650, start_date=20260519T170652, end_date=20260519T170652
[2026-05-19, 17:06:52 UTC] {taskinstance.py:340} ▶ Post task execution logs