- Swizzling: 
    - Read this first: https://research.colfax-intl.com/tutorial-matrix-transpose-in-cutlass/
        Don't worry about the code. Understand why Swizzling and Transposing are important. 
        It discusses a GPU view of things. GPUs use SMEM similar to what we want Sys-Array to use Scratchpad for. 
        Bank Conflicts, Row-Major, Column-Major are the main keywords here.  
    - https://leimao.github.io/blog/CUDA-Shared-Memory-Swizzling/
        More details. Don't try to memorize this. ChatGPT will help. 
    - (Optional:) Math proofs as to why Swizzling works -- https://leimao.github.io/blog/CuTe-Swizzle/
    - (Optional:) https://docs.nvidia.com/cuda/parallel-thread-execution/#tensor-swizzling-modes
    - (Optional:) https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__TENSOR__MEMORY.html -- Inspiration.

- GEMMs: 
    - Why?: https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/
    - GEMM Animations: https://pytorch.org/blog/inside-the-matrix/
    - GEMM Systolic Array: https://ecelabs.njit.edu/ece459/lab3.php
    - Systolic Array Arch: https://www.linkedin.com/pulse/4x4-systolic-array-matrix-multiplication-scalable-256x256-mulleti-8p6ic/
    - (Optional:) https://siboehm.com/articles/22/CUDA-MMM
        This is a GPU focused optimization guide for GEMMs. Gold Mine. 
        Not exactly relevant, but would be great for you to understand. 
    - (Optional:) Nvidia's MM docs: https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/index.html

- Convolutions: 
    - Why?: https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/
    - Convolutions using Numpy: https://hackmd.io/@machine-learning/blog-post-cnnumpy-fast
    Note: Convolutions and GEMMs are different things. People wanted to use GEMM specific hardware to run Convolutions. Below are two ideas on doing so: 
        - https://iq.opengenus.org/im2col/
        - https://iq.opengenus.org/im2row-convolution/
        Do you see the problem here? To convert a Convolution to a series of GEMMs, you need to remake the complete matrix in a Toeplitz Matrix format -- https://mathworld.wolfram.com/ToeplitzMatrix.html

        We want to do this more efficiently!! We say, at runtime, we'll use Scratchpad's Swizzling and a custom TCA FSM in order to use GEMM hardware to do Convolutions, __without need of recreating the Matrix__ in Toeplitz format in RAM. 
    - Convolution Simulator: https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_akshath/tmp/TCA_Sim.ipynb
        Clone this, and run if you want. It's a Systolic Array and Conv Simulator in Python. 
        In the third cell, keep `N = 1` and `K = 1` and `C = 1` constant. Change H, W and R (= S) values to try different activation and kernel sizes.

