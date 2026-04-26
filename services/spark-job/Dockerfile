FROM apache/spark:3.5.1

USER root

WORKDIR /app

COPY spark_batch.py .
COPY sentiment_logic.py .


CMD /opt/spark/bin/spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  spark_batch.py
