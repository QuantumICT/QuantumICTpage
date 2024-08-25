---
title: "Redesigning OpenKMC for Multi-Component Trillion-Atom Simulations on the New Sunway Supercomputer"
author: "Xu, Lei; Shang, Honghui; Chen, Xin; Zhang, Yunquan; Wang, Lifang; Gao, Xingyu; Song, Haifeng"
collection: publications
category: 2023
permalink: /publication/2023-07-01-Redesigning-OpenKMC-for-Multi-Component-Trillion-Atom-Simulations-on-the-New-Sunway-Supercomputer
date: 2023-07-01
paperurl: 'https://doi.org/10.1109/TPDS.2023.3269625'
---

The atomic kinetic Monte Carlo method plays an important role in material simulations by connecting the microscale mechanism with macroscale evolution. However, the long-time simulation of multi-component materials is highly challenging because it demands significant computing resources. With the advent of exascale computing, ultra-high computing power can enable kinetic Monte Carlo (KMC) simulations. In this paper, we deeply optimize OpenKMC for the new-generation Sunway supercomputer. This includes optimizing the memory access for the SW39000 architecture, eliminating various redundant computations at growing scales, and proposing a communication strategy for heterogeneous platforms. In addition, we expanded OpenKMC's simulation for multi-component alloys. Finally, the acceleration framework can produces a $37\times$37× performance enhancement on the Sunway platform. Furthermore, when powered by 10 million cores, our program can perform trillion-atom simulations of complex multi-component alloys with 85% parallel efficiency. © 1990-2012 IEEE.
