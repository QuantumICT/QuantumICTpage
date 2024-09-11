---
title: "Scalable and Differentiable Simulator for Quantum Computational Chemistry"
author: "Xu, Zhiqian; Shang, Honghui; Fan, Yi; Zeng, Xiongzhi; Zhang, Yunquan; Guo, Chu"
collection: publications
category: 2024
permalink: /publication/2024-07-16-Scalable-and-Differentiable-Simulator-for-Quantum-Computational-Chemistry
date: 2024-07-16
paperurl: 'https://doi.org/10.1109/IPDPS57955.2024.00028'
published: 'Journal of XXX'
---

We develop a high-performance simulator for variational quantum eigensolver (VQE), the major innovations include: (1) A differentiable matrix product state (MPS) based VQE simulator that seamlessly integrates MPS into the automatic differentiation framework, which overcomes the exponential memory growth of state-vector simulator and can efficiently calculate gradients with a cost independent of the number of parameters; (2) A dynamic scheme to distribute the gradient calculations to achieve good load balance; (3) A parallel adaptive VQE which integrates our differentiable MPS simulator to further enhance the simulation performance; (4) Study of real chemical systems with convergence to chemical accuracy using our simulator, achieving nearly linearly strong and weak scaling for chemical systems with up to 100 qubits. Our simulator provides an ideal test ground for VQE and paves the way of benchmarking large-scale VQE experiments on near-term quantum computers. © 2024 IEEE.
