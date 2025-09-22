## NOTE: I was assigned to AI HW and the compute controller at the end of Week 3/beginning of Week 4 making this my first design log.

## State: I am not stuck with anything, don't need help right now. Note

## Progress
On the Sunday meeting, I was introduced to the project and familiarized myself with resources to understand how GEMM is used in a convolution. On Monday I met with Saandiya, Sooraj, and Jing to discuss some of the problems we need to solve, and then some solutions for tiling the convolution within the systolic array. On Tuesday I attended the Scratchpad meeting and learned more about their progress and design to use in the compute controller context. On Thursday, I met with Saandiya and Malcolm where we discussed the current issues with the Python/Jupyter Notebook simulator and we discussed some strategies to fix the systolic array model, as that was causing erroneous results. I was later assigned the task of getting the simulator to work with the existing systolic array model.

## Tasks
  My current task is making the current iteration of the compute controller interface with the Systolic Array. The current iteration (as of Thursday) had a custom implementation of SA that did not work.

  Python Simulator Work 
    - Replace current implementation with one from SA team.
    - Verify correctness with various random matrices (try multiple sizes, see if algorithm can support various edge cases)
    - Simulator will not support stride > 1 or kernel > 5x5 for now.

## Notes
   Simulator kernel loading and transformation to toeplitz has been verified, but SA portion is the bottleneck for correctness of the simulator

## Future Plans 
Once simulator is finished, we can get the edge cases verified (including when stride != 1) and then work on a hardware implementation (RTL Block Diagram) and subsequently RTL implementation.
