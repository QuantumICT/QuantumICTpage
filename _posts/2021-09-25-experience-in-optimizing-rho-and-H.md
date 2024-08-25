---
title: 'Experience in Optimizing rho and H'
date: 2021-09-25
permalink: /posts/2021/experience-in-optimizing-rho-and-H/
author: Luo Haiwen
excerpt: "This article details the optimization experiences of rho and H kernels, including techniques for Fortran function optimization, kernel optimization, and lessons learned from unsuccessful attempts."
tags:
  - optimization
  - Fortran
---

# Experience in Optimizing rho and H

### Writing Slave Functions in Fortran

The biggest difference between writing slave functions in Fortran and in C is the way arrays are passed (as shown by the passing of the `matrix` array in the code below). Fortran slave functions use Cray pointers, and the `-fcray-pointer` flag is required during compilation.

```fortran
!Main core code
program main
	type :: param_t
		integer*8 :: matrix_loc
		integer m,n
		real*8 :: k
	end type param_t
	type(param_t) param
	integer,external :: slave_func
	real*8 matrix(100)
	integer :: m,n
	real*8 :: k
	param%matrix_loc=loc(matrix)
	param%m=m
	param%n=n
	param%k=k
	call athread_spawn(slave_func, param)
	call athread_join()
end program main
```

```fortran
!Slave core code
subroutine func(param)
	type :: param_t
		integer*8 :: matrix_loc
		integer m,n
		real*8 :: k
	end type param_t
	type(param_t) :: param,local_param
	real*8 gl_matrix(100)
	pointer(matrix_ptr,gl_matrix)
	integer i
	call crts_dma_get(local_param,param,24)
	matrix_ptr=local_param%matrix_loc
	do i=1,100,1
		print *,gl_matrix(i)
	end do
end subroutine func
```

### Optimization of Small Kernel rho

##### Calculation Process of rho (Described in C Language)

```c
for(int i_my_batch=1;i_my_batch<n_my_batches_work;i_my_batch++)
{
    tab_atom_centered_coords();
    prune_density_matrix_sparse_polar_reduce_memory();
    collect_batch_centers_p2();
    for(int i_index=0;i_index<batches_work_size(i_my_batch);i_index++)
    {
        prune_radial_basis_p2();
        tab_local_geometry_p2();
        tab_trigonom_p0();
        tab_wave_ylm_p0();
        evaluate_radial_functions_p0();
        evaluate_waves_p2();
    }
    dgemm();
    matrix_ddot();
}
```

##### Hotspot Analysis

|            | tab_atom | prune_density | i_index_loop | dgemm | matrix_ddot | collect_batch |
| ---------- | -------- | ------------- | ------------ | ----- | ----------- | ------------- |
| Proportion | 31%      | 25%           | 31%          | 12%   | 1%          | 0.2%          |
| Clock Cycles| 2.1 billion     | 1.7 billion          | 2.1 billion         | 0.8 billion   | 70 million       | 17 million      |

##### Optimization of tab_atom_centered_coords

```c
for(int i=0;i<n_centers_integrals;i++)
{
    dir_tab[0,i]=coord_current[0]-coords_center[0,centers_basis_integrals[i]];
    dir_tab[1,i]=coord_current[1]-coords_center[1,centers_basis_integrals[i]];
    dir_tab[2,i]=coord_current[2]-coords_center[2,centers_basis_integrals[i]];
}
```

1. Precompute values to reduce discrete memory access. The tab_atom_centered_coords function needs to be run n_my_batches_work times, which is the number of iterations of the outer loop. Each time, the access to coords_center[1,centers_basis_integrals[i]] is the same, so precomputing these values eliminates the need to access the centers_basis_integrals array repeatedly, converting the discrete memory access of coords_center into continuous memory access.  
2. Offload to slave core using OpenACC.  

| Before Optimization | After Optimization | Speedup Ratio |
| ------ | ------ | ------ |
| 2.1 billion   | 400 million    | 5.25   |

##### Optimization of prune_density_matrix_sparse_polar_reduce_memory

