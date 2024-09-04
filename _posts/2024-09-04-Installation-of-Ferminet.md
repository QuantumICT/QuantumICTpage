---
title: 'Installation of Ferminet'
date: 2024-09-04
permalink: /posts/2024/Installation-of-Ferminet/
author: Xia Zhuozhao
excerpt: 'This article records the installation process of Ferminet with CUDA support and the solutions to related issues.'
tags:
  - Ferminet
  - JAX
  - CUDA
---

## Clone the Ferminet Repository and Create a Conda Environment

```bash
git clone https://github.com/google-deepmind/ferminet.git
cd ferminet/
conda create --name ferminet python==3.11
conda activate ferminet
```

## Perform the Installation

```bash
pip install -e .
```

During the installation, some libraries will be automatically fetched from GitHub, but due to network issues, you might encounter the following error:

```text
  error: RPC failed; curl 28 Failed to connect to github.com port 443: Connection timed out
  fatal: the remote end hung up unexpectedly
  error: subprocess-exited-with-error

  × git clone --filter=blob:none --quiet https://github.com/microsoft/folx /tmp/pip-install-40pf8bo8/folx_c620f515ab454ac5af8a30de60e6a2b9 did not run successfully.
  │ exit code: 128
  ╰─> See above for output.
```

### Solution: Use a Proxy to Access GitHub

Modify the `setup.py` file by replacing GitHub links in the dependencies with mirror addresses (by adding `https://sciproxy.com/` before the links). For example:

```python
REQUIRED_PACKAGES = [
    'absl-py',
    'attrs',
    'chex',
    'h5py',
    'folx @ git+https://sciproxy.com/https://github.com/microsoft/folx',
    'jax',
    'jaxlib',
    # TODO(b/230487443) - use released version of kfac.
    'kfac_jax @ git+https://sciproxy.com/https://github.com/deepmind/kfac-jax',
    'ml-collections',
    'optax',
    'numpy',
    'pandas',
    'pyscf',
    'pyblock',
    'scipy',
    'typing_extensions',
]
```

### Install the Dependencies

```bash
pip install -e .
```

```text
Successfully installed PyYAML-6.0.2 absl-py-2.1.0 attrs-24.2.0 chex-0.1.86 cloudpickle-3.0.0 contextlib2-21.6.0 decorator-5.1.1 distrax-0.1.5 dm-tree-0.1.8 etils-1.9.4 ferminet-0.2 folx-0.2.12 gast-0.6.0 h5py-3.11.0 immutabledict-4.2.0 iniconfig-2.0.0 jax-0.4.31 jaxlib-0.4.31 jaxtyping-0.2.34 kfac_jax-0.0.6 ml-collections-0.1.1 ml-dtypes-0.4.0 numpy-2.1.1 opt-einsum-3.3.0 optax-0.2.3 packaging-24.1 pandas-2.2.2 parameterized-0.9.0 pluggy-1.5.0 pyblock-0.6 pyscf-2.6.2 pytest-8.3.2 python-dateutil-2.9.0.post0 pytz-2024.1 scipy-1.14.1 six-1.16.0 tensorflow-probability-0.24.0 toolz-0.12.1 typeguard-2.13.3 typing_extensions-4.12.2 tzdata-2024.1
```

### Test the Installation

```bash
ferminet --config ferminet/configs/atom.py --config.system.atom Li --config.batch_size 256 --config.pretrain.iterations 100
```

The installation was successful and the process started running on the CPU:

