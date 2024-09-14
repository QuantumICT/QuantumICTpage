---
title: "Efficient implementation of analytical gradients for periodic hybrid functional calculations within fitted numerical atomic orbitals from NAO2GTO"
author: "Xinming Qin; Honghui Shang; Jinlong Yang"
collection: publications
category: 2023
permalink: /publication/2023-01-01-Efficient-implementation-of-analytical-
date: 2023-01-01
paperurl: 'https://doi.org/10.3389/fchem.2023.1232425'
journal: 'Frontiers in Chemistry'
---
```bibtex
@article{Qin2023,
 abstract = {The NAO2GTO scheme provides an efficient way to evaluate the electron repulsion integrals (ERIs) over numerical atomic orbitals (NAOs) with auxiliary Gaussian-type orbitals (GTOs). However, the NAO2GTO fitting will significantly impact the accuracy and convergence of hybrid functional calculations. To address this issue, here we propose to use the fitted orbitals as a new numerical basis to properly handle the mismatch between NAOs and fitted GTOs. We present an efficient and linear-scaling implementation of analytical gradients of Hartree-Fock exchange (HFX) energy for periodic HSE06 calculations with fitted NAOs in the HONPAS package. In our implementation, the ERIs and their derivatives for HFX matrix and forces are evaluated analytically with the auxiliary GTOs, while other terms are calculated using numerically discretized GTOs. Several integral screening techniques are employed to reduce the number of required ERI derivatives. We benchmark the accuracy and efficiency of our implementation and demonstrate that our results of lattice constants, bulk moduli, and band gaps of several typical semiconductors are in good agreement with the experimental values. We also show that the calculation of HFX forces based on a master-worker dynamic parallel scheme has a very high efficiency and scales linearly with respect to system size. Finally, we study the geometry optimization and polaron formation due to an excess electron in rutile TiO 2 by means of HSE06 calculations to further validate the applicability of our implementation.},
 author = {Qin, Xinming and Shang, Honghui and Yang, Jinlong},
 doi = {10.3389/fchem.2023.1232425},
 issn = {2296-2646},
 journal = {Frontiers in Chemistry},
 keywords = {Hartree-Fock exchange,NAO2GTO,atomic forces,electron repulsion integral derivatives,fi tted orbitals,fitted orbitals,hartree-fock exchange,integral screening,linear scaling,nao2gto},
 month = {jul},
 number = {July},
 pages = {1--14},
 title = {Efficient implementation of analytical gradients for periodic hybrid functional calculations within fitted numerical atomic orbitals from NAO2GTO},
 url = {https://www.frontiersin.org/articles/10.3389/fchem.2023.1232425/full},
 volume = {11},
 year = {2023}
}
```
