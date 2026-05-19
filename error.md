mervedin@172-2-1-178 big-data-project % docker-compose build
WARN[0000] /Users/mervedin/Desktop/big_data/big-data-project/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 16.8s (22/25)                                                      
 => [internal] load local bake definitions                                 0.0s
 => => reading from stdin 1.14kB                                           0.0s
 => [spark-job internal] load build definition from Dockerfile             0.0s
 => => transferring dockerfile: 742B                                       0.0s
 => [news-api internal] load build definition from Dockerfile              0.0s
 => => transferring dockerfile: 404B                                       0.0s
 => [spark-job internal] load metadata for docker.io/apache/spark:3.5.1    1.0s
 => [news-api internal] load metadata for docker.io/library/python:3.10-s  1.2s
 => [auth] library/python:pull token for registry-1.docker.io              0.0s
 => [auth] apache/spark:pull token for registry-1.docker.io                0.0s
 => [spark-job internal] load .dockerignore                                0.0s
 => => transferring context: 2B                                            0.0s
 => CACHED [spark-job 1/6] FROM docker.io/apache/spark:3.5.1@sha256:b49e3  0.0s
 => => resolve docker.io/apache/spark:3.5.1@sha256:b49e3b73ce385c1693cc32  0.0s
 => [spark-job internal] load build context                                0.0s
 => => transferring context: 74B                                           0.0s
 => [spark-job 2/6] RUN apt-get update && apt-get install -y     python3-  8.4s
 => [news-api internal] load .dockerignore                                 0.0s
 => => transferring context: 2B                                            0.0s
 => [news-api 1/6] FROM docker.io/library/python:3.10-slim@sha256:a3699f9  0.0s
 => => resolve docker.io/library/python:3.10-slim@sha256:a3699f905b890636  0.0s
 => [news-api internal] load build context                                 0.0s
 => => transferring context: 10.96kB                                       0.0s
 => CACHED [news-api 2/6] WORKDIR /app                                     0.0s
 => CACHED [news-api 3/6] RUN apt-get update && apt-get install -y     gc  0.0s
 => CACHED [news-api 4/6] COPY requirements.txt .                          0.0s
 => CACHED [news-api 5/6] RUN pip install --no-cache-dir -r requirements.  0.0s
 => [news-api 6/6] COPY main.py .                                          0.0s
 => [news-api] exporting to image                                          0.1s
 => => exporting layers                                                    0.0s
 => => exporting manifest sha256:71908bb608ed95980cc1d20e4a5618dd54f28bb9  0.0s
 => => exporting config sha256:b4ddc933f2222639821ce20ebe3de60cd5900aed0b  0.0s
 => => exporting attestation manifest sha256:abe202ead14bae1b7f8a6670910b  0.0s
 => => exporting manifest list sha256:1ffcdc318e4f0b9fc686d8521ed37ed4491  0.0s
 => => naming to docker.io/library/big-data-project-news-api:latest        0.0s
 => => unpacking to docker.io/library/big-data-project-news-api:latest     0.0s
 => [news-api] resolving provenance for metadata file                      0.0s
 => ERROR [spark-job 3/6] RUN pip install --no-cache-dir     'huggingface  7.1s
------
 > [spark-job 3/6] RUN pip install --no-cache-dir     'huggingface_hub==0.35.0' &&     pip install --no-cache-dir     'transformers==4.40.2'     'torch==2.1.2' --extra-index-url https://download.pytorch.org/whl/cpu:
0.632 Collecting huggingface_hub==0.35.0
0.846   Downloading huggingface_hub-0.35.0-py3-none-any.whl (563 kB)
1.168 Collecting typing-extensions>=3.7.4.3
1.219   Downloading typing_extensions-4.13.2-py3-none-any.whl (45 kB)
1.308 Collecting fsspec>=2023.5.0
1.364   Downloading fsspec-2025.3.0-py3-none-any.whl (193 kB)
1.559 Collecting filelock
1.611   Downloading filelock-3.16.1-py3-none-any.whl (16 kB)
1.717 Collecting tqdm>=4.42.1
1.769   Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
1.885 Collecting hf-xet<2.0.0,>=1.1.3; platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "arm64" or platform_machine == "aarch64"
2.041   Downloading hf_xet-1.5.0.tar.gz (837 kB)
2.192   Installing build dependencies: started
6.157   Installing build dependencies: finished with status 'done'
6.157   Getting requirements to build wheel: started
6.171   Getting requirements to build wheel: finished with status 'done'
6.172   Installing backend dependencies: started
7.112   Installing backend dependencies: finished with status 'error'
7.112   ERROR: Command errored out with exit status 1:
7.112    command: /usr/bin/python3 /usr/lib/python3/dist-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-9yczre1y/normal --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- puccinialin
7.112        cwd: None
7.112   Complete output (2 lines):
7.112   ERROR: Could not find a version that satisfies the requirement puccinialin (from versions: none)
7.112   ERROR: No matching distribution found for puccinialin
7.112   ----------------------------------------
7.119 ERROR: Command errored out with exit status 1: /usr/bin/python3 /usr/lib/python3/dist-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-9yczre1y/normal --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- puccinialin Check the logs for full command output.
------
[+] build 0/2
 ⠙ Image big-data-project-news-api  Building                               16.8s
 ⠙ Image big-data-project-spark-job Building                               16.8s
Dockerfile:13

--------------------

  12 |     # Install torch CPU-only build to keep image size manageable

  13 | >>> RUN pip install --no-cache-dir \

  14 | >>>     'huggingface_hub==0.35.0' && \

  15 | >>>     pip install --no-cache-dir \

  16 | >>>     'transformers==4.40.2' \

  17 | >>>     'torch==2.1.2' --extra-index-url https://download.pytorch.org/whl/cpu

  18 |     

--------------------

target spark-job: failed to solve: process "/bin/sh -c pip install --no-cache-dir     'huggingface_hub==0.35.0' &&     pip install --no-cache-dir     'transformers==4.40.2'     'torch==2.1.2' --extra-index-url https://download.pytorch.org/whl/cpu" did not complete successfully: exit code: 1