```text
 I0904 19:32:38.689715 140096347186368 xla_bridge.py:897] Unable to initialize backend 'cuda':（表示无法使用cuda）
I0904 19:32:38.689853 140096347186368 xla_bridge.py:897] Unable to initialize backend 'rocm': module 'jaxlib.xla_extension' has no attribute 'GpuAllocatorConfig'
I0904 19:32:38.690589 140096347186368 xla_bridge.py:897] Unable to initialize backend 'tpu': INTERNAL: Failed to open libtpu.so: libtpu.so: cannot open shared object file: No such file or directory
W0904 19:32:38.690742 140096347186368 xla_bridge.py:939] An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.
I0904 19:32:38.690810 140096347186368 train.py:384] Starting QMC with 1 XLA devices per host across 1 hosts.
converged SCF energy = -7.43242052759577  <S^2> = 0.75000054  2S+1 = 2.0000005
I0904 19:32:40.776647 140096347186368 train.py:584] No checkpoint found. Training new model.
I0904 19:32:44.342654 140096347186368 pretrain.py:344] Pretrain iter 00000: 0.0486982 0.933594
I0904 19:32:44.362198 140096347186368 pretrain.py:344] Pretrain iter 00001: 0.0303025 0.914062
I0904 19:32:44.377703 140096347186368 pretrain.py:344] Pretrain iter 00002: 0.0196005 0.898438
I0904 19:32:44.393930 140096347186368 pretrain.py:344] Pretrain iter 00003: 0.0143335 0.929688
I0904 19:32:44.410129 140096347186368 pretrain.py:344] Pretrain iter 00004: 0.0121834 0.933594
I0904 19:32:44.428070 140096347186368 pretrain.py:344] Pretrain iter 00005: 0.011141 0.9375
```

## Install CUDA Version of JAX and JAXLIB

JAX provides the API, while JAXLIB provides the concrete implementation of the API. To support CUDA, you need to install the corresponding CUDA-supported version of `jaxlib`.

```text
# Check the system's CUDA version
(ferminet) zhoupy@i-xzsn86y0:~/zhuozhao/ferminet$ pip list | grep jaxlib
jaxlib                 0.4.31

# Check the currently installed jaxlib version
(ferminet) zhoupy@i-xzsn86y0:/usr/local$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0
```

```bash
# Edit the command to find the appropriate jaxlib version
pip install --upgrade jax jaxlib==0.4.31+cuda120 -f https://storage.googleapis.com/jax-releases/jax_releases.html
```

You may encounter the following error:

```text
ERROR: Could not find a version that satisfies the requirement jaxlib==0.4.31+cuda120
ERROR: No matching distribution found for jaxlib==0.4.31+cuda120
```

### Manually Download and Install `jaxlib`

