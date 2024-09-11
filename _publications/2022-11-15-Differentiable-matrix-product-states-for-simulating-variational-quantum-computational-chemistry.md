---
title: "Differentiable matrix product states for simulating variational quantum computational chemistry"
author: "Guo, Chu; Fan, Yi; Xu, Zhiqian; Shang, Honghui"
collection: publications
category: 2022
permalink: /publication/2022-11-15-Differentiable-matrix-product-states-for-simulating-variational-quantum-computational-chemistry
date: 2022-11-15
paperurl: 'https://doi.org/10.48550/arXiv.2211.07983'
journal: 'arXiv'
---

Quantum Computing is believed to be the ultimate solution for quantum chemistry problems. Before the advent of large-scale, fully fault-tolerant quantum computers, the variational quantum eigensolver (VQE) is a promising heuristic quantum algorithm to solve real world quantum chemistry problems on near-term noisy quantum computers. Here we propose a highly parallelizable classical simulator for VQE based on the matrix product state representation of quantum state, which significantly extend the simulation range of the existing simulators. Our simulator seamlessly integrates the quantum circuit evolution into the classical auto-differentiation framework, thus the gradients could be computed efficiently similar to the classical deep neural network, with a scaling that is independent of the number of variational parameters. As applications, we use our simulator to study commonly used small molecules such as HF, HCl, LiH and H2O, as well as larger molecules CO2, BeH2 and H4 with up to 40 qubits. The favorable scaling of our simulator against the number of qubits and the number of parameters could make it an ideal testing ground for near-term quantum algorithms and a perfect benchmarking baseline for oncoming large scale VQE experiments on noisy quantum computers. © 2022, CC BY.
