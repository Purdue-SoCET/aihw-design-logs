# Week 13

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Design Review and Purdue Undergraduate Research Expo:**
  - Attended both the general design review and the senior design review.
  - Presented our project at the Purdue Undergraduate Research Expo and explained our compiler architecture, packetization mechanisms, and ISA integration to both professionals and unfamiliars.
  - Practiced explaining our project to both technical and non-technical audiences.
  - Received feedbacks and questions from professors and audiences, especially the decision to create a new ISA instead of extending RISC-V.

- **Feedbacks:**
  - Why not just extend RISC-V instead of designing a new ISA?
    - Right now we think that our machine requires custom instructions optimized for tightly coupled VLIW and systolic operations, particularly for machine learning workloads.
    - We believe that simply extending the RISC-V ISA would limit our flexibility when defining new vector and tensor instructions, especially when it comes to scratchpad and systolic-array dataflows.

- **Vector ISA Implementation:**
  - Almost finished all of the vector instructions in the compiler backend.
  - We have talked to the hardware team about their modified ISA bitmap and we will start fixing them accordingly.
  - We have changed the opcode mappings and token layouts in the compiler to match the updated hardware definitions.


## Design Choices
- **ISA Design:**
  Compared to simply extending the RISC-V ISA, a custom ISA gives us better control over how dataflow, scheduling, and packetization interact with the hardware's parallel functional units. This allows vector, systolic, and SDMA instructions to be easily integrated into our compiler passes. However, from the professor's feedbacks, we have realized that using Python as our compiler language may limit the performance. Although Python allows easy development for research, we still have to be aware of Python's overheads and bottlenecks. We might have to migrate to another language in the future.

- **Poster and Presentation Focus:**
  We designed our poster in a way to highlight our compiler's ability to perform latency-aware packetization, scoreboard scheduling, and bank-aware register allocation. The poster was designed to make these compiler concepts easy to understand for general audiences outside of computer architecture.


## Next Week
1. **Vector ISA:**
   - Finish implementing all remaining vector instructions in the backend.
   - Update the instruction selector and codegen flow to use the new bitmaps.

2. **Compiler Synchronization:**
   - Debug instruction printing and encoding after the ISA update.
   - Try running our compiler with a larger code base and record the execution time.
   - Verify the codegen output for sample vector and GEMM kernels.

3. **Feedbacks:**
   - Discuss a response to the “Why new ISA?” feedback from the architectural knowledge we have learned so far.
   - Prepare materials for the final project report and presentation.

