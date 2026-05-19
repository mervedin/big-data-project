
Task
run_ml_sentiment_analysis

Details

Graph

Gantt

Code

Event Log

Logs

XCom



59bf5cec34e2
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T16:26:09.495566+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 16:26:10 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 16:26:10 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 16:26:10 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        docker run --rm           --network big-data-project_default           --mount source=big-data-project_results_data,target=/results           big-data-project-spark-job:latest         && echo "✅ ML sentiment analysis complete"\n        ']
[2026-05-19, 16:26:10 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - :: loading settings :: url = jar:file:/opt/spark/jars/ivy-2.5.1.jar!/org/apache/ivy/core/settings/ivysettings.xml
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - Ivy Default Cache set to: /root/.ivy2/cache
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - The jars for the packages stored in: /root/.ivy2/jars
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - org.apache.spark#spark-sql-kafka-0-10_2.12 added as a dependency
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - :: resolving dependencies :: org.apache.spark#spark-submit-parent-dd99bb2f-e8a5-485d-84b8-84cd80264c55;1.0
[2026-05-19, 16:26:11 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:26:12 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:26:12 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:26:13 UTC] {subprocess.py:93} INFO - 	found org.apache.kafka#kafka-clients;3.4.1 in central
[2026-05-19, 16:26:13 UTC] {subprocess.py:93} INFO - 	found org.lz4#lz4-java;1.8.0 in central
[2026-05-19, 16:26:13 UTC] {subprocess.py:93} INFO - 	found org.xerial.snappy#snappy-java;1.1.10.3 in central
[2026-05-19, 16:26:13 UTC] {subprocess.py:93} INFO - 	found org.slf4j#slf4j-api;2.0.7 in central
[2026-05-19, 16:26:15 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-runtime;3.3.4 in central
[2026-05-19, 16:26:15 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-api;3.3.4 in central
[2026-05-19, 16:26:16 UTC] {subprocess.py:93} INFO - 	found commons-logging#commons-logging;1.1.3 in central
[2026-05-19, 16:26:16 UTC] {subprocess.py:93} INFO - 	found com.google.code.findbugs#jsr305;3.0.0 in central
[2026-05-19, 16:26:18 UTC] {subprocess.py:93} INFO - 	found org.apache.commons#commons-pool2;2.11.1 in central
[2026-05-19, 16:26:18 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:26:19 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1!spark-sql-kafka-0-10_2.12.jar (345ms)
[2026-05-19, 16:26:19 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:26:19 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1!spark-token-provider-kafka-0-10_2.12.jar (125ms)
[2026-05-19, 16:26:19 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.1/kafka-clients-3.4.1.jar ...
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.kafka#kafka-clients;3.4.1!kafka-clients.jar (676ms)
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.0/jsr305-3.0.0.jar ...
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] com.google.code.findbugs#jsr305;3.0.0!jsr305.jar (37ms)
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar ...
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.commons#commons-pool2;2.11.1!commons-pool2.jar (45ms)
[2026-05-19, 16:26:20 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar ...
[2026-05-19, 16:26:22 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-runtime;3.3.4!hadoop-client-runtime.jar (2605ms)
[2026-05-19, 16:26:22 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar ...
[2026-05-19, 16:26:22 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.lz4#lz4-java;1.8.0!lz4-java.jar (96ms)
[2026-05-19, 16:26:22 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.3/snappy-java-1.1.10.3.jar ...
[2026-05-19, 16:26:23 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.xerial.snappy#snappy-java;1.1.10.3!snappy-java.jar(bundle) (217ms)
[2026-05-19, 16:26:23 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.7/slf4j-api-2.0.7.jar ...
[2026-05-19, 16:26:23 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.slf4j#slf4j-api;2.0.7!slf4j-api.jar (41ms)
[2026-05-19, 16:26:23 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar ...
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-api;3.3.4!hadoop-client-api.jar (1701ms)
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar ...
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] commons-logging#commons-logging;1.1.3!commons-logging.jar (40ms)
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - :: resolution report :: resolve 7660ms :: artifacts dl 5939ms
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	:: modules in use:
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	com.google.code.findbugs#jsr305;3.0.0 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	commons-logging#commons-logging;1.1.3 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.commons#commons-pool2;2.11.1 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-api;3.3.4 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-runtime;3.3.4 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.kafka#kafka-clients;3.4.1 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.lz4#lz4-java;1.8.0 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.slf4j#slf4j-api;2.0.7 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	org.xerial.snappy#snappy-java;1.1.10.3 from central in [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	|                  |            modules            ||   artifacts   |
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	|      default     |   11  |   11  |   11  |   0   ||   11  |   11  |
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - :: retrieving :: org.apache.spark#spark-submit-parent-dd99bb2f-e8a5-485d-84b8-84cd80264c55
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 	11 artifacts copied, 0 already retrieved (56767kB/27ms)
[2026-05-19, 16:26:24 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:24 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Running Spark version 3.5.1
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Java version 11.0.22
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceUtils: No custom resources configured for spark.driver.
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Submitted application: KafkaSparkBatchSentiment
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceProfile: Limiting resource is cpu
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO ResourceProfileManager: Added ResourceProfile id: 0
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SecurityManager: Changing view acls to: root
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SecurityManager: Changing modify acls to: root
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SecurityManager: Changing view acls groups to:
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SecurityManager: Changing modify acls groups to:
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: root; groups with view permissions: EMPTY; users with modify permissions: root; groups with modify permissions: EMPTY
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Successfully started service 'sparkDriver' on port 35693.
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkEnv: Registering MapOutputTracker
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkEnv: Registering BlockManagerMaster
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-efe56b2d-6b8e-4dc6-9a3b-0b3eded057e2
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO MemoryStore: MemoryStore started with capacity 434.4 MiB
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkEnv: Registering OutputCommitCoordinator
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO JettyUtils: Start Jetty 0.0.0.0:4040 for SparkUI
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Successfully started service 'SparkUI' on port 4040.
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at spark://9f622a1f48c5:35693/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at spark://9f622a1f48c5:35693/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at spark://9f622a1f48c5:35693/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at spark://9f622a1f48c5:35693/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at spark://9f622a1f48c5:35693/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at spark://9f622a1f48c5:35693/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added JAR file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at spark://9f622a1f48c5:35693/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO SparkContext: Added file file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Copying /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Starting executor ID driver on host 9f622a1f48c5
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Java version 11.0.22
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Starting executor with user classpath (userClassPathFirst = false): ''
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Created or updated repl class loader org.apache.spark.util.MutableURLClassLoader@7a1100f7 for default.
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO TransportClientFactory: Successfully created connection to 9f622a1f48c5/172.18.0.8:35693 after 8 ms (0 ms spent in bootstraps)
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp3220951621617322361.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp3220951621617322361.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.xerial.snappy_snappy-java-1.1.10.3.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp974537719144073949.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp974537719144073949.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.slf4j_slf4j-api-2.0.7.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp11774579021090538736.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp11774579021090538736.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp11086599459091619174.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp11086599459091619174.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.commons_commons-pool2-2.11.1.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp13893826072764381499.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp13893826072764381499.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/commons-logging_commons-logging-1.1.3.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp5418484493006409805.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp5418484493006409805.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/com.google.code.findbugs_jsr305-3.0.0.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp4544827787433235665.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp4544827787433235665.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp12872995796760188674.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp12872995796760188674.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.lz4_lz4-java-1.8.0.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp15344828865690634793.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp15344828865690634793.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp15970490759285640774.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp15970490759285640774.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.kafka_kafka-clients-3.4.1.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Fetching spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207993466
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Fetching spark://9f622a1f48c5:35693/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp8154865894817258859.tmp
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/fetchFileTemp8154865894817258859.tmp has been previously copied to /tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Executor: Adding file:/tmp/spark-91757e71-113d-4413-8de5-53553aa32d9e/userFiles-4f18f118-346c-4586-8e98-1da8e89cad36/org.apache.hadoop_hadoop-client-api-3.3.4.jar to class loader default
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 46021.
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO NettyBlockTransferService: Server created on 9f622a1f48c5:46021
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 9f622a1f48c5, 46021, None)
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManagerMasterEndpoint: Registering block manager 9f622a1f48c5:46021 with 434.4 MiB RAM, BlockManagerId(driver, 9f622a1f48c5, 46021, None)
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 9f622a1f48c5, 46021, None)
[2026-05-19, 16:26:33 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:33 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 9f622a1f48c5, 46021, None)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 26/05/19 16:26:35 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset]' were supplied but are not used yet.
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - Traceback (most recent call last):
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 81, in <module>
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -     main()
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 68, in main
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -     result_df
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/sql/readwriter.py", line 1864, in csv
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 179, in deco
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/protocol.py", line 326, in get_return_value
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - py4j.protocol.Py4JJavaError: An error occurred while calling o93.csv.
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - : java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions(ConsumerStrategy.scala:66)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions$(ConsumerStrategy.scala:65)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.retrieveAllPartitions(ConsumerStrategy.scala:102)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.assignedTopicPartitions(ConsumerStrategy.scala:113)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.fetchPartitionOffsets(KafkaOffsetReaderAdmin.scala:128)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.getOffsetRangesFromUnresolvedOffsets(KafkaOffsetReaderAdmin.scala:374)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaRelation.buildScan(KafkaRelation.scala:67)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.datasources.DataSourceStrategy$.apply(DataSourceStrategy.scala:349)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$1(QueryPlanner.scala:63)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:491)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$3(QueryPlanner.scala:78)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:196)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce$folder$1.apply(TraversableOnce.scala:194)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft(TraversableOnce.scala:199)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableOnce.foldLeft$(TraversableOnce.scala:192)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foldLeft(Iterator.scala:1431)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.$anonfun$plan$2(QueryPlanner.scala:75)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.nextCur(Iterator.scala:486)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:492)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.planning.QueryPlanner.plan(QueryPlanner.scala:93)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SparkStrategies.plan(SparkStrategies.scala:70)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$.createSparkPlan(QueryExecution.scala:496)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$sparkPlan$1(QueryExecution.scala:171)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.QueryPlanningTracker.measurePhase(QueryPlanningTracker.scala:138)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$2(QueryExecution.scala:219)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$.withInternalError(QueryExecution.scala:546)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$1(QueryExecution.scala:219)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.executePhase(QueryExecution.scala:218)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.sparkPlan$lzycompute(QueryExecution.scala:171)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.sparkPlan(QueryExecution.scala:164)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executedPlan$1(QueryExecution.scala:186)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.QueryPlanningTracker.measurePhase(QueryPlanningTracker.scala:138)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$2(QueryExecution.scala:219)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$.withInternalError(QueryExecution.scala:546)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$1(QueryExecution.scala:219)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.executePhase(QueryExecution.scala:218)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.executedPlan$lzycompute(QueryExecution.scala:186)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.executedPlan(QueryExecution.scala:179)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.simpleString(QueryExecution.scala:238)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.org$apache$spark$sql$execution$QueryExecution$$explainString(QueryExecution.scala:284)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.explainString(QueryExecution.scala:252)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$6(SQLExecution.scala:117)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withSQLConfPropagated(SQLExecution.scala:201)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$1(SQLExecution.scala:108)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.SQLExecution$.withNewExecutionId(SQLExecution.scala:66)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:107)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.applyOrElse(QueryExecution.scala:98)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.$anonfun$transformDownWithPruning$1(TreeNode.scala:461)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.CurrentOrigin$.withOrigin(origin.scala:76)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDownWithPruning(TreeNode.scala:461)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.org$apache$spark$sql$catalyst$plans$logical$AnalysisHelper$$super$transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning(AnalysisHelper.scala:267)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper.transformDownWithPruning$(AnalysisHelper.scala:263)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.transformDownWithPruning(LogicalPlan.scala:32)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.catalyst.trees.TreeNode.transformDown(TreeNode.scala:437)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.eagerlyExecuteCommands(QueryExecution.scala:98)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted$lzycompute(QueryExecution.scala:85)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.commandExecuted(QueryExecution.scala:83)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.QueryExecution.assertCommandExecuted(QueryExecution.scala:142)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.runCommand(DataFrameWriter.scala:859)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveToV1Source(DataFrameWriter.scala:388)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.saveInternal(DataFrameWriter.scala:361)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:240)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.DataFrameWriter.csv(DataFrameWriter.scala:850)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.Gateway.invoke(Gateway.java:282)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.commands.CallCommand.execute(CallCommand.java:79)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at py4j.ClientServerConnection.run(ClientServerConnection.java:106)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 	at java.base/java.lang.Thread.run(Unknown Source)
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - Caused by: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:26:35 UTC] {subprocess.py:93} INFO - 
[2026-05-19, 16:26:35 UTC] {subprocess.py:97} INFO - Command exited with return code 1
[2026-05-19, 16:26:35 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
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
[2026-05-19, 16:26:35 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=run_ml_sentiment_analysis, run_id=manual__2026-05-19T16:26:09.495566+00:00, execution_date=20260519T162609, start_date=20260519T162610, end_date=20260519T162635
[2026-05-19, 16:26:35 UTC] {taskinstance.py:340} ▶ Post task execution logs