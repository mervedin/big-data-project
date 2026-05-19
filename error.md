 > [3/6] RUN pip install --no-cache-dir     maturin &&     pip install --no-cache-dir     'typing-extensions<4.5' &&     pip install --no-cache-dir     'transformers==4.25.1'     'torch==1.13.1'  --extra-index-url https://download.pytorch.org/whl/cpu:
0.895 Collecting maturin
1.113   Downloading maturin-1.13.3-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.musllinux_1_1_aarch64.whl (10.1 MB)
9.810 Collecting tomli>=1.1.0; python_full_version < "3.11"
9.858   Downloading tomli-2.4.1-py3-none-any.whl (14 kB)
9.865 Installing collected packages: tomli, maturin
9.965 Successfully installed maturin-1.13.3 tomli-2.4.1
10.42 Collecting typing-extensions<4.5
10.57   Downloading typing_extensions-4.4.0-py3-none-any.whl (26 kB)
10.59 Installing collected packages: typing-extensions
10.60 Successfully installed typing-extensions-4.4.0
10.89 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu
11.71 Collecting transformers==4.25.1
11.88   Downloading transformers-4.25.1-py3-none-any.whl (5.8 MB)
14.01 Collecting torch==1.13.1
14.06   Downloading torch-1.13.1-cp38-cp38-manylinux2014_aarch64.whl (60.5 MB)
26.25 Collecting tokenizers!=0.11.3,<0.14,>=0.11.1
26.30   Downloading tokenizers-0.13.3-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (7.5 MB)
29.15 Collecting regex!=2019.12.17
29.20   Downloading regex-2024.11.6-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (783 kB)
30.10 Collecting filelock
30.15   Downloading filelock-3.16.1-py3-none-any.whl (16 kB)
32.09 Collecting numpy>=1.17
32.14   Downloading numpy-1.24.4-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.0 MB)
37.66 Collecting requests
37.71   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
38.30 Collecting huggingface-hub<1.0,>=0.10.0
38.36   Downloading huggingface_hub-0.36.2-py3-none-any.whl (566 kB)
39.12 Collecting packaging>=20.0
39.17   Downloading packaging-26.2-py3-none-any.whl (100 kB)
39.75 Collecting pyyaml>=5.1
39.81   Downloading PyYAML-6.0.3-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (795 kB)
40.28 Collecting tqdm>=4.27
40.33   Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
40.35 Requirement already satisfied: typing-extensions in /usr/local/lib/python3.8/dist-packages (from torch==1.13.1) (4.4.0)
41.07 Collecting charset_normalizer<4,>=2
41.12   Downloading charset_normalizer-3.4.7-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (192 kB)
41.69 Collecting idna<4,>=2.5
41.74   Downloading idna-3.15-py3-none-any.whl (72 kB)
42.37 Collecting certifi>=2017.4.17
42.42   Downloading certifi-2026.4.22-py3-none-any.whl (135 kB)
43.02 Collecting urllib3<3,>=1.21.1
43.07   Downloading urllib3-2.2.3-py3-none-any.whl (126 kB)
44.03 Collecting hf-xet<2.0.0,>=1.1.3; platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "arm64" or platform_machine == "aarch64"
44.08   Downloading hf_xet-1.5.0.tar.gz (837 kB)
44.36   Installing build dependencies: started
48.42   Installing build dependencies: finished with status 'done'
48.42   Getting requirements to build wheel: started
48.44   Getting requirements to build wheel: finished with status 'done'
48.44     Preparing wheel metadata: started
48.46     Preparing wheel metadata: finished with status 'error'
48.46     ERROR: Command errored out with exit status 1:
48.46      command: /usr/bin/python3 /tmp/tmpsnu5dae3 prepare_metadata_for_build_wheel /tmp/tmpkakie332
48.46          cwd: /tmp/pip-install-dgucymp2/hf-xet
48.46     Complete output (14 lines):
48.46     error: failed to parse manifest at `/tmp/pip-install-dgucymp2/hf-xet/hf_xet/Cargo.toml`
48.46     
48.46     Caused by:
48.46       feature `edition2024` is required
48.46     
48.46       The package requires the Cargo feature called `edition2024`, but that feature is not stabilized in this version of Cargo (1.75.0).
48.46       Consider adding `cargo-features = ["edition2024"]` to the top of Cargo.toml (above the [package] table) to tell Cargo you are opting in to use this unstable feature.
48.46       See https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024 for more information about the status of this feature.
48.46     💥 maturin failed
48.46       Caused by: Cargo metadata failed. Does your crate compile with `cargo build`?
48.46       Caused by: `cargo metadata` exited with an error:
48.46     Error running maturin: Command '['maturin', 'pep517', 'write-dist-info', '--metadata-directory', '/tmp/pip-modern-metadata-ysdoe5vv', '--interpreter', '/usr/bin/python3']' returned non-zero exit status 1.
48.46     Checking for Rust toolchain....
48.46     Running `maturin pep517 write-dist-info --metadata-directory /tmp/pip-modern-metadata-ysdoe5vv --interpreter /usr/bin/python3`
48.46     ----------------------------------------
48.54 ERROR: Command errored out with exit status 1: /usr/bin/python3 /tmp/tmpsnu5dae3 prepare_metadata_for_build_wheel /tmp/tmpkakie332 Check the logs for full command output.
------
[+] build 0/1
 ⠙ Image big-data-project-spark-job Building                               49.4s
Dockerfile:15

--------------------

  14 |     # Install ML dependencies - explicitly exclude problematic typing-extensions from torch index

  15 | >>> RUN pip install --no-cache-dir \

  16 | >>>     maturin && \

  17 | >>>     pip install --no-cache-dir \

  18 | >>>     'typing-extensions<4.5' && \

  19 | >>>     pip install --no-cache-dir \

  20 | >>>     'transformers==4.25.1' \

  21 | >>>     'torch==1.13.1'  --extra-index-url https://download.pytorch.org/whl/cpu

  22 |     

--------------------

failed to solve: process "/bin/sh -c pip install --no-cache-dir     maturin &&     pip install --no-cache-dir     'typing-extensions<4.5' &&     pip install --no-cache-dir     'transformers==4.25.1'     'torch==1.13.1'  --extra-index-url https://download.pytorch.org/whl/cpu" did not complete successfully: exit code: 1
