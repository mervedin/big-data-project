FROM apache/spark:3.5.1

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Pin huggingface_hub<0.36 to avoid hf-xet which requires Rust edition2024
# Install torch CPU-only build to keep image size manageable
RUN pip install --no-cache-dir \
    'huggingface_hub==0.35.0' && \
    pip install --no-cache-dir \
    'transformers==4.40.2' \
    'torch==2.1.2' --extra-index-url https://download.pytorch.org/whl/cpu

WORKDIR /app

COPY spark_batch.py .
COPY sentiment_logic.py .


CMD /opt/spark/bin/spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  spark_batch.py
