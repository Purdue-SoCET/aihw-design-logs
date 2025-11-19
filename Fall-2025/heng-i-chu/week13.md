# Week 13

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Design Review and Purdue Undergraduate Research Expo:**
  - Attended both the general design review and the senior design review.
  - Presented our project at the Purdue Undergraduate Research Expo and explained our compiler architecture, packetization mechanisms, and ISA integration to both professionals and unfamiliars.
  - Practiced explaining our project to both technical and non-technical audiences.
  - Received feedbacks and questions from professors and audiences, especially the decision to create a new ISA instead of extending RISC-V.

- **Feedbacks:**
  - “Why not just extend RISC-V instead of designing a new ISA?”
    - Our current reasoning is that Atalla requires custom instructions optimized for tightly coupled VLIW and systolic operations, particularly for machine learning workloads.
    Extending RISC-V would limit flexibility when defining new vector and tensor instructions, especially those tailored for our scratchpad and systolic-array dataflows.
  - We suspect that the need for dedicated VLSI paths for parallel data handling justifies our separate ISA design.
  - We plan to formalize these arguments and back them with microarchitectural data in the final report.

- **Vector ISA Implementation:**
  - Continued work on finalizing vector instructions in the compiler backend.
  - Verified encoding consistency between our compiler and the hardware team's modified ISA bitmap.
  - Adjusted opcode mappings and token layouts in the compiler to match the updated hardware definitions.
  - The hardware team updated the ISA bit specification this week, changing the encoding for several vector operations and modifying a few instruction fields.


## Design Choices
- **ISA Design Justification:**
  A custom ISA gives us tighter control over how dataflow, scheduling, and packetization interact with the hardware's parallel functional units. This allows for vector, systolic, and SDMA instructions that can be deeply integrated into compiler passes — something that extending RISC-V alone would complicate.

- **Poster and Presentation Focus:**
  We emphasized our compiler's ability to perform latency-aware packetization, scoreboard scheduling, and bank-aware register allocation. The poster was designed to make these compiler concepts accessible to audiences outside of computer architecture.


## Next Week
1. **Vector ISA Finalization:**
   - Finish verifying and implementing all remaining vector instructions in the backend.
   - Update the instruction selector and codegen flow to use the new bitmaps.

2. **Compiler Synchronization:**
   - Continue debugging instruction printing and encoding after the ISA update.
   - Validate codegen output for sample vector and GEMM kernels.

3. **Feedback Integration:**
   - Write a formal response to the “Why new ISA?” feedback using both architectural and VLSI reasoning.
   - Prepare materials for the final project report and presentation.