Go to [https://storage.googleapis.com/jax-releases/jax_releases.html](https://storage.googleapis.com/jax-releases/jax_releases.html) and find the `cuda12_plugin` (CUDA12 support) for `jax_cuda12_plugin-0.4.31` (jax version) and `cp311` (cpython3.11). The download link is:

`https://storage.googleapis.com/jax-releases/cuda12_plugin/jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl`

```bash
wget https://storage.googleapis.com/jax-releases/cuda12_plugin/jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
pip install jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
```

```text
(ferminet) zhoupy@i-xzsn86y0:~/zhuozhao/ferminet$ pip install jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
Looking in indexes: https://pypi.mirrors.ustc.edu.cn/simple
Processing ./jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
Collecting jax-cuda12-pjrt==0.4.31 (from jax-cuda12-plugin==0.4.31)
  Downloading https://mirrors.ustc.edu.cn/pypi/packages/f0/7e/f924606c12c1ef9ec34e64f8d2638f3244fee1753f0a96840c022e2b019c/jax_cuda12_pjrt-0.4.31-py3-none-manylinux2014_x86_64.whl (84.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.2/84.2 MB 36.3 MB/s eta 0:00:00
Installing collected packages: jax-cuda12-pjrt, jax-cuda12-plugin
Successfully installed jax-cuda12-pjrt-0.4.31 jax-cuda12-plugin-0.4.31
```

## Configure and Test CuDNN

When testing Ferminet again, you might encounter the following error:

```text
E0904 19:50:19.200583   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
jaxlib.xla_extension.XlaRuntimeError: FAILED_PRECONDITION: DNN library initialization failed.
I0904 19:50:19.024740 140572529931456 xla_bridge.py:897] Unable to initialize backend 'rocm': module 'jaxlib.xla_extension' has no attribute 'GpuAllocatorConfig'
I0904 19:50:19.025613 140572529931456 xla_bridge.py:897] Unable to initialize backend 'tpu': INTERNAL: Failed to open libtpu.so: libtpu.so: cannot open shared object file: No such file or directory
I0904 19:50:19.026619 140572529931456 train.py:384] Starting QMC with 2 XLA devices per host across 1 hosts.
E0904 19:50:19.200583   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
E0904 19:50:19.200674   74352 cuda_dnn.cc:539] Memory usage: 41776644096 bytes free, 42296475648 bytes total.
E0904 19:50:19.201102   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
E0904 19:50:19.201134   74352 cuda_dnn.cc:539] Memory usage: 41776644096 bytes free, 42296475648 bytes total.
jaxlib.xla_extension.XlaRuntimeError: FAILED_PRECONDITION: DNN library initialization failed. Look at the errors above for more details.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

This is most likely because CuDNN is not properly configured. It is recommended to use Conda to change the system's CuDNN configuration. In theory, everything except the NVIDIA driver can be configured by a non-root user.

Search for available CuDNN versions via Conda using `conda search cudnn --info`:

```text
cudnn 9.1.1.17 cuda12_0
-----------------------
file name   : cudnn-9.1.1.17-cuda12_0.conda
name        : cudnn
version     : 9.1.1.17
build       : cuda12_0
build number: 0
size        : 477.5 MB
license     : LicenseRef-Proprietary
subdir      : linux-64
url         : https://repo.anaconda.com/pkgs/main/linux-64/cudnn-9.1.1.17-cuda12_0.conda
md5         : a64c4e255e55eab4d50720fe93d18979
timestamp   : 2024-06-06 18:26:08 UTC
dependencies:
  - cuda-nvrtc
  - cuda-version 12.*
  - libcublas
```

Find the suitable CuDNN version for CUDA 12 (CuDNN by Conda 9.1.1.17) and install it:

```bash
conda install cudnn=9.1.1.17
```

### Test Again

```bash
ferminet --config ferminet/configs/atom.py --config.system.atom Li --config.batch_size 256 --config.pretrain.iterations 100
```

```text
I0904 20:01:20.533259 139623640442048 train.py:384] Starting QMC with 2 XLA devices per host across 1 hosts. (Indicates that GPU was successfully enabled)
```

## Summary

1. Conda is necessary because it has some features that virtual environments (`venv`) do not have, especially its package manager, which can install things that pip cannot.
2. Applications should preferably be installed without administrative privileges.

----------------------

## 克隆 Ferminet 仓库并创建 Conda 环境

```bash
git clone https://github.com/google-deepmind/ferminet.git
cd ferminet/
conda create --name ferminet python==3.11
conda activate ferminet
```
## 执行安装

```bash
pip install -e .
```


在安装过程中，会自动向github拉取某几个库，但因网络状况遇到如下错误：


```text
  error: RPC failed; curl 28 Failed to connect to github.com port 443: Connection timed out
  fatal: the remote end hung up unexpectedly
  error: subprocess-exited-with-error

  × git clone --filter=blob:none --quiet https://github.com/microsoft/folx /tmp/pip-install-40pf8bo8/folx_c620f515ab454ac5af8a30de60e6a2b9 did not run successfully.
  │ exit code: 128
  ╰─> See above for output.