1. A similar function exists in H, where after offloading to the slave core, the speedup was 12.5. However, in rho, more than 60% of the time is spent on discrete memory access. Attempts were made to use non-blocking stride DMA, but a bug occurred after calling the corresponding function, which is yet to be resolved.

| Before Optimization | After Optimization | Speedup Ratio |
| ------ | ------ | ------ |
| 1.7 billion   | 980 million  | 1.7    |

##### Optimization of matrix_ddot

1. SIMD.  
2. Double buffering was initially implemented with non-blocking DMA, but the final result was incorrect, indicating that the computation finished before the DMA completed. As a result, blocking DMA had to be used, which negates the benefit of double buffering. Clearly, when the memory access to computation ratio is 1, this kernel is memory-bound.  
3. Load balancing was improved by ensuring each slave core's task is contiguous rather than using round-robin.  

| Before Optimization | After Offloading | SIMD Optimization | double buffer | Speedup Ratio |
| ------ | -------- | -------- | ------------- | ------ |
| 70 million  | 14.4 million  | 13.6 million    | 13.6 million   | 5.1    |

##### Final Optimization Result for rho  

|       | Before Optimization | After Optimization |
| ----- | ------ | ------ |
| 512 Cores | 3.380  | 2.220  |
| 64 Cores | 27.350 | 17.630 |

### Optimization of Small Kernel H

##### Calculation Process of H (Described in C Language)

```c
for(int i_my_batch=1;i_my_batch<n_my_batches_work;i_my_batch++)
{
    tab_atom_centered_coords();
    collect_batch_centers_p2();
    for(int i_index=0;i_index<batches_work_size(i_my_batch);i_index++)
    {
        prune_radial_basis_p2();
        tab_local_geometry_p2();
        tab_trigonom_p0();
        tab_wave_ylm_p0();
        evaluate_radial_functions_p0();
        evaluate_waves_p2();
        evaluate_xc_DFPT();
    }
    evaluate_first_order_H_polar_reduce_memory();
    prune_density_matrix_sparse_from_dense();
}
```

##### Eliminating Transposition of wave Array

```fortran
!Original code
real*8 :: wave(n_max_compute_ham,n_points)
real*8 :: contract(n_points,n_compute_c),wave_t(n_points,n_max_compute_ham)

wave_t=transpose(wave)
do i_compute=1,n_compute_c
	do i_point=1,n_points
		contract(i_points,i_compute)=partition_tab(i_point)*wave_t(i_point,i_compute)*&
								   (-grid_coord(i_point)+v_hartree_gradient(i_point)&
								    +dvxc_drho(i_point)*first_order_rho(i_point))
	end do
end do
call dgemm("T","N",n_compute_c,n_compute_c,n_points,1.d0,contract,n_points,wave_t,n_points,0.d0,&
            first_order_H_dense,n_compute_c)
```

The above is part of the original code for evaluate_first_order_H_polar_reduce_memory. The original code performs a transposition on the wave array, which was likely done to improve the locality of array accesses within the double loop. However, the transposition operation itself is time-consuming, and after linking with xmath, the transposition took longer than the matrix multiplication. Therefore, the transposition was eliminated. To maintain the locality within the double loop, the loop order was changed, and the definition of the contract array was modified. The modified code is shown below:  
```fortran
real*8 :: wave(n_max_compute_ham,n_points)
real*8 :: contract(n_compute_c,n_points)

do i_point=1,n_points
	do i_compute=1,n_compute_c
		contract(i_compute,i_point)=partition_tab(i_point)*wave(i_compute,i_point)*&
								   (-grid_coord(i_point)+v_hartree_gradient(i_point)&
								    +dvxc_drho(i_point)*first_order_rho(i_point))
	end do
end do
call dgemm("N","T",n_compute_c,n_compute_c,n_points,1.d0,contract,n_compute_c,&
            wave,n_max_compute_ham,0.d0,first_order_H_dense,n_compute_c)
```

