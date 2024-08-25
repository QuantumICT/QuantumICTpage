---
title: 'Reducing Memory Usage of dist_tab, dir_tab, and dist_tab_sq'
date: 2021-06-07
permalink: /posts/2021/reducing-memory-usage/
author: DownFly
excerpt: 'This post explains how to reduce memory usage by optimizing the arrays dist_tab, dir_tab, and dist_tab_sq in Fortran code, including merging loops to compute and use each row immediately.'
tags:
  - Fortran
  - Memory Optimization
---

# Reduce Memory Usage of dist_tab, dir_tab, and dist_tab_sq

### Original Code (in C language)

Location: src/DFPT_dielectric/integrate_first_order_rho_dielectric.f90 and src/DFPT_dielectric/integrate_first_order_H_dielectric.f90

```c
double dist_tab_sq[n_max_batch_size][n_centers_integrals];
double dist_tab[n_max_batch_size][n_centers_integrals];
double dir_tab[n_max_batch_size][n_centers_integrals][3];

for(int i_index=0; i_index<batch_size; i_index++)
{
    // Each loop calculates one row of dist_tab_sq and dir_tab
    tab_atom_centered_coords_p0(dist_tab_sq[i_index], dir_tab[i_index]);
}
for(int i_index=0; i_index<batch_size; i_index++)
{
    // Each loop uses one row of dist_tab_sq, dir_tab, and dist_tab
    functions(dist_tab_sq[i_index], dist_tab[i_index], dir_tab[i_index]);
}

### Modified Code

It can be seen that these three arrays are calculated row by row and used row by row, and there is no connection between each row. Therefore, the loops can be merged, calculating and using one row at a time without having to calculate all rows.

```c
double dist_tab_sq[n_centers_integrals];
double dist_tab[n_centers_integrals];
double dir_tab[n_centers_integrals][3];

for(int i_index=0;i_index<batch_size;i_index++)
{
    tab_atom_centered_coords_p0(dist_tab_sq,dir_tab);
    functions(dist_tab_sq,dist_tab,dir_tab);
}
```
