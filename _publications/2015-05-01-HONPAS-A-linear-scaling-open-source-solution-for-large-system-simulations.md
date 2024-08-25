---
title: "HONPAS: A linear scaling open-source solution for large system simulations"
author: "Qin, Xinming; Shang, Honghui; Xiang, Hongjun; Li, Zhenyu; Yang, Jinlong"
collection: publications
category: 2015
permalink: /publication/2015-05-01-HONPAS:-A-linear-scaling-open-source-solution-for-large-system-simulations
date: 2015-05-01
paperurl: 'https://doi.org/10.1002/qua.24837'
---

HONPAS is an ab initio electronic structure program for linear scaling or O(N) first-principles calculations of large and complex systems using standard norm-conserving pseudopotentials, numerical atomic orbitals (NAOs) basis sets, and periodic boundary conditions. HONPAS is developed in the framework of the SIESTA methodology and focuses on the development and implementation of efficient O(N) algorithms for ab initio electronic structure calculations. The Heyd-Scuseria-Ernzerhof (HSE) screened hybrid density functional has been implemented using a NAO2GTO scheme to evaluate the electron repulsion integrals (ERIs) with NAOs. ERI screening techniques allow the HSE functional calculations to be very efficient and scale linearly. The density matrix purification algorithms have been implemented, and the PSUTC2 and SUTC2 methods have been developed to deal with spin unrestricted systems with or without predetermined spin multiplicity, respectively. After the self-consistent field (SCF) process, additional O(N) post-SCF calculations for frontier molecular orbitals and maximally localized Wannier functions are also developed and implemented. Finally, an O(N) method based on the density matrix perturbation theory has been proposed and implemented to treat electric field in solids. This article provides an overall introduction to capabilities of HONPAS and implementation details of different O(N) algorithms. © 2014 Wiley Periodicals, Inc.
