# Weekly Report – Week 7

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. Focused on the scheduler core architecture this week. Read up on VLIW from the following source:
   - https://www.engineering.iastate.edu/~zzhang/courses/cpre581-f06/lectures/Lecture24-1p.pdf
   - https://www2.seas.gwu.edu/~bhagiweb/cs211/lectures/epic.pdf
   - https://www.youtube.com/watch?v=FvJTnPEGVWg&t=70s
   - https://www.youtube.com/watch?v=jBzj24--_uE
   - Appendix H of Hennesy and Patterson, lecture slides 3c of ECE 565.

2. Discussion with Vector core team on 10/08 regarding how the different vector ops are pipelined and how the vector register file can be banked. This information will be helpful to us to decide on the possible format of the packets of instructions containing vector ops.

2. Discussion with Sooraj on how to architect the scheduler pipeline. Following points were agreed upon:
   - Packets containing 4 instructions will be fed to the pipeline. The format of the packet will be chose from some available possible combinations given by us to the compiler. Packets will have no instructions dependent on each other within itself. 
   - No predication and load speculation. Reasoning: Too much area-consuming and complicated hardware for not much benefit, as the loop unrolling and software pipelining allows for sufficient instruction-level parallelism for our workloads.
   - Branch speculation uptill the decode stage, not beyond that. We will use a branch predictor to issue instruction for either taken or not-taken case, and allow the instructions to proceed upto the decode stage. After that we halt the pipeline and allow the branch to resolve in execute, check if our prediction is correct. If it in not, flush the pipe till decode and take the correct route.

---

## Next Week’s Tasks
1. Contact different teams for the latencies of different instructions, so we can update the compiler with worst case latencies of different types of instructions. Idea is to create a green zone where the compiler can put the dependent instructions for each type of instruction. It should fill up the space before the green zone arrives with independent instructions.
   Need to talk to vector-core for vector ops, scratchpad for memory ops and systolic array for Gemm and Conv instructions.
2. Create a report with all the ISA and Pipeline related stuff that will be useful for compiler. We need to add the following stuff to it:
    - Possible packet types: what type of 4 instructions can make up a packet. All combinations, not permutations.
    - Worst case latency for each type of instruction op. This in turn will tell the compiler number of cycles needed for each packet, depending on the slowest instruction of the packet.
    - Overview of the pipeline, hierarchy of the scalar and vector register files (number of ports etc).
    - clear / set meachanism discussed today.
3. Top level diagram on the scheduler core pipeline needs to be finalized.
