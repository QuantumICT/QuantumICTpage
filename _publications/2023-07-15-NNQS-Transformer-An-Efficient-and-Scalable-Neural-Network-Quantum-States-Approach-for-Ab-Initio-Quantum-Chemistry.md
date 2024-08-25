---
title: "NNQS-Transformer: An Efficient and Scalable Neural Network Quantum States Approach for Ab Initio Quantum Chemistry"
author: "Wu, Yangjun; Guo, Chu; Fan, Yi; Zhou, Pengyu; Shang, Honghui"
collection: publications
category: 2023
permalink: /publication/2023-07-15-NNQS-Transformer:-An-Efficient-and-Scalable-Neural-Network-Quantum-States-Approach-for-Ab-Initio-Quantum-Chemistry
date: 2023-07-15
paperurl: 'https://doi.org/10.1145/3581784.3607061'
---

Neural network quantum state (NNQS) has emerged as a promising candidate for quantum many-body problems, but its practical applications are often hindered by the high cost of sampling and local energy calculation. We develop a high-performance NNQS method for ab initio electronic structure calculations. The major innovations include: (1) A transformer based architecture as the quantum wave function ansatz; (2) A data-centric parallelization scheme for the variational Monte Carlo (VMC) algorithm which preserves data locality and well adapts for different computing architectures; (3) A parallel batch sampling strategy which reduces the sampling cost and achieves good load balance; (4) A parallel local energy evaluation scheme which is both memory and computationally efficient; (5) Study of real chemical systems demonstrates both the superior accuracy of our method compared to state-of-the-art and the strong and weak scalability for large molecular systems with up to 120 spin orbitals. © 2023 ACM.
