

Details

Graph

Gantt

Code

Event Log

Logs

XCom



104ad4af7e3f
*** Found local files:
***   * /opt/airflow/logs/dag_id=batch_kafka_spark_pipeline/run_id=manual__2026-05-19T16:18:10.637296+00:00/task_id=run_ml_sentiment_analysis/attempt=1.log
[2026-05-19, 16:18:12 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2026-05-19, 16:18:12 UTC] {subprocess.py:63} INFO - Tmp dir root location: /tmp
[2026-05-19, 16:18:12 UTC] {subprocess.py:75} INFO - Running command: ['/usr/bin/bash', '-c', '\n        docker run --rm           --network big-data-project_default           --mount source=big-data-project_results_data,target=/results           big-data-project-spark-job:latest         && echo "✅ ML sentiment analysis complete"\n        ']
[2026-05-19, 16:18:12 UTC] {subprocess.py:86} INFO - Output:
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - :: loading settings :: url = jar:file:/opt/spark/jars/ivy-2.5.1.jar!/org/apache/ivy/core/settings/ivysettings.xml
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - Ivy Default Cache set to: /root/.ivy2/cache
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - The jars for the packages stored in: /root/.ivy2/jars
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - org.apache.spark#spark-sql-kafka-0-10_2.12 added as a dependency
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - :: resolving dependencies :: org.apache.spark#spark-submit-parent-b0a44078-d8a5-4c2f-8e7a-89443a78984a;1.0
[2026-05-19, 16:18:12 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.apache.kafka#kafka-clients;3.4.1 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.lz4#lz4-java;1.8.0 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.xerial.snappy#snappy-java;1.1.10.3 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.slf4j#slf4j-api;2.0.7 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-runtime;3.3.4 in central
[2026-05-19, 16:18:13 UTC] {subprocess.py:93} INFO - 	found org.apache.hadoop#hadoop-client-api;3.3.4 in central
[2026-05-19, 16:18:15 UTC] {subprocess.py:93} INFO - 	found commons-logging#commons-logging;1.1.3 in central
[2026-05-19, 16:18:15 UTC] {subprocess.py:93} INFO - 	found com.google.code.findbugs#jsr305;3.0.0 in central
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - 	found org.apache.commons#commons-pool2;2.11.1 in central
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1!spark-sql-kafka-0-10_2.12.jar (114ms)
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar ...
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1!spark-token-provider-kafka-0-10_2.12.jar (44ms)
[2026-05-19, 16:18:17 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.1/kafka-clients-3.4.1.jar ...
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.kafka#kafka-clients;3.4.1!kafka-clients.jar (606ms)
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.0/jsr305-3.0.0.jar ...
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] com.google.code.findbugs#jsr305;3.0.0!jsr305.jar (53ms)
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar ...
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.commons#commons-pool2;2.11.1!commons-pool2.jar (57ms)
[2026-05-19, 16:18:18 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar ...
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-runtime;3.3.4!hadoop-client-runtime.jar (5690ms)
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar ...
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.lz4#lz4-java;1.8.0!lz4-java.jar (159ms)
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.3/snappy-java-1.1.10.3.jar ...
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.xerial.snappy#snappy-java;1.1.10.3!snappy-java.jar(bundle) (415ms)
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.7/slf4j-api-2.0.7.jar ...
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.slf4j#slf4j-api;2.0.7!slf4j-api.jar (47ms)
[2026-05-19, 16:18:24 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar ...
[2026-05-19, 16:18:27 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] org.apache.hadoop#hadoop-client-api;3.3.4!hadoop-client-api.jar (3326ms)
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - downloading https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar ...
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	[SUCCESSFUL ] commons-logging#commons-logging;1.1.3!commons-logging.jar (49ms)
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - :: resolution report :: resolve 4703ms :: artifacts dl 10567ms
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	:: modules in use:
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	com.google.code.findbugs#jsr305;3.0.0 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	commons-logging#commons-logging;1.1.3 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.commons#commons-pool2;2.11.1 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-api;3.3.4 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.hadoop#hadoop-client-runtime;3.3.4 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.kafka#kafka-clients;3.4.1 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-sql-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.5.1 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.lz4#lz4-java;1.8.0 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.slf4j#slf4j-api;2.0.7 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	org.xerial.snappy#snappy-java;1.1.10.3 from central in [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	|                  |            modules            ||   artifacts   |
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	|      default     |   11  |   11  |   11  |   0   ||   11  |   11  |
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	---------------------------------------------------------------------
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - :: retrieving :: org.apache.spark#spark-submit-parent-b0a44078-d8a5-4c2f-8e7a-89443a78984a
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	confs: [default]
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 	11 artifacts copied, 0 already retrieved (56767kB/32ms)
[2026-05-19, 16:18:28 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkContext: Running Spark version 3.5.1
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkContext: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkContext: Java version 11.0.22
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceUtils: No custom resources configured for spark.driver.
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceUtils: ==============================================================
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkContext: Submitted application: KafkaSparkBatchSentiment
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceProfile: Limiting resource is cpu
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO ResourceProfileManager: Added ResourceProfile id: 0
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SecurityManager: Changing view acls to: root
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SecurityManager: Changing modify acls to: root
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SecurityManager: Changing view acls groups to:
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SecurityManager: Changing modify acls groups to:
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: root; groups with view permissions: EMPTY; users with modify permissions: root; groups with modify permissions: EMPTY
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO Utils: Successfully started service 'sparkDriver' on port 33403.
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkEnv: Registering MapOutputTracker
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkEnv: Registering BlockManagerMaster
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-80d690ce-09d4-41cd-b70c-aea22eb0ded1
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO MemoryStore: MemoryStore started with capacity 434.4 MiB
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO SparkEnv: Registering OutputCommitCoordinator
[2026-05-19, 16:18:36 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:36 INFO JettyUtils: Start Jetty 0.0.0.0:4040 for SparkUI
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Successfully started service 'SparkUI' on port 4040.
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at spark://8a112dd440b9:33403/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at spark://8a112dd440b9:33403/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at spark://8a112dd440b9:33403/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at spark://8a112dd440b9:33403/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at spark://8a112dd440b9:33403/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at spark://8a112dd440b9:33403/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at spark://8a112dd440b9:33403/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at spark://8a112dd440b9:33403/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added JAR file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at spark://8a112dd440b9:33403/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar at file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar at file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar at file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar at file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar at file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar at file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar at file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar at file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO SparkContext: Added file file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar at file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Copying /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Starting executor ID driver on host 8a112dd440b9
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: OS info Linux, 6.12.76-linuxkit, aarch64
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Java version 11.0.22
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Starting executor with user classpath (userClassPathFirst = false): ''
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Created or updated repl class loader org.apache.spark.util.MutableURLClassLoader@7af726e6 for default.
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/com.google.code.findbugs_jsr305-3.0.0.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.slf4j_slf4j-api-2.0.7.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.commons_commons-pool2-2.11.1.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/commons-logging_commons-logging-1.1.3.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.lz4_lz4-java-1.8.0.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.kafka_kafka-clients-3.4.1.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching file:///root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /root/.ivy2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.lz4_lz4-java-1.8.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO TransportClientFactory: Successfully created connection to 8a112dd440b9/172.18.0.9:33403 after 13 ms (0 ms spent in bootstraps)
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.lz4_lz4-java-1.8.0.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp6725051026558734770.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp6725051026558734770.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.lz4_lz4-java-1.8.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.lz4_lz4-java-1.8.0.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-api-3.3.4.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp14078755059032521480.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp14078755059032521480.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-api-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-api-3.3.4.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.xerial.snappy_snappy-java-1.1.10.3.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp16019679870286207799.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp16019679870286207799.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.xerial.snappy_snappy-java-1.1.10.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.xerial.snappy_snappy-java-1.1.10.3.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.slf4j_slf4j-api-2.0.7.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.slf4j_slf4j-api-2.0.7.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8569106823151486696.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8569106823151486696.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.slf4j_slf4j-api-2.0.7.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.slf4j_slf4j-api-2.0.7.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.commons_commons-pool2-2.11.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.commons_commons-pool2-2.11.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp17371995186701252429.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp17371995186701252429.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.commons_commons-pool2-2.11.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.commons_commons-pool2-2.11.1.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/commons-logging_commons-logging-1.1.3.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/commons-logging_commons-logging-1.1.3.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp12750360351453718012.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp12750360351453718012.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/commons-logging_commons-logging-1.1.3.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/commons-logging_commons-logging-1.1.3.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.kafka_kafka-clients-3.4.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.kafka_kafka-clients-3.4.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8724075544168466059.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8724075544168466059.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.kafka_kafka-clients-3.4.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.kafka_kafka-clients-3.4.1.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/com.google.code.findbugs_jsr305-3.0.0.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/com.google.code.findbugs_jsr305-3.0.0.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp2872130401966540932.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp2872130401966540932.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/com.google.code.findbugs_jsr305-3.0.0.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/com.google.code.findbugs_jsr305-3.0.0.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp16441230739492098221.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp16441230739492098221.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp668480934355950137.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp668480934355950137.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.spark_spark-sql-kafka-0-10_2.12-3.5.1.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Fetching spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar with timestamp 1779207516759
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Fetching spark://8a112dd440b9:33403/jars/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8375937820589424558.tmp
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/fetchFileTemp8375937820589424558.tmp has been previously copied to /tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Executor: Adding file:/tmp/spark-c09b962f-fa69-4222-ae75-db9b74f3e64f/userFiles-d0d8532e-0a54-4fb4-be15-36e49f6bf7fa/org.apache.hadoop_hadoop-client-runtime-3.3.4.jar to class loader default
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 40233.
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO NettyBlockTransferService: Server created on 8a112dd440b9:40233
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 8a112dd440b9, 40233, None)
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO BlockManagerMasterEndpoint: Registering block manager 8a112dd440b9:40233 with 434.4 MiB RAM, BlockManagerId(driver, 8a112dd440b9, 40233, None)
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 8a112dd440b9, 40233, None)
[2026-05-19, 16:18:37 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:37 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 8a112dd440b9, 40233, None)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:38 WARN ResolveWriteToStream: spark.sql.adaptive.enabled is not supported in streaming DataFrames/Datasets and will be disabled.
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:38 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset, consumer.commit.groupid]' were supplied but are not used yet.
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:38 WARN KafkaOffsetReaderAdmin: Error in attempt 1 getting Kafka offsets:
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions(ConsumerStrategy.scala:66)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions$(ConsumerStrategy.scala:65)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.retrieveAllPartitions(ConsumerStrategy.scala:102)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.assignedTopicPartitions(ConsumerStrategy.scala:113)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.$anonfun$partitionsAssignedToAdmin$1(KafkaOffsetReaderAdmin.scala:499)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.withRetries(KafkaOffsetReaderAdmin.scala:518)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.partitionsAssignedToAdmin(KafkaOffsetReaderAdmin.scala:498)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.fetchEarliestOffsets(KafkaOffsetReaderAdmin.scala:288)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.$anonfun$getOrCreateInitialPartitionOffsets$1(KafkaMicroBatchStream.scala:244)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.getOrCreateInitialPartitionOffsets(KafkaMicroBatchStream.scala:241)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.initialOffset(KafkaMicroBatchStream.scala:98)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$getStartOffset$2(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.getStartOffset(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$4(MicroBatchExecution.scala:491)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$2(MicroBatchExecution.scala:490)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.$anonfun$map$1(TraversableLike.scala:286)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach(IterableLike.scala:74)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach$(IterableLike.scala:73)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterable.foreach(Iterable.scala:56)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map(TraversableLike.scala:286)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map$(TraversableLike.scala:279)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractTraversable.map(Traversable.scala:108)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$1(MicroBatchExecution.scala:479)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcZ$sp.apply(JFunction0$mcZ$sp.java:23)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.withProgressLocked(MicroBatchExecution.scala:810)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.constructNextBatch(MicroBatchExecution.scala:475)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$2(MicroBatchExecution.scala:268)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$1(MicroBatchExecution.scala:249)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.SingleBatchExecutor.execute(TriggerExecutor.scala:39)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.runActivatedStream(MicroBatchExecution.scala:239)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.$anonfun$runStream$1(StreamExecution.scala:311)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.org$apache$spark$sql$execution$streaming$StreamExecution$$runStream(StreamExecution.scala:289)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.$anonfun$run$1(StreamExecution.scala:211)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.JobArtifactSet$.withActiveJobArtifactState(JobArtifactSet.scala:94)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.run(StreamExecution.scala:211)
[2026-05-19, 16:18:38 UTC] {subprocess.py:93} INFO - Caused by: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:39 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset, consumer.commit.groupid]' were supplied but are not used yet.
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:39 WARN KafkaOffsetReaderAdmin: Error in attempt 2 getting Kafka offsets:
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions(ConsumerStrategy.scala:66)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions$(ConsumerStrategy.scala:65)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.retrieveAllPartitions(ConsumerStrategy.scala:102)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.assignedTopicPartitions(ConsumerStrategy.scala:113)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.$anonfun$partitionsAssignedToAdmin$1(KafkaOffsetReaderAdmin.scala:499)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.withRetries(KafkaOffsetReaderAdmin.scala:518)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.partitionsAssignedToAdmin(KafkaOffsetReaderAdmin.scala:498)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.fetchEarliestOffsets(KafkaOffsetReaderAdmin.scala:288)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.$anonfun$getOrCreateInitialPartitionOffsets$1(KafkaMicroBatchStream.scala:244)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.getOrCreateInitialPartitionOffsets(KafkaMicroBatchStream.scala:241)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.initialOffset(KafkaMicroBatchStream.scala:98)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$getStartOffset$2(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.getStartOffset(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$4(MicroBatchExecution.scala:491)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$2(MicroBatchExecution.scala:490)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.$anonfun$map$1(TraversableLike.scala:286)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach(IterableLike.scala:74)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach$(IterableLike.scala:73)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterable.foreach(Iterable.scala:56)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map(TraversableLike.scala:286)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map$(TraversableLike.scala:279)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractTraversable.map(Traversable.scala:108)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$1(MicroBatchExecution.scala:479)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcZ$sp.apply(JFunction0$mcZ$sp.java:23)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.withProgressLocked(MicroBatchExecution.scala:810)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.constructNextBatch(MicroBatchExecution.scala:475)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$2(MicroBatchExecution.scala:268)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$1(MicroBatchExecution.scala:249)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.SingleBatchExecutor.execute(TriggerExecutor.scala:39)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.runActivatedStream(MicroBatchExecution.scala:239)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.$anonfun$runStream$1(StreamExecution.scala:311)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.org$apache$spark$sql$execution$streaming$StreamExecution$$runStream(StreamExecution.scala:289)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.$anonfun$run$1(StreamExecution.scala:211)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.JobArtifactSet$.withActiveJobArtifactState(JobArtifactSet.scala:94)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.run(StreamExecution.scala:211)
[2026-05-19, 16:18:39 UTC] {subprocess.py:93} INFO - Caused by: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:40 WARN AdminClientConfig: These configurations '[key.deserializer, value.deserializer, enable.auto.commit, max.poll.records, auto.offset.reset, consumer.commit.groupid]' were supplied but are not used yet.
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:40 WARN KafkaOffsetReaderAdmin: Error in attempt 3 getting Kafka offsets:
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions(ConsumerStrategy.scala:66)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions$(ConsumerStrategy.scala:65)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.retrieveAllPartitions(ConsumerStrategy.scala:102)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.assignedTopicPartitions(ConsumerStrategy.scala:113)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.$anonfun$partitionsAssignedToAdmin$1(KafkaOffsetReaderAdmin.scala:499)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.withRetries(KafkaOffsetReaderAdmin.scala:518)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.partitionsAssignedToAdmin(KafkaOffsetReaderAdmin.scala:498)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.fetchEarliestOffsets(KafkaOffsetReaderAdmin.scala:288)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.$anonfun$getOrCreateInitialPartitionOffsets$1(KafkaMicroBatchStream.scala:244)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.getOrCreateInitialPartitionOffsets(KafkaMicroBatchStream.scala:241)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.initialOffset(KafkaMicroBatchStream.scala:98)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$getStartOffset$2(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.getStartOffset(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$4(MicroBatchExecution.scala:491)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$2(MicroBatchExecution.scala:490)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.$anonfun$map$1(TraversableLike.scala:286)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach(IterableLike.scala:74)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach$(IterableLike.scala:73)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterable.foreach(Iterable.scala:56)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map(TraversableLike.scala:286)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map$(TraversableLike.scala:279)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractTraversable.map(Traversable.scala:108)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$1(MicroBatchExecution.scala:479)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcZ$sp.apply(JFunction0$mcZ$sp.java:23)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.withProgressLocked(MicroBatchExecution.scala:810)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.constructNextBatch(MicroBatchExecution.scala:475)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$2(MicroBatchExecution.scala:268)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$1(MicroBatchExecution.scala:249)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.SingleBatchExecutor.execute(TriggerExecutor.scala:39)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.runActivatedStream(MicroBatchExecution.scala:239)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.$anonfun$runStream$1(StreamExecution.scala:311)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.org$apache$spark$sql$execution$streaming$StreamExecution$$runStream(StreamExecution.scala:289)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.$anonfun$run$1(StreamExecution.scala:211)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.JobArtifactSet$.withActiveJobArtifactState(JobArtifactSet.scala:94)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.run(StreamExecution.scala:211)
[2026-05-19, 16:18:40 UTC] {subprocess.py:93} INFO - Caused by: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 26/05/19 16:18:41 ERROR MicroBatchExecution: Query [id = 5f47e3ef-52e6-40b0-a8a4-327433076ef9, runId = 0755bfd3-9d29-4879-b0a3-c337c4dd43db] terminated with error
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions(ConsumerStrategy.scala:66)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.ConsumerStrategy.retrieveAllPartitions$(ConsumerStrategy.scala:65)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.retrieveAllPartitions(ConsumerStrategy.scala:102)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.SubscribeStrategy.assignedTopicPartitions(ConsumerStrategy.scala:113)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.$anonfun$partitionsAssignedToAdmin$1(KafkaOffsetReaderAdmin.scala:499)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.withRetries(KafkaOffsetReaderAdmin.scala:518)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.partitionsAssignedToAdmin(KafkaOffsetReaderAdmin.scala:498)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaOffsetReaderAdmin.fetchEarliestOffsets(KafkaOffsetReaderAdmin.scala:288)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.$anonfun$getOrCreateInitialPartitionOffsets$1(KafkaMicroBatchStream.scala:244)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.getOrCreateInitialPartitionOffsets(KafkaMicroBatchStream.scala:241)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.kafka010.KafkaMicroBatchStream.initialOffset(KafkaMicroBatchStream.scala:98)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$getStartOffset$2(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.Option.getOrElse(Option.scala:189)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.getStartOffset(MicroBatchExecution.scala:457)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$4(MicroBatchExecution.scala:491)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$2(MicroBatchExecution.scala:490)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.$anonfun$map$1(TraversableLike.scala:286)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach(Iterator.scala:943)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.Iterator.foreach$(Iterator.scala:943)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach(IterableLike.scala:74)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.IterableLike.foreach$(IterableLike.scala:73)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractIterable.foreach(Iterable.scala:56)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map(TraversableLike.scala:286)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.TraversableLike.map$(TraversableLike.scala:279)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.collection.AbstractTraversable.map(Traversable.scala:108)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$constructNextBatch$1(MicroBatchExecution.scala:479)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcZ$sp.apply(JFunction0$mcZ$sp.java:23)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.withProgressLocked(MicroBatchExecution.scala:810)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.constructNextBatch(MicroBatchExecution.scala:475)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$2(MicroBatchExecution.scala:268)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken(ProgressReporter.scala:427)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.ProgressReporter.reportTimeTaken$(ProgressReporter.scala:425)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.reportTimeTaken(StreamExecution.scala:67)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.$anonfun$runActivatedStream$1(MicroBatchExecution.scala:249)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.SingleBatchExecutor.execute(TriggerExecutor.scala:39)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.MicroBatchExecution.runActivatedStream(MicroBatchExecution.scala:239)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.$anonfun$runStream$1(StreamExecution.scala:311)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:900)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution.org$apache$spark$sql$execution$streaming$StreamExecution$$runStream(StreamExecution.scala:289)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.$anonfun$run$1(StreamExecution.scala:211)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.JobArtifactSet$.withActiveJobArtifactState(JobArtifactSet.scala:94)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - 	at org.apache.spark.sql.execution.streaming.StreamExecution$$anon$1.run(StreamExecution.scala:211)
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - Caused by: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - Traceback (most recent call last):
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 97, in <module>
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -     main()
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -   File "/app/spark_batch.py", line 92, in main
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -     query.awaitTermination()
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/sql/streaming/query.py", line 221, in awaitTermination
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO -   File "/opt/spark/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 185, in deco
[2026-05-19, 16:18:41 UTC] {subprocess.py:93} INFO - pyspark.errors.exceptions.captured.StreamingQueryException: [STREAM_FAILED] Query [id = 5f47e3ef-52e6-40b0-a8a4-327433076ef9, runId = 0755bfd3-9d29-4879-b0a3-c337c4dd43db] terminated with exception: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
[2026-05-19, 16:18:42 UTC] {subprocess.py:97} INFO - Command exited with return code 1
[2026-05-19, 16:18:42 UTC] {taskinstance.py:3310} ERROR - Task failed with exception
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
[2026-05-19, 16:18:42 UTC] {taskinstance.py:1225} INFO - Marking task as UP_FOR_RETRY. dag_id=batch_kafka_spark_pipeline, task_id=run_ml_sentiment_analysis, run_id=manual__2026-05-19T16:18:10.637296+00:00, execution_date=20260519T161810, start_date=20260519T161812, end_date=20260519T161842
[2026-05-19, 16:18:42 UTC] {taskinstance.py:340} ▶ Post task execution logs