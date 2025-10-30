> This week was focused on completing the core Atalla-Sim classes, and coordinating with the team on which units to work on. 

## State

[STALLED] Waiting on CBG from Haejune. Deadline set for Friday.
[STALLED] Waiting on Backend Verification from Julio. Deadline set for Friday.

## Arch Updates
[NONE]

## Progress
- Check out the Atalla-Sim repository!
- Completed parameterizing the new Batcher and Benes designs. Set the REGISTER_MASK to get 4 options -- Fully Pipelined, Combinational, INTO_5, INTO_3. Values are set such that it can scale beyond 32x32. 
- Synthesized the Batcher and Benes for all 4 options at 1666.6ps period. Easing the timing constraints. As it was trying to meet the higher freq target, area was exploding. 
    > Q: Why was the area increasing, even though latches were being removed? 
    > A: Because Innovus increases the size of each cell drastically, to allow for a higher drive strength. We need this so that the signals can propagate faster to meet the new timing demands. 
- Decided that the programming model was going to be vector-based for the compiler, but tile based for the programmer. Programmer gets a fixed set of tiled-kernels, for GEMM and CONV. `float` inherently is defined as a `bfloat16` type -- programmer gets no flexibility. 
- Had a sit down with Rafael, and walked him through the Lockup Free DCache logic. 
- Adder the D-Cache and verification tbs into the new repository. 

## Future Plan
- Coordinate with Emmi and Rafael regarding Atalla-Sim Core-Libs. Emmi will work on Scratchpad, while Rafael will work on DCache.