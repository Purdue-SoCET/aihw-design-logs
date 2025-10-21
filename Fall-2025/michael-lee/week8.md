# Week 7
## State: 
- I do not need help 

## Progress: 
- Completing top level diagram with changed crossbaring strategy
- First send all 4 VLIW's straight to 4 decoders of scalar or vector type
- Or 4 to 1 to the scratchpad decoder
- The crossbaring in execute to issue to correct FU
- 8 bit dependency registers
- Each VLIW comes with 4 40 bit instructions with 8 check bits and 8 set bits
- Sets will set one dependency register to indicate the VLIW exists in flight (dependency generating instruction)
- Notably, everything is a dependency generating instruction
- Also very key that any time a set bit is going to be set the corresponding dependency register should be checked as to not clobber the existing state for a VLIW
- Directly from slides below
- Illegal packets VS stupid packets
- Structural Hazards: Each FU can only be issued one instruction at a time
- Register File Structural Hazards: Only 4 banks and hence 4 reads from scalar reg file and 4 reads from veggie
- Branch Control Hazards: Branches necessitate one cycle stalls due to not having speculative execution 
- Bank Conflicts: Multiple accesses to the same bank cause stalls
- Long Latency Conflicts: Ideally schedule short latency instructions with other short latency, and long with long, especially branches to prevent branch hazards
- Green Zone Guarantees: Compiler is guaranteed completion after certain time so that it can not set certain dependencies
- Undergraduate research presentation abstract rough draft and final draft completed: https://docs.google.com/document/d/1v1pnD3Oixzc5w928pwdRQqF7BzCdNIqIGLxgcK-EC-0/edit?usp=sharing
- Script to determine valid packets was made



## Next Steps:
- Complete report to hand to compiler team
- Confirm worst case latencies and pipelining from vectorcore
- Prepare for design review
