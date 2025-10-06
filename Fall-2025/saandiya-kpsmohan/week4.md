## State: I am not stuck.

## Progress
- On Monday (9/15/25), me, Sooraj, Nikhil, Jing and Malcolm sat together and discussed the whole flow of convolution from tiling into the Scratchpad until the end of the convolution.   
- On Tuesday (9/16/25), I met up with Jing and Malcolm again to further understand this new design and I started implementing this in a Python simulator.  
- The new design, idea, requirements are documented in this google docs: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?usp=sharing

## Evidence of progress
This section explains how convolution will be done in hardware from top to bottom: Implicit GEMM method. The core idea is that the inputs will be transformed into a Toeplitz matrix using im2col method, and it will be matrix matrix multiplied with a flattened kernel vector. Psums will be accumulated across the convolution kernels.

## 1. Tiling
This section explains how tiling will be done in the software and why:
![IMG_7434](https://github.com/user-attachments/assets/eb985763-16d4-4222-8295-1b2443b02250)

This is an example of how tiling will be done:
![Screenshot 2025-10-06 at 6 16 09 PM](https://github.com/user-attachments/assets/41408632-544f-4648-a07f-7018ae10fddf)

When loading the input matrix as tiles we are padding the right and bottom with extra 2 rows/columns.   
Deterministic equation: (row, col) = (t_i * (T−K+1) * s, t_j * (T−K+1) * s).  
Note that the last row/col of tiles extend past the 64×64 boundary → this is where padding is implicitly required so the SA can still process a full 32×32 input window. We tile it this way so that botht the previous and next convolution operations has all the appropriate values needed to carry out convolution based on kernel size and stride. The tiles will be saved in the scratchpad.

## 2. Kernels
Kernels will be transformed into 1 vector (including all channels). One column of systolic array is the same kernel but different channels. Example:
![Screenshot 2025-10-06 at 6 23 14 PM](https://github.com/user-attachments/assets/0cc38d86-df6f-44ce-b99e-3e13326532b3)
![IMG_7436](https://github.com/user-attachments/assets/42a085ac-3e34-4283-8c84-22569f9a6e64)

## 3. Inputs
Load 1 tile at a time from SP to TCA, rearrange matrix into Toeplitz matrix using im2col in a register/buffer. Stream this into SA, across 32 buffers at a time.
![IMG_7437](https://github.com/user-attachments/assets/af20bc95-f3e6-42c3-b7e0-4e08bfba9b89)

## 4. Post processing/PSUMS adding
Psums will be added column by column in the systolic array corresponding to the output kernel. During the next convolution operation, the existing psums will just be fed back into the top of the systolic array to continue accumulating.

## Python Simulator
- As of now, my simulator works with different kernel number, kernel size and input size with stride = 1 with the tiling, and kernel loading and using matmul to represent the Systolic Array.
- The simulator doesnt work with my implementation of an actual Systolic array, so we narrowed down the error to the implementation of the Systolic Array itself.
- The current simulator is updated in my github. https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/tmp/TCA_tiled_sim.ipynb  
Current result:
![IMG_7443](https://github.com/user-attachments/assets/9a7c62c6-b27f-4984-979b-5356892f7610)

## Design Choice
We went with this design flow because this is how a typical convolution is done even on the software level. Now we have a unit in the hardware to do convolutions instead of decoding the instructions every single time before carrying out 1 convolution operation. This also utilizes the existing systolic array. Obviously, there are some limitations where the utilization of the systolic array itself depends on the number of output channels. The more the output channel size, the better the utilization of a 32x32 systolic array.

## Next Steps
- I am going to try and use the SA simulator students made last semester and hopefully that works.
- Planning to finish this by Sunday meeting, so that we can implement the RTL during the team meeting.
- During Sunday meeting, I will go over this with Sooraj and Malcolm






