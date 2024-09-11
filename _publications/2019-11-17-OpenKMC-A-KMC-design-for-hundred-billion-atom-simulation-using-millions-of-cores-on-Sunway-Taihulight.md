---
title: "OpenKMC: A KMC design for hundred-billion-atom simulation using millions of cores on Sunway Taihulight"
author: "Li, Kun; Shang, Honghui; Zhang, Yunquan; Li, Shigang; Wu, Baodong; Wang, Dong; Zhang, Libo; Li, Fang; Chen, Dexun; Wei, Zhiqiang"
collection: publications
category: 2019
permalink: /publication/2019-11-17-OpenKMC:-A-KMC-design-for-hundred-billion-atom-simulation-using-millions-of-cores-on-Sunway-Taihulight
date: 2019-11-17
paperurl: 'https://doi.org/10.1145/3295500.3356165'
journal: 'International Conference for High Performance Computing, Networking, Storage and Analysis, SC'
---

With more attention attached to nuclear energy, the formation mechanism of the solute clusters precipitation within complex alloys becomes intriguing research in the embrittlement of nuclear reactor pressure vessel (RPV) steels. Such phenomenon can be simulated with atomic kinetic Monte Carlo (AKMC) software, which evaluates the interactions of solute atoms with point defects in metal alloys. In this paper, we propose OpenKMC to accelerate large-scale KMC simulations on Sunway many-core architecture. To overcome the constraints caused by complex many-core architecture, we employ six levels of optimization in OpenKMC: (1) a new efficient potential computation model; (2) a group reaction strategy for fast event selection; (3) a software cache strategy; (4) combined communication optimizations; (5) a Transcription-Translation-Transmission algorithm for many-core optimization; (6) vectorization acceleration. Experiments illustrate that our OpenKMC has high accuracy and good scalability of applying hundred-billion-atom simulation over 5.2 million cores with a performance of over 80.1% parallel efficiency. © 2019 ACM.
