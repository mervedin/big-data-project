FROM apache/spark:3.5.1

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install all ML deps in one command so pip resolves versions together.
# huggingface_hub is pinned to <0.30 to avoid hf-xet (broken on aarch64/amd64).
# transformers 4.40.2 requires huggingface_hub>=0.23.0, so 0.25.2 satisfies it.
RUN pip install --no-cache-dir \
    'typing-extensions==4.7.1' \
    'huggingface_hub==0.25.2' \
    'transformers==4.40.2' \
    'torch==2.1.2' \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Pre-download DistilBERT model at build time so it's baked into the image.
# This avoids a 7+ minute download at runtime which causes task timeouts.
RUN python3 -c "\
from transformers import pipeline; \
pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english', device=-1); \
print('Model cached successfully')"

WORKDIR /app

COPY spark_batch.py .
COPY sentiment_logic.py .


CMD /opt/spark/bin/spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  spark_batch.py