```

解决方案：使用代理访问 GitHub。
修改 `setup.py` 文件，将依赖项中的 GitHub 链接替换为镜像地址（在链接前添加https://sciproxy.com/），示例如下：

```python
REQUIRED_PACKAGES = [
    'absl-py',
    'attrs',
    'chex',
    'h5py',
    'folx @ git+https://sciproxy.com/https://github.com/microsoft/folx',
    'jax',
    'jaxlib',
    # TODO(b/230487443) - use released version of kfac.
    'kfac_jax @ git+https://sciproxy.com/https://github.com/deepmind/kfac-jax',
    'ml-collections',
    'optax',
    'numpy',
    'pandas',
    'pyscf',
    'pyblock',
    'scipy',
    'typing_extensions',
]
```

安装：


```bash
pip install -e .
```
```text
Successfully installed PyYAML-6.0.2 absl-py-2.1.0 attrs-24.2.0 chex-0.1.86 cloudpickle-3.0.0 contextlib2-21.6.0 decorator-5.1.1 distrax-0.1.5 dm-tree-0.1.8 etils-1.9.4 ferminet-0.2 folx-0.2.12 gast-0.6.0 h5py-3.11.0 immutabledict-4.2.0 iniconfig-2.0.0 jax-0.4.31 jaxlib-0.4.31 jaxtyping-0.2.34 kfac_jax-0.0.6 ml-collections-0.1.1 ml-dtypes-0.4.0 numpy-2.1.1 opt-einsum-3.3.0 optax-0.2.3 packaging-24.1 pandas-2.2.2 parameterized-0.9.0 pluggy-1.5.0 pyblock-0.6 pyscf-2.6.2 pytest-8.3.2 python-dateutil-2.9.0.post0 pytz-2024.1 scipy-1.14.1 six-1.16.0 tensorflow-probability-0.24.0 toolz-0.12.1 typeguard-2.13.3 typing_extensions-4.12.2 tzdata-2024.1
```
测试安装：

```bash
ferminet --config ferminet/configs/atom.py --config.system.atom Li --config.batch_size 256 --config.pretrain.iterations 100
```

发现已经成功使用CPU开始运行：

```text
 I0904 19:32:38.689715 140096347186368 xla_bridge.py:897] Unable to initialize backend 'cuda':（表示无法使用cuda）
I0904 19:32:38.689853 140096347186368 xla_bridge.py:897] Unable to initialize backend 'rocm': module 'jaxlib.xla_extension' has no attribute 'GpuAllocatorConfig'
I0904 19:32:38.690589 140096347186368 xla_bridge.py:897] Unable to initialize backend 'tpu': INTERNAL: Failed to open libtpu.so: libtpu.so: cannot open shared object file: No such file or directory
W0904 19:32:38.690742 140096347186368 xla_bridge.py:939] An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.
I0904 19:32:38.690810 140096347186368 train.py:384] Starting QMC with 1 XLA devices per host across 1 hosts.
converged SCF energy = -7.43242052759577  <S^2> = 0.75000054  2S+1 = 2.0000005
I0904 19:32:40.776647 140096347186368 train.py:584] No checkpoint found. Training new model.
I0904 19:32:44.342654 140096347186368 pretrain.py:344] Pretrain iter 00000: 0.0486982 0.933594
I0904 19:32:44.362198 140096347186368 pretrain.py:344] Pretrain iter 00001: 0.0303025 0.914062
I0904 19:32:44.377703 140096347186368 pretrain.py:344] Pretrain iter 00002: 0.0196005 0.898438
I0904 19:32:44.393930 140096347186368 pretrain.py:344] Pretrain iter 00003: 0.0143335 0.929688
I0904 19:32:44.410129 140096347186368 pretrain.py:344] Pretrain iter 00004: 0.0121834 0.933594
I0904 19:32:44.428070 140096347186368 pretrain.py:344] Pretrain iter 00005: 0.011141 0.9375
```


## 安装 CUDA 版本的 JAX 和 JAXLIB 
jax提供了一套API，jaxlib提供了API的具体实现。为了支持 CUDA，需要安装对应版本的支持CUDA的 `jaxlib`。
```text
# 查看系统的CUDA版本
(ferminet) zhoupy@i-xzsn86y0:~/zhuozhao/ferminet$ pip list | grep jaxlib
jaxlib                 0.4.31

# 查看目前安装的jaxlib版本
(ferminet) zhoupy@i-xzsn86y0:/usr/local$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0
```

```bash
# 编辑命令，找到合适的jaxlib版本
pip install --upgrade jax jaxlib==0.4.31+cuda120 -f https://storage.googleapis.com/jax-releases/jax_releases.html
```

出现如下错误：


```text
ERROR: Could not find a version that satisfies the requirement jaxlib==0.4.31+cuda120
ERROR: No matching distribution found for jaxlib==0.4.31+cuda120
```
需要手动下载并安装 `jaxlib`：

去https://storage.googleapis.com/jax-releases/jax_releases.html，找到
`cuda12_plugin（CUDA12支持）/jax_cuda12_plugin-0.4.31（jax版本）-cp311（cpython3.11）-cp311-manylinux2014_x86_64.whl`  
地址为：`https://storage.googleapis.com/jax-releases/cuda12_plugin/jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl

