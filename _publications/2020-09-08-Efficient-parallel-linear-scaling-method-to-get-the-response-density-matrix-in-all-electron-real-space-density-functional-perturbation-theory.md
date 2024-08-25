---
title: "Efficient parallel linear scaling method to get the response density matrix in all-electron real-space density-functional perturbation theory"
author: "Shang, Honghui; Liang, Wanzhen; Zhang, Yunquan; Yang, Jinlong"
collection: publications
category: 2020
permalink: /publication/2020-09-08-Efficient-parallel-linear-scaling-method-to-get-the-response-density-matrix-in-all-electron-real-space-density-functional-perturbation-theory
date: 2020-09-08
paperurl: 'https://doi.org/'
---

The real-space density-functional perturbation theory (DFPT) for the computations of the response properties with respect to the atomic displacement and homogeneous electric field perturbation has been recently developed and implemented into the all-electron, numeric atom-centered orbitals electronic structure package FHI-aims. It is found that the bottleneck for large scale applications is the computation of the response density matrix, which scales as O(N3). Here for the response properties with respect to the homogeneous electric field, we present an efficient parallel linear scaling algorithm for the response density matrix calculation. Our scheme is based on the second-order trace-correcting purification and the parallel sparse matrix-matrix multiplication algorithms. The new scheme reduces the formal scaling from O(N3) to O(N), and shows good parallel scalability over tens of thousands of cores. As demonstrated by extensive validation, we achieve a rapid computation of accurate polarizabilities using DFPT. Finally, the computational efficiency of this scheme has been illustrated by making the scaling tests and scalability tests on massively parallel computer systems. Copyright © 2020, The Authors. All rights reserved.