| Before Optimization | After Optimization | Speedup Ratio |
| ------------------- | ------------------- | ------------- |
| 650 million         | 320 million         | 2             |

##### matrix_ddot Optimization

This kernel is the double loop from the previous section. With the experience from rho, this kernel neither uses SIMD nor double buffer.

| Before Optimization | After Optimization | Speedup Ratio |
| ------------------- | ------------------- | ------------- |
| 8.9 million         | 1.6 million         | 5.6           |

##### prune_density_matrix_sparse_from_dense Optimization

| Before Optimization | After Optimization | Speedup Ratio |
| ------------------- | ------------------- | ------------- |
| 1.5 billion         | 120 million         | 12.5          |

##### Final Optimization Results of H

|       | Before Optimization | After Optimization |
| ----- | ------------------- | ------------------ |
| 512 cores | 4.86            | 3.15               |
| 64 cores  | 35.28           | 21.10              |

### Large Kernel rho Optimization

##### Hotspot Analysis

|            | tab_atom | prune_density | i_index_loop | dgemm  | matrix_ddot | collect_batch |
| ---------- | -------- | ------------- | ------------ | ------ | ----------- | ------------- |
| Proportion | 31%      | 25%           | 31%          | 12%    | 1%          | 0.2%          |
| Clock Cycles | 4 billion | 400 million | 1.75 billion | 26 million | 1.7 million | 25 million |

##### tab_atom_centered_coords

Optimization Method: Similar to the small kernel, use a lookup table to replace discrete memory access with continuous memory access, and then use DMA operations to access memory.

| Before Optimization | After Optimization | Speedup Ratio |
| ------------------- | ------------------- | ------------- |
| 4 billion           | 400 million         | 10            |

##### prune_density_matrix_sparse_polar_reduce_memory

Optimization Method: Symmetric matrices can reduce memory access by half. Discrete memory access can be converted to faster DMA operations through data prefetching, fully utilizing bandwidth.

| Before Optimization | After Optimization | Speedup Ratio |
| ------------------- | ------------------- | ------------- |
| 400 million         | 300 million         | 1.3           |

##### Final Optimization Results of Large Kernel rho

|       | Before Optimization | After Optimization |
| ----- | ------------------- | ------------------ |
| 512 cores | 3.51            | 2.32               |
| 64 cores  | 22.31           | 15.23              |

### 

### Large Kernel H Optimization

##### Hotspot Analysis

| tab_atom_centered_coords | 10%  |
| ------------------------ | ---- |
| prune_radial_basis       | 4%   |
| tab_local_geometry       |      |
| tab_trigonom             |      |
| tab_wave_ylm             |      |
| evaluate_radial_function |      |
| evaluate_waves           |      |
| pz_lda                   |      |
| dgemm+ddot               |      |
| pre_reduction            |      |
| reduction                | 82%  |

### Comparison of Large and Small Kernels

##### rho

|       | Large Kernel | Small Kernel | Original |
| ----- | ------------ | ------------ | -------- |
| 64 cores  | 15.11    | 17.61        | 239.60   |
| 512 cores | 2.50     | 2.24         | 31.45    |

##### Comparison of rho Components (Only 64 cores are compared due to load imbalance in 512-core large kernel)

|             | tab_atom | prune_density | i_index_loop | dgemm | matrix_ddot | collect_batch |
| ----------- | -------- | ------------- | ------------ | ----- | ----------- | ------------- |
| 64_Small Kernel | 3.4 billion | 8.2 billion | 17.1 billion | 100 million | 15 million | 140 million |
| 64_Large Kernel | 2.5 billion | 6.4 billion | 21.1 billion | 360 million | 24 million | 480 million |

##### Summary

The previous conclusion was that the small kernel is slightly faster than the large kernel. As shown in the table above, the large kernel takes 2.50 seconds, while the small kernel takes 2.24 seconds. However, the results of testing with 64 cores show that the large kernel is slightly faster. Later, I tested the runtime of each sub-core of the large kernel and found that the reason was the load imbalance among the sub-cores.

##### H

