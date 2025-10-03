## State  
I am not stuck with anything as of right now.

## Progress
I attended Systolic Array Meeting led by Malcolm:
1. Met with new teammates, I will be working with Myles for convolution controller.
2. Malcolm explained about Wallace Tree implementation in systolic array, how does it work and why.
3. Got assigned roles to work on rest of the semester.

I attended the Scratchpad Meeting led by Akshath and Vinay:
1. Got to know the entire finalized Scratchpad Architecture, the subcomponents, why we need a Scratchpad and how does it work on a very high level.
2. I will be working on Tensor Compute Accelerator with Myles, we need to figure out an FSM and RTL by September.
3. Got to know timeline of my work that I will be doing this semester.

## Notes
FSM and RTL made last semester doesn't completely work. We need to figure out masking and shifting of row and column indices of the matrix within the TCA which consist of both GEMM and Convolution Controller.
The Scratchpad will provide me with an entire row or an entire column at once and its the TCA's job to mask and shift these values as it needs to be before entering the Systolic Array.
There is already an existing Python simulator, we need to edit it to make sure our new idea works.

## Next Steps
I will be working on the new logic and discuss some ideas with Myles and nail it down during the Sunday team meeting.

