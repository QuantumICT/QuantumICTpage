---
title: 'Optimizing Memory Usage in Fortran Code'
date: 2021-06-08
permalink: /posts/2021/optimizing-memory-usage/
author: DownFly
excerpt: 'This post discusses the changes made to reduce memory usage in the Fortran subroutine get_n_compute_maxes_p1.f90, including the removal and dynamic allocation of certain arrays.'
tags:
  - Fortran
  - Memory Optimization
---

# Reducing Memory Usage in get_n_compute_maxes_p1.f90

## Memory Usage Changes
- `dist_tab (n_centers_integrals, n_max_batch_size)`
  - Removed
- `dir_tab (3, n_centers_integrals, n_max_batch_size)`
  - Removed
- `dist_tab_sq (n_centers_integrals, n_max_batch_size)`
  - Reduced dimensions to `dist_tab_sq(n_centers_integrals)`
  - Changed to allocate memory dynamically

## Precision Comparison  

||gidx - gidx'|gidx - lidx|gidx - lidx'|
|:----|:----:|:----:|:----:| 
|H2|0|1.33E-14|1.07E-14|
|H2O| 0|2.345E-12|1.927E-12|
|RBDmini| Running| Running| Running|