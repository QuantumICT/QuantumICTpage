---
title: 'FHI-aims Million Atom Development Collaboration Log'
date: 2021-06-07
permalink: /posts/2021/FHI-aims-Million-Atom-Development-Collaboration-Log/
author: Wu Yangjun
excerpt: This document outlines the development conventions, environment setup, and precision requirements for the FHI-aims million atom project on Sunway TaihuLight.
tags:
  - FHI-aims
---


# Development Conventions

## Environment Platform

- **Supercomputing Platform**: Sunway TaihuLight  

- **Program Path**: `/home/export/online3/para030/wuyangjun/07_aims_million_dev/fhi-aims_MPE_O3_local-index`

  - Clone the repository to your directory

  ```shell
  git clone /home/export/online3/para030/wuyangjun/07_aims_million_dev/fhi-aims_MPE_O3_local-index
  ```

  - Use git pull and git push for synchronization, merging, and pushing changes
  - If git push fails, configure the following in the main repository

  ```shell
  git config --global receive.denyCurrentBranch updateInstead
  ```

- **Test Path**：`/home/export/online3/para030/wuyangjun/07_aims_million_dev/sw5_test`  
  
  - `H2_mini`：Hydrogen molecule  
  - `H2O`：Water molecule  
  - `RBDmini`：RBD protein  

## Compilation Environment

- **Must load the 710 compiler**：`module load sw/compiler/gcc710`

## Precision Requirements

FHI-aims currently has two versions of the program, a large memory version (global index) and a small memory version (local index). They can be switched in`control.in`：
- **local index**：Add the following configuration in control.in  

```shell
use_local_index .true.
load_balancing .true.
```

- **global index**：Comment out the following configuration in control.in

```shell
#use_local_index .true.
#load_balancing .true.
```

**The local index introduces precision errors. To ensure precision consistency, testing is done in two steps:**

- Step 1: First, develop and test under the **global index** to ensure **no precision loss**  
- Step 2: Then switch to **local index**testing. As long as the precision error (compared to the original global index) does not exceed the error between the **original program's** global index and local index.  
  - After development, there are four program versions: the original program's global index (gidx) and local index (lidx), and the optimized global index (gidx') and local index (lidx')  
  - Step 1 ensures gidx and gidx' are completely consistent  
  - Step 2 ensures the error between lidx' and gidx/gidx' does not exceed the error between lidx and gidx  
