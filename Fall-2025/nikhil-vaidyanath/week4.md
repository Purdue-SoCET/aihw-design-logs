## NOTE: I was assigned to AI HW and the compute controller at the end of Week 3/beginning of Week 4 making this my first design log.

## State: I am not stuck with anything, don't need help right now.

## Progress
On the Sunday meeting, I was introduced to the project and familiarized myself with resources to understand how GEMM is used in a convolution. On Monday I met with Saandiya, Sooraj, and Jing to discuss some of the problems we need to solve, and then some solutions for tiling the convolution within the systolic array. On Tuesday I attended the Scratchpad meeting and learned more about their progress and design to use in the compute controller context. On Thursday, I met with Saandiya and Malcolm where we discussed the current issues with the Python/Jupyter Notebook simulator and we discussed some strategies to fix the systolic array model, as that was causing erroneous results. I was later assigned the task of getting the simulator to work with the existing systolic array model.

I was introduced to a couple resources below which I used to familiarize myself with im2col Toeplitz formation for use in GEMM. A couple of my learnings/findings from the articles and the general architecture are below.

Resources:
https://docs.nvidia.com/deeplearning/performance/dl-performance-convolutional/index.html
[Scratchpad slideshow](https://docs.google.com/presentation/d/1XjGjhvMaXZSdV3kM1icad6hjELPlMbN1ILH3GXEVX6o/edit?pli=1&slide=id.g37bb5937d7c_1_2#slide=id.g37bb5937d7c_1_2)
im2col articles

Learnings/Findings:
Convolution takes a input matrix and a kernel and moves the kernel along the input matrix (kernel size < input size). The amount it moves is called the stride, for the most basic case (stride = 1) it moves along the matrix from left to right and top to bottom, performing a matrix multiplication. If we can remove the relevant patch from the input array, we can correctly perform a convolution. To do this, we can use a Toeplitz matrix, which has the property of having diagonals being the same value. Im2Col will use the dimensions of the kernel along with the values from the input to make the Toeplitz columns. These can be loaded into the systolic array. The systolic array will be doing the GEMM (general matrix multiplication) where weights are stationary and inputs are loaded from the left and shifted right. To the systolic array, GEMM and convolution are the same, but our TCA needs to correctly load the Toeplitz columns and/or weights correctly which will be the challenge. Scratchpad will be controlled by software and be our "cache" for matrices. We will read matrices from Scratchpad, operate on them with Systolic Array, and send them back to Scratchpad after the operation.


## Tasks
  My current task is making the current iteration of the compute controller interface with the Systolic Array. The current iteration (as of Thursday) had a custom implementation of SA that did not work.

  Python Simulator Work 
    - Replace current implementation with one from SA team.
    - Verify correctness with various random matrices (try multiple sizes, see if algorithm can support various edge cases)
    - Simulator will not support stride > 1 or kernel > 5x5 for now. In the hardware architecture we also won't support > 5x5 because Toeplitz form of 6x6 kernel means columns (patches) of more than 32 which can't be directly loaded into systolic array. We need to figure out a tiling mechanism to make larger convolutions supported if that's possible.

## Notes
   Simulator kernel loading and transformation to toeplitz has been verified, but SA portion is the bottleneck for correctness of the simulator

## Future Plans 
Once simulator is finished, we can get the edge cases verified (including when stride != 1) and then work on a hardware implementation (RTL Block Diagram) and subsequently RTL implementation.
