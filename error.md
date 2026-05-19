

Details

Graph

Gantt

Code

Event Log

Logs

XCom



94f0429cee99
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T16:46:28.079190+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
*** !!!! Please make sure that all your Airflow components (e.g. schedulers, webservers, workers and triggerer) have the same 'secret_key' configured in 'webserver' section and time is synchronized on all your machines (for example with ntpd)
See more at https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#secret-key
*** Could not read served logs: 403 Client Error: FORBIDDEN for url: http://94f0429cee99:8793/log/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T16:46:28.079190+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 16:46:30 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 16:46:30 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 16:46:30 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        docker run --rm           --network big-data-project_default           --mount source=big-data-project_results_data,target=/results           big-data-project-spark-job:latest         && echo "✅ ML sentiment analysis complete"\n        ']
[2026-05-19, 16:46:30 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 16:46:30 UTC] {subprocess.py:93} INFO - :: loading settings :: url = jar:file:/opt/spark/jars/ivy-2.5.1.jar!/org/apache/ivy/core/settings/ivysettings.xml
[2026-05-19, 16:46:31 UTC] {subprocess.py:93} INFO - Ivy Default Cache set to: /root/.ivy2/cache
[2026-05-19, 16:46:31 UTC] {subprocess.py:93} INFO - The jars for the packages stored in: /root/.ivy2/jars
[2026-05-19, 16:46:31 UTC] {subprocess.py:93} INFO - org.apache.spark#spark-sql-kafka-0-10_2.12 added as a dependency
[2026-05-19, 16:46:31 UTC] {subprocess.py:93} INFO - :: resolving dependencies :: org.apache.spark#spark-submit-parent-c85627fe-b33b-4a75-a0d2-f4591f884270;1.0
[2026-05-19, 16:46:31 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:46:32 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:46:33 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:46:33 UTC] {subprocess.py:93} INFO - 	found org.apache.kafka#kafka-clients;3.4.1 in central
[2026-05-19, 16:46:33 UTC] {subprocess.py:93} INFO - 	found org.lz4#lz4-java;1.8.0 in central
[2026-05-19, 16:46:33 UTC] {subprocess.py:93} INFO - 	found org.xerial.snappy#snappy-java;1.1.10.3 in central
[2026-05-19, 16:46:34 UTC] {subprocess.py:93} INFO - 	found org.slf4j#slf4j-api;2.0.7 in central
[2026-05-19, 16:46:35 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-runtime;3.3.4 in central
[2026-05-19, 16:46:35 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-api;3.3.4 in central
[2026-05-19, 16:46:36 UTC] {subprocess.py:93} INFO - 	found commons-logging#commons-logging;1.1.3 in central
[2026-05-19, 16:46:36 UTC] {subprocess.py:93} INFO - 	found com.google.code.findbugs#jsr305;3.0.0 in central
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - 	found org.apache.commons#commons-pool2;2.11.1 in central
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1!spark-sql-kafka-0-10_2.12.jar (152ms)
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1!spark-token-provider-kafka-0-10_2.12.jar (169ms)
[2026-05-19, 16:46:39 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.1/kafka-clients-3.4.1.jar ...
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.kafka#kafka-clients;3.4.1!kafka-clients.jar (838ms)
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.0/jsr305-3.0.0.jar ...
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] com.google.code.findbugs#jsr305;3.0.0!jsr305.jar (44ms)
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar ...
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.commons#commons-pool2;2.11.1!commons-pool2.jar (52ms)
[2026-05-19, 16:46:40 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar ...
[2026-05-19, 16:46:42 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-runtime;3.3.4!hadoop-client-runtime.jar (2614ms)
[2026-05-19, 16:46:42 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar ...
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.lz4#lz4-java;1.8.0!lz4-java.jar (98ms)
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.3/snappy-java-1.1.10.3.jar ...
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.xerial.snappy#snappy-java;1.1.10.3!snappy-java.jar(bundle) (219ms)
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.7/slf4j-api-2.0.7.jar ...
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.slf4j#slf4j-api;2.0.7!slf4j-api.jar (41ms)
[2026-05-19, 16:46:43 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar ...
[2026-05-19, 16:46:44 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-api;3.3.4!hadoop-client-api.jar (1698ms)
[2026-05-19, 16:46:44 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar ...
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] commons-logging#commons-logging;1.1.3!commons-logging.jar (41ms)
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - :: resolution report :: resolve 8011ms :: artifacts dl 5983ms
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	:: modules in use:
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	com.google.code.findbugs#jsr305;3.0.0 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	commons-logging#commons-logging;1.1.3 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.commons#commons-pool2;2.11.1 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-api;3.3.4 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-runtime;3.3.4 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.kafka#kafka-clients;3.4.1 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.lz4#lz4-java;1.8.0 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.slf4j#slf4j-api;2.0.7 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	org.xerial.snappy#snappy-java;1.1.10.3 from central in [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	|                  |            modules            ||   artifacts   |
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	|      default     |   11  |   11  |   11  |   0   ||   11  |   11  |
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - :: retrieving :: org.apache.spark#spark-submit-parent-c85627fe-b33b-4a75-a0d2-f4591f884270
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 	11 artifacts copied, 0 already retrieved (56767kB/41ms)
[2026-05-19, 16:46:45 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:45 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Running Spark version 3.5.1
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Java version 11.0.22
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceUtils: No custom resources configured for spark.driver.
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Submitted application: KafkaSparkBatchSentiment
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceProfile: Limiting resource is cpu
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO ResourceProfileManager: Added ResourceProfile id: 0
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SecurityManager: Changing view acls to: root
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SecurityManager: Changing modify acls to: root
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SecurityManager: Changing view acls groups to:
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SecurityManager: Changing modify acls groups to:
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: root; groups with view permissions: EMPTY; users with modify permissions: root; groups with modify permissions: EMPTY
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Successfully started service 'sparkDriver' on port 42607.
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkEnv: Registering MapOutputTracker
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkEnv: Registering BlockManagerMaster
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-0ed99fa2-b061-4641-8f9c-0f5bd9328aa1
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO MemoryStore: MemoryStore started with capacity 434.4 MiB
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkEnv: Registering OutputCommitCoordinator
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO JettyUtils: Start Jetty 0.0.0.0:4040 for SparkUI
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Successfully started service 'SparkUI' on port 4040.
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at spark://6dd05553c34f:42607/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at spark://6dd05553c34f:42607/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at spark://6dd05553c34f:42607/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at spark://6dd05553c34f:42607/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at spark://6dd05553c34f:42607/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at spark://6dd05553c34f:42607/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at spark://6dd05553c34f:42607/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at spark://6dd05553c34f:42607/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added JAR file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at spark://6dd05553c34f:42607/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO SparkContext: Added file file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Copying /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Starting executor ID driver on host 6dd05553c34f
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Java version 11.0.22
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Starting executor with user classpath (userClassPathFirst = false): ''
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Created or updated repl class loader org.apache.spark.util.MutableURLClassLoader@42e5d425 for default.
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO TransportClientFactory: Successfully created connection to 6dd05553c34f/172.18.0.8:42607 after 9 ms (0 ms spent in bootstraps)
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp14728800784037281339.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp14728800784037281339.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/commons-logging_commons-logging-1.1.3.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp10302138381451234655.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp10302138381451234655.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/com.google.code.findbugs_jsr305-3.0.0.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp4052103990238172505.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp4052103990238172505.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.xerial.snappy_snappy-java-1.1.10.3.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp15939709746218976303.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp15939709746218976303.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.kafka_kafka-clients-3.4.1.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp15098521767996233694.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp15098521767996233694.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp17583063038621308574.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp17583063038621308574.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-api-3.3.4.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp14547804474334633926.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp14547804474334633926.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.lz4_lz4-java-1.8.0.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp13008968127972584892.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp13008968127972584892.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.slf4j_slf4j-api-2.0.7.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp3649370453443474628.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp3649370453443474628.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp17219787819704408556.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp17219787819704408556.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Fetching spark://6dd05553c34f:42607/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779209213253
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Fetching spark://6dd05553c34f:42607/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp2918656058278892458.tmp
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/fetchFileTemp2918656058278892458.tmp has been previously copied to /tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Executor: Adding file:/tmp/spark-334f9190-b38b-49da-867c-1d5b580dad6f/userFiles-572d2b5f-fc91-4809-85f2-8a899fb803c0/org.apache.commons_commons-pool2-2.11.1.jar to class loader default
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 41717.
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO NettyBlockTransferService: Server created on 6dd05553c34f:41717
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 6dd05553c34f, 41717, None)
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManagerMasterEndpoint: Registering block manager 6dd05553c34f:41717 with 434.4 MiB RAM, BlockManagerId(driver, 6dd05553c34f, 41717, None)
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 6dd05553c34f, 41717, None)
[2026-05-19, 16:46:53 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:53 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 6dd05553c34f, 41717, None)
[2026-05-19, 16:46:54 UTC] {subprocess.py:93} INFO - 26/05/19 16:46:54 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset]' were supplied but are not used yet.