```bash
wget https://storage.googleapis.com/jax-releases/cuda12_plugin/jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
pip install jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
```
```text
(ferminet) zhoupy@i-xzsn86y0:~/zhuozhao/ferminet$ pip install jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
Looking in indexes: https://pypi.mirrors.ustc.edu.cn/simple
Processing ./jax_cuda12_plugin-0.4.31-cp311-cp311-manylinux2014_x86_64.whl
Collecting jax-cuda12-pjrt==0.4.31 (from jax-cuda12-plugin==0.4.31)
  Downloading https://mirrors.ustc.edu.cn/pypi/packages/f0/7e/f924606c12c1ef9ec34e64f8d2638f3244fee1753f0a96840c022e2b019c/jax_cuda12_pjrt-0.4.31-py3-none-manylinux2014_x86_64.whl (84.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.2/84.2 MB 36.3 MB/s eta 0:00:00
Installing collected packages: jax-cuda12-pjrt, jax-cuda12-plugin
Successfully installed jax-cuda12-pjrt-0.4.31 jax-cuda12-plugin-0.4.31
```


## 配置和测试 CuDNN 

再次测试ferminet，出现以下错误：

```text
E0904 19:50:19.200583   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
jaxlib.xla_extension.XlaRuntimeError: FAILED_PRECONDITION: DNN library initialization failed.
I0904 19:50:19.024740 140572529931456 xla_bridge.py:897] Unable to initialize backend 'rocm': module 'jaxlib.xla_extension' has no attribute 'GpuAllocatorConfig'
I0904 19:50:19.025613 140572529931456 xla_bridge.py:897] Unable to initialize backend 'tpu': INTERNAL: Failed to open libtpu.so: libtpu.so: cannot open shared object file: No such file or directory
I0904 19:50:19.026619 140572529931456 train.py:384] Starting QMC with 2 XLA devices per host across 1 hosts.
E0904 19:50:19.200583   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
E0904 19:50:19.200674   74352 cuda_dnn.cc:539] Memory usage: 41776644096 bytes free, 42296475648 bytes total.
E0904 19:50:19.201102   74352 cuda_dnn.cc:535] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
E0904 19:50:19.201134   74352 cuda_dnn.cc:539] Memory usage: 41776644096 bytes free, 42296475648 bytes total.
jaxlib.xla_extension.XlaRuntimeError: FAILED_PRECONDITION: DNN library initialization failed. Look at the errors above for more details.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

多半是cudnn没配置好。此处推荐使用conda更改系统的cudnn配置，理论上除了nvidia驱动以外的东西都能在非root用户配置。
使用 `conda search cudnn --info`搜索可用的cudnn by conda版本：
```text
cudnn 9.1.1.17 cuda12_0
-----------------------
file name   : cudnn-9.1.1.17-cuda12_0.conda
name        : cudnn
version     : 9.1.1.17
build       : cuda12_0
build number: 0
size        : 477.5 MB
license     : LicenseRef-Proprietary
subdir      : linux-64
url         : https://repo.anaconda.com/pkgs/main/linux-64/cudnn-9.1.1.17-cuda12_0.conda
md5         : a64c4e255e55eab4d50720fe93d18979
timestamp   : 2024-06-06 18:26:08 UTC
dependencies:
  - cuda-nvrtc
  - cuda-version 12.*
  - libcublas
```
找到适合cuda12的cudnn by conda 9.1.1.17，安装之
```bash
conda install cudnn=9.1.1.17
```

再次测试，安装成功。
```bash
ferminet --config ferminet/configs/atom.py --config.system.atom Li --config.batch_size 256 --config.pretrain.iterations 100
```
```text
I0904 20:01:20.533259 139623640442048 train.py:384] Starting QMC with 2 XLA devices per host across 1 hosts.（说明GPU启用成功）
```

## 总结
1. conda是有必要的，它拥有一些venv没拥有的特性，特别是它的包管理器可以安装很多pip做不到的东西
2. 应尽量使用非管理权限安装应用

