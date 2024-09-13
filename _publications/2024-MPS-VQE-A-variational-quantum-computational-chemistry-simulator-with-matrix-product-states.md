---
title: "MPS-VQE: A variational quantum computational chemistry simulator with matrix product states"
author: "Zhiqian Xu; Yi Fan; Chu Guo; Honghui Shang"
collection: publications
category: 2024
permalink: /publication/2024-MPS-VQE-A-variational-quantum-computational-chemistry-simulator-with-matrix-product-states
date: 2024
paperurl: 'https://doi.org/https://doi.org/10.1016/j.cpc.2023.108897'
journal: 'Computer Physics Communications'
---
```bibtex
@article{Xuzhiqian_CPC_2023,
 abstract = {Quantum computing is attracting more and more attention in material and biological science. In the noisy intermediate-scale quantum (NISQ) computing era, the variational quantum eigensolver (VQE) is expected as an effective method to solve quantum chemistry problems which has potential quantum advantage. Classically simulating quantum algorithms plays a critical role in algorithmic development and the validation of noisy quantum devices before large-scale, fully fault-tolerant quantum computers are developed. However, most existing simulators are based on the state vector or density matrix representation of the quantum state which is faced with the memory bottleneck due to the exponential growth of memory requirement as the number of qubits increases. In this work, we present a VQE simulator based on the matrix product states (MPS) method from quantum many-body physics, and a detailed study of our MPS-VQE simulator in quantum chemistry applications. The memory requirement of MPS-VQE grows only polynomially and we demonstrate that accurate results can be obtained despite the truncation of the smallest singular values during the algorithm. A distributed parallelization scheme is also presented for massively parallel computer systems, and different implementations of the parallelization scheme based on the Julia language are benchmarked which demonstrate the efficiency and scalability of our method. Our method could open a new avenue towards large-scale classical simulation of quantum computational chemistry.},
 author = {Zhiqian Xu and Yi Fan and Chu Guo and Honghui Shang},
 doi = {https://doi.org/10.1016/j.cpc.2023.108897},
 issn = {0010-4655},
 journal = {Computer Physics Communications},
 keywords = {Quantum computing, Variational quantum eigensolver, Matrix product state, Quantum chemistry, Parallel scalability},
 pages = {108897},
 title = {MPS-VQE: A variational quantum computational chemistry simulator with matrix product states},
 url = {https://www.sciencedirect.com/science/article/pii/S0010465523002424},
 volume = {294},
 year = {2024}
}
```
