---
title: 'Block2 Installation'
date: 2022-01-14
permalink: /posts/2022/block2-Installation/
author: DownFly
# posts: true
tags:
  - block2
---

## Preparation
Download block2
```bash
git clone https://github.com/block-hczhai/block2-preview
```
Install pybind11
```
pip bybind11
```
Load CMake 3.7
```
module add cmake/3.7.0
```
Load gcc 8.3
```
module add gcc/8.3.0-wzm
```
## Installation
You can configure CMake parameters in the cmake_args variable in <block2_path>/setup.py. Specific parameters can be found in the README.md. I added a parameter to enable MPI.

Run the command to compile and create the whl package
```
python3 setup.py bdist_wheel
```
The created whl package is by default located in the <block2_path>/dist folder. Use pip to install the whl package
```
pip install block2-0.1.10-cp37-cp37m-linux_x86_64.whl
```
Dependencies will be checked and downloaded automatically during installation.