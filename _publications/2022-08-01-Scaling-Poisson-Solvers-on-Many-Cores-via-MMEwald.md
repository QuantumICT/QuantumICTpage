---
title: "Scaling Poisson Solvers on Many Cores via MMEwald"
author: "Wu, Mingchuan; Wu, Yangjun; Shang, Honghui; Liu, Ying; Cui, Huimin; Li, Fang; Duan, Xiaohui; Zhang, Yunquan; Feng, Xiaobing"
collection: publications
category: 2022
permalink: /publication/2022-08-01-Scaling-Poisson-Solvers-on-Many-Cores-via-MMEwald
date: 2022-08-01
paperurl: 'https://doi.org/10.1109/TPDS.2021.3127138'
---

The Poisson solver for the calculation of the electrostatic potential is an essential primitive in quantum mechanics calculations. In this article, we adopt the Ewald method and propose a highly-optimized and scalable framework for Poisson solver, MMEwald, on the new generation Sunway supercomputer, capable of utilizing the collection of 390-core accelerators it uses. The MMEwald is based on a grid adapted cut-plane approach to partition the points into batches and distribute the batch to the processors. Furthermore, we propose a set of architecture-specific optimizations to efficiently utilize the memory bandwidth and computation capacity of the supercomputer. Experimental results demonstrate the efficiency of the MMEwald in providing strong and weak scaling performance. © 1990-2012 IEEE.
