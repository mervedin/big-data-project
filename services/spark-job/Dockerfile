FROM apache/spark:3.5.1

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    build-essential \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Install ML dependencies - explicitly exclude problematic typing-extensions from torch index
RUN pip install --no-cache-dir \
    maturin && \
    pip install --no-cache-dir \
    'typing-extensions<4.5' && \
    pip install --no-cache-dir \
    'transformers==4.25.1' \
    'torch==1.13.1'  --extra-index-url https://download.pytorch.org/whl/cpu

WORKDIR /app

COPY spark_batch.py .
COPY sentiment_logic.py .


CMD /opt/spark/bin/spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  spark_batch.py
