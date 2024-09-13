---
title: "The static parallel distribution algorithms for hybrid density-functional calculations in HONPAS package"
author: "Qin, Xinming; Shang, Honghui; Xu, Lei; Hu, Wei; Yang, Jinlong; Li, Shigang; Zhang, Yunquan"
collection: publications
category: 2020
permalink: /publication/2020-01-01-The-static-parallel-distribution-algorithms-for-hybrid-density-functional-calculations-in-HONPAS-package
date: 2020-01-01
paperurl: 'https://doi.org/10.1177/1094342019845046'
journal: 'International Journal of High Performance Computing Applications'
---
@article{Qin2020_HONPAS,
 abstract = {Hybrid density-functional calculation is one of the most commonly adopted electronic structure theories in computational chemistry and materials science because of its balance between accuracy and computational cost. Recently, we have developed a novel scheme called NAO2GTO to achieve linear scaling (Order-N) calculations for hybrid density-functionals. In our scheme, the most time-consuming step is the calculation of the electron repulsion integrals (ERIs) part, so creating an even distribution of these ERIs in parallel implementation is an issue of particular importance. Here, we present two static scalable distributed algorithms for the ERIs computation. Firstly, the ERIs are distributed over ERIs shell pairs. Secondly, the ERIs are distributed over ERIs shell quartets. In both algorithms, the calculation of ERIs is independent of each other, so the communication time is minimized. We show our speedup results to demonstrate the performance of these static parallel distributed algorithms in the Hefei Order-N packages for ab initio simulations.},
 author = {Qin, Xinming and Shang, Honghui and Xu, Lei and Hu, Wei and Yang, Jinlong and Li, Shigang and Zhang, Yunquan},
 doi = {10.1177/1094342019845046},
 file = {:C$\backslash$:/Users/shanghui/work/shanghui_latex/my_publication/2020_Qin_Shang_IJHPCA.pdf:pdf},
 issn = {17412846},
 journal = {International Journal of High Performance Computing Applications},
 keywords = {Distributed algorithms,HONPAS package,electron repulsion integrals,hybrid density-functional calculations,parallel implementation},
 month = {mar},
 number = {2},
 pages = {159--168},
 title = {The static parallel distribution algorithms for hybrid density-functional calculations in HONPAS package},
 url = {http://journals.sagepub.com/doi/10.1177/1094342019845046},
 volume = {34},
 year = {2020}
}
