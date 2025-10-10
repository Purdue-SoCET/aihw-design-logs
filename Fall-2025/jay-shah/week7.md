# Weekly Report – Week 7

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. Focused on the scheduler core architecture this week. Read up on VLIW from the following sources:
   - https://www.engineering.iastate.edu/~zzhang/courses/cpre581-f06/lectures/Lecture24-1p.pdf
   - https://www2.seas.gwu.edu/~bhagiweb/cs211/lectures/epic.pdf
   - https://www.youtube.com/watch?v=FvJTnPEGVWg&t=70s
   - https://www.youtube.com/watch?v=jBzj24--_uE
   - Appendix H of Hennesy and Patterson, lecture slides 3c of ECE 565.

2. Discussion with Vector core team on 10/08 regarding how the different vector ops are pipelined and how the vector register file can be banked. This information will be helpful to us to decide on the possible format of the packets of instructions containing vector ops. Confirmed that we can issue multiple instructions parallely to the vector-core

3. Discussion with Sooraj on how to architect the scheduler pipeline. Following points were agreed upon:
   - Packets containing 2/3/4 instructions will be fed to the pipeline. The format of the packet will be chose from some available possible combinations given by us to the compiler. Packets will have no instructions dependent on each other within itself. Banking of the scalar and vector register file to be decided by us based on the packet types possible (How many loads, stores, ALU, vector ops within a packet). Typically we don't allow loads and stores in the same packet. Each packet to have maximum one branch. **Reasoning:** Maximum 4 instructions per packet are chosen for area considerarions. Following partial VLIW methodology for crafting independent packets. More than 1 branch per packet will cause multiple stalls in the pipeline to resolve both the branches. Loads and stores in the same packet will lead to speculative loads.
   - No predication and load speculation. **Reasoning:** Too much area-consuming and complicated hardware for not much benefit, as the loop unrolling and software pipelining allows for sufficient instruction-level parallelism for our workloads.
   - Branch speculation uptil the decode stage, not beyond that. We will use a branch predictor to issue instruction for either taken or not-taken case, and allow the instructions to proceed upto the decode stage. After that we halt the pipeline and allow the branch to resolve in execute, check if our prediction is correct. If it in not, flush the pipe till decode and take the correct route. **Reasoning:** Beyond decode, it would be messy to reverse the effects of some operations like load in case of branch misprediction, so better to just do the speculation til decode.
   - Check / Update mechanism. A metadata of 2N bits present with each packet of instruction that informs us about possible dependencies across packets, and will help us identify when it is "safe" to issue a dependent instruction. There are N 1-bit registers present in the design. Each packet has N update bits - when the packet is issued, we see if if some bits from those N are 1, and set the particular registers of design corresponding to the positions where the update bits are set to 1. When the packet completes execution (last instruction of packet completes execution), we clear the registers that this packet had set. Now, each packet also contains N check bits. Before issuing a packet, we check if any position of N check bits are 1, if they are, we check the N registers to see if the corresponding regs are also set to 1. If they are, then there is a dependency on a packet up ahead, and we must wait before it completes. Once the packet up ahead completes execution, it will clear the corresponding registers, and we can proceed with issuing. Currently N has been chosen as 8. **Reasoning:** It is an extremely effective method to record dependencies across packets that uses minimal hardware. It adds 2N bits metadata per packet, so no changes to the ISA.
   - This method can also make use of an issue queue. If we have multiple packets arriving, it's possible that packets 2 and 3 are dependent on packet 1, but packet 4 in independent. A CAM issue queue will allow us to issue packet 4, while keeping packets 2 and 3 in the queue. We don't need as big a CAM as a standard OOO processor, because again the parallelism in ML workloads will help us to reduce dependent packets.

     <img width="2016" height="1512" alt="image" src="https://github.com/user-attachments/assets/f2855f6c-c869-4200-8ec5-f24186539aa6" />
                                                      Picture credits: Josh

4. Discussion on Systolic array controller, and the changes expected. 1 particular change needed is the inclusion of a global stall signal, that will stall the feeding of weights and inputs to the systolic array and also the writeback of outputs. The stall can come from 2 places - the writeback buffer if it overflows, and from the input FIFOs, is there is no valid data being supplied by the memory, while a MAC is ongoing. 

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