|       | Large Kernel | Small Kernel | Original |
| ----- | ------------ | ------------ | -------- |
| 64 cores  | 85.92    | 21.10        | 131.02   |
| 512 cores | 13.63    | 3.15         | 17.47    |

##### Comparison of H Components

|             | tab_atom | update first_order_H | i_index_loop | dgemm+ddot | collect_batch |
| ----------- | -------- | -------------------- | ------------ | ---------- | ------------- |
| 64_Small Kernel | 3.4 billion | 980 million          | 26.3 billion   | 980 million  | 140 million   |
| 64_Large Kernel | 2.5 billion | 137.2 billion        | 9.08 billion   | 370 million  | 240 million   |

##### Summary

The `update first_order_H` part involves 64 sub-cores simultaneously updating `first_order_H`, which can cause data conflicts. Except for the `update first_order_H` part, each component in the large kernel performs better than in the small kernel. Therefore, if the large kernel can use a more efficient method to update `first_order_H`, it would make sense to use the large kernel to compute H. Currently, two methods have been considered: using fine-grained locks or having a few sub-cores dedicated to updating `first_order_H`.

### Some Failed Attempts

##### Optimization of i_index_loop

In the rho optimization section, it can be seen that this loop accounts for 31%. The loop contains seven small functions. Initially, the idea was to run the entire loop on sub-cores, but the result was that the runtime increased from 2.1 billion clock cycles to 3.4 billion clock cycles. The analysis showed that the loop involves too many arrays, many of which are accessed discretely, so even enabling the cache didn't help much. Later, the approach was changed to run the small functions within the loop on sub-cores individually, selecting `tab_local_geometry_p2` and `tab_trigonom_p0`. The `tab_local_geometry_p2` function involves four arrays, three of which are accessed continuously and one discretely, and has a significant amount of computation. Running it on sub-cores increased the runtime from 200 million clock cycles to 800 million clock cycles. The `tab_trigonom_p0` function involves only two arrays, both accessed continuously, and also has some computation. Running it on sub-cores increased the runtime from 190 million clock cycles to 650 million clock cycles. The analysis found two reasons: first, repeatedly running on sub-cores incurs significant overhead; second, the tasks of these two kernels are too small to be distributed among 64 sub-cores. In summary, running the entire loop on sub-cores slows down due to too many discrete memory accesses, and running the functions within the loop on sub-cores individually cannot offset the overhead of repeatedly running on sub-cores due to the small task size. Another idea is loop splitting, but this would waste too much space, so this loop cannot be optimized.

##### Master-Slave Collaboration

There is no data dependency between `i_index_loop` and `prune_density_matrix_sparse_polar_reduce_memory`. As mentioned above, `i_index_loop` cannot be run on sub-cores, so `prune_density_matrix_sparse_polar_reduce_memory` can run on sub-cores while `i_index_loop` runs on the master core to hide the runtime of `prune_density_matrix_sparse_polar_reduce_memory`. However, due to the presence of xmath, some built-in functions of `i_index_loop` call sub-cores, such as the log function, so this attempt also failed.

Since `prune_density_matrix_sparse_polar_reduce_memory` cannot collaborate with `i_index_loop` in a master-slave manner, it can collaborate with `tab_atom_centered_coords` in a master-slave manner. However, the result is obvious: the speedup of running `tab_atom_centered_coords` on sub-cores is much greater than 2, so it is better to run both functions on sub-cores rather than using master-slave collaboration.

### Summary

The Sunway OceanLight is severely bandwidth-limited between the master core and sub-cores, so unless the computation is particularly intensive, the sub-cores of the Sunway OceanLight cannot be fully utilized. For kernels that are not particularly computation-intensive, they can be considered memory-bound. Therefore, even if a kernel is entirely memory-bound, optimizing it is not meaningless. Computation-intensive kernels achieve the best speedup on sub-cores, kernels with only continuous or nearly continuous memory access achieve moderate speedup with a speedup ratio between 2 and 12, and kernels with a lot of discrete memory access may even experience a slowdown when using sub-cores.