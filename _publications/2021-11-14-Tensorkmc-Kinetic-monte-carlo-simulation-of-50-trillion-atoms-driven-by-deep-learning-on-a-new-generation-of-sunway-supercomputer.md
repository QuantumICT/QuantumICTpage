---
title: "Tensorkmc: Kinetic monte carlo simulation of 50 trillion atoms driven by deep learning on a new generation of sunway supercomputer"
author: "Shang, Honghui; Chen, Xin; Gao, Xingyu; Lin, Rongfen; Wang, Lifang; Li, Fang; Xiao, Qian; Xu, Lei; Sun, Qiang; Zhu, Leilei; Wang, Fei; Zhang, Yunquan; Song, Haifeng"
collection: publications
category: 2021
permalink: /publication/2021-11-14-Tensorkmc:-Kinetic-monte-carlo-simulation-of-50-trillion-atoms-driven-by-deep-learning-on-a-new-generation-of-sunway-supercomputer
date: 2021-11-14
paperurl: 'https://doi.org/10.1145/3458817.3476174'
---

The atomic kinetic Monte Carlo method plays an important role in multi-scale physical simulations because it bridges the micro and macro worlds. However, its accuracy is limited by empirical potentials.We therefore propose herein a triple-encoding algorithm and vacancy-cache mechanism to efficiently integrate ab initio neural network potentials (NNPs) with AKMC and implement them in our TensorKMC codes. We port our program to SW26010-pro and innovate a fast feature operator and a big fusion operator for the NNPs for fully utilizing the powerful heterogeneous computing units of the new-generation Sunway supercomputer. We further optimize memory usage. With these improvements, TensorKMC can simulate up to 54 trillions of atoms and achieve excellent strong and weak scaling performance up to 27,456,000 cores. © 2021 IEEE Computer Society. All rights reserved.
