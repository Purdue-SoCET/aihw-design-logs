State: I am not stuck or blocked at this time. 

Progress: 

*due to Fall break and having a 437 exam on Thursday, I didn't get to do as much this week

Wednesday 10/15 - Senior design group met to work on developing the compiler spec. Worked on the introduction sections 

- Developed new instructions due to the vector format. For loading in an immediate, we only have 25 bits of space available in an instruction out of the 32 that are needed. To support this issue, we need two separate instructions (load immediate and load upper immediate )
- Instructions will be 4x40 bits per instruction and 16 check and 16 set bits. Previously, each instruction was 48 bits and there were only 8 check and set bits. The reason the instr length changed was that they were able to be condensed. We increased to 16 bits for the dependency register because with 8 we felt there might be too many stalls as there would likely be more than 8 instructions in the pipe at a time. 
- Fleshed out how the dependency registers' counters would work. We need a way to figure out when a packet is done so that a packet with a dependency on the previous instruction would be able to know when it its dependencies are cleared. We handled this by ensuring that each instruction is tagged with a corresponding field that tells you which set bit it was originally correlated with. Each time a instruciton is written back, its  tag bit will tell the dependency register which counter to decrement. Once the counter is at 0, that bit in dependency register will be 0. 
- Decided that when we have bank conflicts we will handle those inside the sceggie and will take 3 cycles to resolve. However, compiler needs to know to avoid bank conflicts hopefully at least 70% of the time
- There are situations where we have to move mask from scalar register to mask register. In these case, we considered many different ways of doing this (one instr or multiple). We decided on multiple with different operations that move and convert. This makes it so we maintain a more RISC type ISA as opposed to a CISC type. 

- I also reached out to Cole to determine multiplication, division, mod worst case latencies. 


Thursday 10/16 - 
- I finished developing and submitted the abstract for the OUR poster presentation, discusing the problem, our approach, and the impact we want to have 
- https://docs.google.com/document/d/1v1pnD3Oixzc5w928pwdRQqF7BzCdNIqIGLxgcK-EC-0/edit?usp=sharing 

Next Steps: 
- Finish report from compiler
- Finish slides for design review
- Compile all worst-case latencies
- Low-level diagrams 


