 => ERROR [3/6] RUN pip install --no-cache-dir     'huggingface_hub==0.2  20.3s
------                                                                          
 > [3/6] RUN pip install --no-cache-dir     'huggingface_hub==0.25.2'     'transformers==4.40.2'     'torch==2.1.2'     --extra-index-url https://download.pytorch.org/whl/cpu:
0.407 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu
1.326 Collecting huggingface_hub==0.25.2
1.526   Downloading huggingface_hub-0.25.2-py3-none-any.whl (436 kB)
2.301 Collecting transformers==4.40.2
2.355   Downloading transformers-4.40.2-py3-none-any.whl (9.0 MB)
4.743 Collecting torch==2.1.2
4.796   Downloading torch-2.1.2-cp38-cp38-manylinux2014_aarch64.whl (84.1 MB)
17.11 Collecting fsspec>=2023.5.0
17.16   Downloading fsspec-2025.3.0-py3-none-any.whl (193 kB)
17.78 Collecting tqdm>=4.42.1
17.83   Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
18.42 Collecting requests
18.54   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
19.26 Collecting packaging>=20.9
19.40   Downloading packaging-26.2-py3-none-any.whl (100 kB)
20.09 Collecting typing-extensions>=3.7.4.3
20.10   Downloading https://download.pytorch.org/whl/typing_extensions-4.15.0-py3-none-any.whl (44 kB)
20.22 ERROR: Package 'typing-extensions' requires a different Python: 3.8.10 not in '>=3.9'
------
[+] build 0/1
 ⠙ Image big-data-project-spark-job Building                               21.5s
Dockerfile:13

--------------------

  12 |     # transformers 4.40.2 requires huggingface_hub>=0.23.0, so 0.25.2 satisfies it.

  13 | >>> RUN pip install --no-cache-dir \

  14 | >>>     'huggingface_hub==0.25.2' \

  15 | >>>     'transformers==4.40.2' \

  16 | >>>     'torch==2.1.2' \

  17 | >>>     --extra-index-url https://download.pytorch.org/whl/cpu

  18 |     

--------------------

failed to solve: process "/bin/sh -c pip install --no-cache-dir     'huggingface_hub==0.25.2'     'transformers==4.40.2'     'torch==2.1.2'     --extra-index-url https://download.pytorch.org/whl/cpu" did not complete successfully: exit code: 1
