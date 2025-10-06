## State: I am not stuck with anything, don't need help right now.

## Evidence of Progress:
These are progress made from first semester senior design:
RTL: https://app.diagrams.net/?src=about#G1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR#%7B%22pageId%22%3A%229D6ffl-pBdOOQ0Yu_FEU%22%7D 
Simulator: https://github.com/Purdue-SoCET/tensor-core/blob/systolic_array_cache/tmp/conv_on_systolic_array_2d/Custom_Works.ipynb

Last semester we got a basic idea on how to convert Convolution operations to GEMM operations to fully utilize the existing Systolic Array, supplemented with newly built Scratchpad that is being worked by Akshath. We came up with a unit called Tensor Compute Accelerator (TCA), which has both GEMM and Convolution controllers and this interacts between Systolic Array and Scratchpad.

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
