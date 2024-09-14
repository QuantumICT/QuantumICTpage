---
title: "Efficient parallel linear scaling method to get the response density matrix in all-electron real-space density-functional perturbation theory"
author: "Honghui Shang; WanZhen Liang; Yunquan Zhang; Jinlong Yang"
collection: publications
category: 2021
permalink: /publication/2021-01-01-Efficient-parallel-linear-scaling-metho
date: 2021-01-01
paperurl: 'https://doi.org/https://doi.org/10.1016/j.cpc.2020.107613'
journal: 'Computer Physics Communications'
---
```bibtex
@article{Shang2021_CPC_ntpoly,
 abstract = {The real-space density-functional perturbation theory (DFPT) for the computations of the response properties with respect to the atomic displacement and homogeneous electric field perturbation has been recently developed and implemented into the all-electron, numeric atom-centered orbitals electronic structure package FHI-aims. It is found that the bottleneck for large scale applications is the computation of the response density matrix, which scales as O(N3). Here for the response properties with respect to the homogeneous electric field, we present an efficient parallel linear scaling algorithm for the response density matrix calculation. Our scheme is based on the second-order trace-correcting purification and the parallel sparse matrix–matrix multiplication algorithms. The new scheme reduces the formal scaling from O(N3) to O(N), and shows good parallel scalability over tens of thousands of cores. As demonstrated by extensive validation, we achieve a rapid computation of accurate polarizabilities using DFPT. Finally, the computational efficiency of this scheme has been illustrated by making the scaling tests and scalability tests on massively parallel computer systems.},
 author = {Honghui Shang and WanZhen Liang and Yunquan Zhang and Jinlong Yang},
 doi = {https://doi.org/10.1016/j.cpc.2020.107613},
 issn = {0010-4655},
 journal = {Computer Physics Communications},
 keywords = {Density-functional perturbation theory, Linear scaling, MPI, Numeric atomic orbitals, Density-function theory},
 pages = {107613},
 title = {Efficient parallel linear scaling method to get the response density matrix in all-electron real-space density-functional perturbation theory},
 url = {https://www.sciencedirect.com/science/article/pii/S0010465520302940},
 volume = {258},
 year = {2021}
}
```
