# Week 7
## State: 
- I do not need help 

## Progress: 
- Met with Sooraj to flush out details on VLIW/EPIC implementation
- Instructions will be 4x48 bits per instruction and 16 check and set bits
- check will check for prior dependencies and set will set the packets own dependency
- Scheduler team is soley responsible for all scalar ops
- Planning for 2, 3, 4 "lanes" of execution
- 4 banks for scalar and vector register files one read and one write port
- Sooraj noted we may need many more for scalar
- Key point is that we will implement 8 dependency registers that will limit in flight instructions to 8 instructions and enable basic out of order abilities by checking and setting dependency registers
- Diagram for VLIW instructions and full crossbar created
- Readings: 
- https://www.engineering.iastate.edu/~zzhang/courses/cpre581-f06/lectures/Lecture24-1p.pdf
- https://www2.seas.gwu.edu/~bhagiweb/cs211/lectures/epic.pdf
- https://prod.tinker.cc.gatech.edu/symposia/lcpc01.pdf
- https://zoo.cs.yale.edu/classes/cs323/CAAQA6E/Appendix_H_online.pdf
- https://www.youtube.com/watch?v=FvJTnPEGVWg&t=70s

Main ideas:
- Register Renaming removes waw hazards not raw hazards war and rar are not hazards

Very Large Instruction Word (VLIW) 
- No or partial hazard detection
- Trade instruction space (may have noops) for easy decoding
- Compilers can schedule away FU stalls but cache misses cannot be speculated
- Motivated by complexity of superscalar -> clock rate
- One instruction is encoded for multiple ops
- Basic VLIW has no crossbar and maintains instr go to one FU no need for hardware routing
- VLIW lock step one stall = all stall -> hardware simplicity (Loads may stall add)
- VLIW does well for large blocks of math and less hard to predict branches
- similar to risc-> simplify architecture
- Risc originally compiles only to control signals
- Compiler find instr level parallelism
- Everything NEEDS PREDICTABLE execution cycles MUST BE PIPELINED
- BEST workload is dsp and embedded systems however works well wit tensorcore since very set workloads

Explicit Parallel Instruction Computing (EPIC)
- Compiler performs scheduling
- EPIC has dependencies in bundles but is specified which on which in extra bits
- First slide 17 can poor locality in special cache??
- Convert control dependencies to data dependencies
- EPIC implements a rotating register file that works together with software pipelining to extract efficiency from loops

Compiler's optimize w/the below summaries
- The most important of these is profile-guided optimization (PGO). Here's how it works:

- Profiling: The developer first compiles the program and runs it with a typical workload or dataset. This generates a "profile"—statistical data about how the program actually behaves in the real world (e.g., which branches are taken most often, which loops run the most).

- Re-compilation: The compiler then uses this profile data to re-compile the program, making highly intelligent scheduling decisions based on the most probable execution paths. For example, it might aggressively schedule instructions from a frequently taken if block, assuming that path will be chosen.

- Speculation: The compiler can schedule an instruction "speculatively" before it knows for sure if the instruction is needed (e.g., loading data from memory before a branch is resolved). It uses the profile data to make an educated guess, and EPIC includes special hardware features to squash the results if the guess was wrong.


Questions:
- So we use vliw for predication
- So we need to fetch more than one if predication occurs??
- Interleave fetchs??
- Ensure we have issuing every cycle
- Crossbar? Is it worth  what motivates this based on source true vliw means compiler knows which instr goes to what fu in the instr
- Predication means no trace scheduling/profiling


## Next Steps:
- We will make a document to track the ISA and architecture to provide to the compiler team
- Contact teams to find worst case guarantees for # of cycles for execution times
- Clean up ISA and bitspec
- Ask cole regarding scalar multiply divide mod
- question could a packet set more than one dependency ie writing to two vector registers liek two wide loads??