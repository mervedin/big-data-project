Event Log

Logs

XCom



94f0429cee99
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T16:31:30.009322+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 16:31:32 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 16:31:32 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 16:31:32 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        docker run --rm           --network big-data-project_default           --mount source=big-data-project_results_data,target=/results           big-data-project-spark-job:latest         && echo "✅ ML sentiment analysis complete"\n        ']
[2026-05-19, 16:31:32 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - :: loading settings :: url = jar:file:/opt/spark/jars/ivy-2.5.1.jar!/org/apache/ivy/core/settings/ivysettings.xml
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - Ivy Default Cache set to: /root/.ivy2/cache
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - The jars for the packages stored in: /root/.ivy2/jars
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - org.apache.spark#spark-sql-kafka-0-10_2.12 added as a dependency
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - :: resolving dependencies :: org.apache.spark#spark-submit-parent-f0ae9b69-adea-4b7c-83c7-fbd549abab85;1.0
[2026-05-19, 16:31:33 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:31:35 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:31:35 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:31:35 UTC] {subprocess.py:93} INFO - 	found org.apache.kafka#kafka-clients;3.4.1 in central
[2026-05-19, 16:31:35 UTC] {subprocess.py:93} INFO - 	found org.lz4#lz4-java;1.8.0 in central
[2026-05-19, 16:31:35 UTC] {subprocess.py:93} INFO - 	found org.xerial.snappy#snappy-java;1.1.10.3 in central
[2026-05-19, 16:31:36 UTC] {subprocess.py:93} INFO - 	found org.slf4j#slf4j-api;2.0.7 in central
[2026-05-19, 16:31:37 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-runtime;3.3.4 in central
[2026-05-19, 16:31:37 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-api;3.3.4 in central
[2026-05-19, 16:31:38 UTC] {subprocess.py:93} INFO - 	found commons-logging#commons-logging;1.1.3 in central
[2026-05-19, 16:31:38 UTC] {subprocess.py:93} INFO - 	found com.google.code.findbugs#jsr305;3.0.0 in central
[2026-05-19, 16:31:40 UTC] {subprocess.py:93} INFO - 	found org.apache.commons#commons-pool2;2.11.1 in central
[2026-05-19, 16:31:40 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:31:40 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1!spark-sql-kafka-0-10_2.12.jar (116ms)
[2026-05-19, 16:31:40 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1!spark-token-provider-kafka-0-10_2.12.jar (50ms)
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.1/kafka-clients-3.4.1.jar ...
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.kafka#kafka-clients;3.4.1!kafka-clients.jar (847ms)
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.0/jsr305-3.0.0.jar ...
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] com.google.code.findbugs#jsr305;3.0.0!jsr305.jar (56ms)
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar ...
[2026-05-19, 16:31:41 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.commons#commons-pool2;2.11.1!commons-pool2.jar (54ms)
[2026-05-19, 16:31:42 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar ...
[2026-05-19, 16:31:48 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-runtime;3.3.4!hadoop-client-runtime.jar (6491ms)
[2026-05-19, 16:31:48 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar ...
[2026-05-19, 16:31:48 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.lz4#lz4-java;1.8.0!lz4-java.jar (174ms)
[2026-05-19, 16:31:48 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.3/snappy-java-1.1.10.3.jar ...
[2026-05-19, 16:31:49 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.xerial.snappy#snappy-java;1.1.10.3!snappy-java.jar(bundle) (394ms)
[2026-05-19, 16:31:49 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.7/slf4j-api-2.0.7.jar ...
[2026-05-19, 16:31:49 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.slf4j#slf4j-api;2.0.7!slf4j-api.jar (58ms)
[2026-05-19, 16:31:49 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar ...
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-api;3.3.4!hadoop-client-api.jar (2799ms)
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar ...
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] commons-logging#commons-logging;1.1.3!commons-logging.jar (51ms)
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - :: resolution report :: resolve 7186ms :: artifacts dl 11094ms
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	:: modules in use:
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	com.google.code.findbugs#jsr305;3.0.0 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	commons-logging#commons-logging;1.1.3 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.commons#commons-pool2;2.11.1 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-api;3.3.4 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-runtime;3.3.4 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.kafka#kafka-clients;3.4.1 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.lz4#lz4-java;1.8.0 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.slf4j#slf4j-api;2.0.7 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	org.xerial.snappy#snappy-java;1.1.10.3 from central in [default]
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	|                  |            modules            ||   artifacts   |
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	|      default     |   11  |   11  |   11  |   0   ||   11  |   11  |
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - :: retrieving :: org.apache.spark#spark-submit-parent-f0ae9b69-adea-4b7c-83c7-fbd549abab85
[2026-05-19, 16:31:51 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:31:52 UTC] {subprocess.py:93} INFO - 	11 artifacts copied, 0 already retrieved (56767kB/42ms)
[2026-05-19, 16:31:52 UTC] {subprocess.py:93} INFO - 26/05/19 16:31:52 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO SparkContext: Running Spark version 3.5.1
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO SparkContext: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO SparkContext: Java version 11.0.22
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceUtils: No custom resources configured for spark.driver.
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO SparkContext: Submitted application: KafkaSparkBatchSentiment
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceProfile: Limiting resource is cpu
[2026-05-19, 16:32:00 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:00 INFO ResourceProfileManager: Added ResourceProfile id: 0
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SecurityManager: Changing view acls to: root
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SecurityManager: Changing modify acls to: root
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SecurityManager: Changing view acls groups to:
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SecurityManager: Changing modify acls groups to:
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: root; groups with view permissions: EMPTY; users with modify permissions: root; groups with modify permissions: EMPTY
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Successfully started service 'sparkDriver' on port 37103.
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkEnv: Registering MapOutputTracker
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkEnv: Registering BlockManagerMaster
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-cefa83e3-7a94-4318-9c2f-70b8e3c524c3
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO MemoryStore: MemoryStore started with capacity 434.4 MiB
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkEnv: Registering OutputCommitCoordinator
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO JettyUtils: Start Jetty 0.0.0.0:4040 for SparkUI
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Successfully started service 'SparkUI' on port 4040.
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at spark://2ed238f5ea52:37103/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at spark://2ed238f5ea52:37103/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at spark://2ed238f5ea52:37103/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at spark://2ed238f5ea52:37103/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at spark://2ed238f5ea52:37103/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at spark://2ed238f5ea52:37103/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added JAR file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at spark://2ed238f5ea52:37103/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO SparkContext: Added file file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Copying /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Starting executor ID driver on host 2ed238f5ea52
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Java version 11.0.22
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Starting executor with user classpath (userClassPathFirst = false): ''
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Created or updated repl class loader org.apache.spark.util.MutableURLClassLoader@61224839 for default.
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO TransportClientFactory: Successfully created connection to 2ed238f5ea52/172.18.0.8:37103 after 10 ms (0 ms spent in bootstraps)
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp2950867167038853130.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp2950867167038853130.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-api-3.3.4.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp14019516401235909289.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp14019516401235909289.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.commons_commons-pool2-2.11.1.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp14637648878940435644.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp14637648878940435644.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/com.google.code.findbugs_jsr305-3.0.0.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp13012795288687667193.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp13012795288687667193.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.slf4j_slf4j-api-2.0.7.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp9840433375620955396.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp9840433375620955396.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.kafka_kafka-clients-3.4.1.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp1120601688970851810.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp1120601688970851810.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/commons-logging_commons-logging-1.1.3.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp6971940759741750187.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp6971940759741750187.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp12893652848246545097.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp12893652848246545097.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp13244205218118680720.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp13244205218118680720.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.lz4_lz4-java-1.8.0.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp9455849842787615856.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp9455849842787615856.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.xerial.snappy_snappy-java-1.1.10.3.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Fetching spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779208320946
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Fetching spark://2ed238f5ea52:37103/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp12010478535500575748.tmp
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/fetchFileTemp12010478535500575748.tmp has been previously copied to /tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Executor: Adding file:/tmp/spark-3b73aa34-75a6-4710-851b-a1a9a0402e93/userFiles-791dece5-fa36-4d73-a10b-abbfd8038490/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 45707.
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO NettyBlockTransferService: Server created on 2ed238f5ea52:45707
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 2ed238f5ea52, 45707, None)
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManagerMasterEndpoint: Registering block manager 2ed238f5ea52:45707 with 434.4 MiB RAM, BlockManagerId(driver, 2ed238f5ea52, 45707, None)
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 2ed238f5ea52, 45707, None)
[2026-05-19, 16:32:01 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:01 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 2ed238f5ea52, 45707, None)
[2026-05-19, 16:32:03 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:03 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset]' were supplied but are not used yet.
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 26/05/19 16:32:13 ERROR FileFormatWriter: Aborting job 0fa029eb-7d7a-4f8e-a4b6-43b5309a69d3.
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - java.io.FileNotFoundException: File file:/results/sentiments/_temporary/0 does not exist
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.RawLocalFileSystem.listStatus(RawLocalFileSystem.java:597)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1972)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:2014)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.ChecksumFileSystem.listStatus(ChecksumFileSystem.java:761)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1972)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:2014)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.getAllCommittedTaskPaths(FileOutputCommitter.java:334)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.commitJobInternal(FileOutputCommitter.java:404)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.commitJob(FileOutputCommitter.java:377)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.internal.io.HadoopMapReduceCommitProtocol.commitJob(HadoopMapReduceCommitProtocol.scala:192)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.$anonfun$writeAndCommit$3(FileFormatWriter.scala:275)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.util.Utils$.timeTakenMs(Utils.scala:552)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.writeAndCommit(FileFormatWriter.scala:275)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.executeWrite(FileFormatWriter.scala:304)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.write(FileFormatWriter.scala:190)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.InsertIntoHadoopFsRelationCommand.run(InsertIntoHadoopFsRelationCommand.scala:190)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult$lzycompute(commands.scala:113)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult(commands.scala:111)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.executeCollect(commands.scala:125)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.$anonfun$applyOrElse$1(QueryExecution.scala:107)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$6(SQLExecution.scala:125)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withSQLConfPropagated(SQLExecution.scala:201)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$1(SQLExecution.scala:108)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withNewExecutionId(SQLExecution.scala:66)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:107)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:98)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.$anonfun$transformDownWithPruning$1(TreeNode.scala:461)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.CurrentOrigin$.withOrigin(origin.scala:76)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDownWithPruning(TreeNode.scala:461)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.org$apache$spark$sql$catalyst$plans$logical$AnalysisHelper$$super$transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning(AnalysisHelper.scala:267)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning$(AnalysisHelper.scala:263)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDown(TreeNode.scala:437)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.eagerlyExecuteCommands(QueryExecution.scala:98)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted$lzycompute(QueryExecution.scala:85)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted(QueryExecution.scala:83)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.assertCommandExecuted(QueryExecution.scala:142)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.runCommand(DataFrameWriter.scala:859)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveToV1Source(DataFrameWriter.scala:388)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveInternal(DataFrameWriter.scala:361)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:240)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.csv(DataFrameWriter.scala:850)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.Gateway.invoke(Gateway.java:282)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.commands.CallCommand.execute(CallCommand.java:79)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.run(ClientServerConnection.java:106)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.Thread.run(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - Traceback (most recent call last):
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 81, in <module>
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -     main()
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 68, in main
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -     result_df
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/sql/readwriter.py", line 1864, in csv
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 179, in deco
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/protocol.py", line 326, in get_return_value
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - py4j.protocol.Py4JJavaError: An error occurred while calling o93.csv.
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - : java.io.FileNotFoundException: File file:/results/sentiments/_temporary/0 does not exist
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.RawLocalFileSystem.listStatus(RawLocalFileSystem.java:597)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1972)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:2014)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.ChecksumFileSystem.listStatus(ChecksumFileSystem.java:761)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1972)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:2014)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.getAllCommittedTaskPaths(FileOutputCommitter.java:334)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.commitJobInternal(FileOutputCommitter.java:404)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter.commitJob(FileOutputCommitter.java:377)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.internal.io.HadoopMapReduceCommitProtocol.commitJob(HadoopMapReduceCommitProtocol.scala:192)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.$anonfun$writeAndCommit$3(FileFormatWriter.scala:275)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.util.Utils$.timeTakenMs(Utils.scala:552)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.writeAndCommit(FileFormatWriter.scala:275)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.executeWrite(FileFormatWriter.scala:304)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.write(FileFormatWriter.scala:190)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.InsertIntoHadoopFsRelationCommand.run(InsertIntoHadoopFsRelationCommand.scala:190)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult$lzycompute(commands.scala:113)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult(commands.scala:111)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.command.DataWritingCommandExec.executeCollect(commands.scala:125)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.$anonfun$applyOrElse$1(QueryExecution.scala:107)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$6(SQLExecution.scala:125)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withSQLConfPropagated(SQLExecution.scala:201)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$1(SQLExecution.scala:108)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withNewExecutionId(SQLExecution.scala:66)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:107)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:98)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.$anonfun$transformDownWithPruning$1(TreeNode.scala:461)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.CurrentOrigin$.withOrigin(origin.scala:76)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDownWithPruning(TreeNode.scala:461)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.org$apache$spark$sql$catalyst$plans$logical$AnalysisHelper$$super$transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning(AnalysisHelper.scala:267)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning$(AnalysisHelper.scala:263)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDown(TreeNode.scala:437)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.eagerlyExecuteCommands(QueryExecution.scala:98)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted$lzycompute(QueryExecution.scala:85)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted(QueryExecution.scala:83)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.assertCommandExecuted(QueryExecution.scala:142)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.runCommand(DataFrameWriter.scala:859)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveToV1Source(DataFrameWriter.scala:388)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveInternal(DataFrameWriter.scala:361)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:240)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.csv(DataFrameWriter.scala:850)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.Gateway.invoke(Gateway.java:282)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.commands.CallCommand.execute(CallCommand.java:79)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.run(ClientServerConnection.java:106)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.Thread.run(Unknown Source)
[2026-05-19, 16:32:13 UTC] {subprocess.py:93} INFO - 
[2026-05-19, 16:32:13 UTC] {subprocess.py:97} INFO - Command exited with return code 1
[2026-05-19, 16:32:13 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
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
airflow.exceptions.AirflowException: Bash command failed. The command returned a non-zero exit code 1.
[2026-05-19, 16:32:13 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=run_ml_sentiment_analysis, run_id=manual__2026-05-19T16:31:30.009322+00:00, execution_date=20260519T163130, start_date=20260519T163132, end_date=20260519T163213
[2026-05-19, 16:32:13 UTC] {taskinstance.py:340} ▶ Post task execution logs