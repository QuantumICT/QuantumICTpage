---
title: "The dynamic parallel distribution algorithm for hybrid density-functional calculations in HONPAS package"
author: "Shang, Honghui; Xu, Lei; Wu, Baodong; Qin, Xinming; Zhang, Yunquan; Yang, Jinlong"
collection: publications
category: 2020
permalink: /publication/2020-09-08-The-dynamic-parallel-distribution-algorithm-for-hybrid-density-functional-calculations-in-HONPAS-package
date: 2020-09-08
paperurl: 'https://doi.org/'
---

This work presents a dynamic parallel distribution scheme for the Hartree-Fock exchange (HFX) calculations based on the real-space NAO2GTO framework. The most time-consuming electron repulsion integrals (ERIs) calculation is perfectly load-balanced with 2-level master-worker dynamic parallel scheme, the density matrix and the HFX matrix are both stored in the sparse format, the network communication time is minimized via only communicating the index of the batched ERIs and the final sparse matrix form of the HFX matrix. The performance of this dynamic scalable distributed algorithm has been demonstrated by several examples of large scale hybrid density-functional calculations on Tianhe-2 supercomputers, including both molecular and solid states systems with multiple dimensions, and illustrates good scalability. Copyright © 2020, The Authors. All rights reserved.
