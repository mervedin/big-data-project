FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN TMPDIR=/var/tmp pip3 install --no-cache-dir -r requirements.txt

COPY batch_pipeline.py .

CMD ["python", "batch_pipeline.py"]
