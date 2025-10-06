## State: I am not stuck with anything, don't need help right now.

## Evidence of Progress:
These are progress made from first semester senior design:
RTL: https://app.diagrams.net/?src=about#G1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR#%7B%22pageId%22%3A%229D6ffl-pBdOOQ0Yu_FEU%22%7D 
Simulator: https://github.com/Purdue-SoCET/tensor-core/blob/systolic_array_cache/tmp/conv_on_systolic_array_2d/Custom_Works.ipynb

## Progress
Last semester we got a basic idea on how to convert Convolution operations to GEMM operations to fully utilize the existing Systolic Array, supplemented with newly built Scratchpad that is being worked by Akshath. We came up with a unit called Tensor Compute Accelerator (TCA), which has both GEMM and Convolution controllers and this interacts between Systolic Array and Scratchpad. The idea is to perform im2col on the exisiting matrix and multiplying it with a kernel matrix which is flattened.
Readings: https://docs.nvidia.com/deeplearning/performance/dl-performance-convolutional/index.html  
From this we learnt about:  
1. All the parameters involved in convolution, including dilations and how they affect convolution.
2. Our method is called an implicit GEMM method.
3. It is important to reiterate that matrices of these sizes are not stored in memory; they are an abstraction to help explain the computation. The "repeated" values are not literally copied, and wasteful reads from memory are avoided.

We chose the implicit GEMM method because it maximizes reuse of existing systolic array hardware, minimizing hardware redesign effort. The im2col transformation allows convolution data to be mapped efficiently into the matrix-multiply pipeline, enabling reuse of the GEMM controller logic.

This week: Revisited last semester’s RTL and simulation environment, confirmed convolution-to-GEMM mapping logic works as intended, and reviewed memory dataflow between TCA and Scratchpad.

## Plan:
To implement TCA in System Verilog and synthesize the module.  
To create an interface with Scratchpad and Systolic Array to verify convolution controller works together.  

Timeline:  
9/14: Complete python simulation  
9/21: Complete RTL & FSM  
10/5: Implementation in System Verilog  
10/12: Come up with a Test Plan  
10/31: Verification and fix errors  
11/16: Integration and testing  
11/30: Fix failures and get figures  
12: Documentation + Report
