# Week 14

State: I am not stuck with anything, don't need help right now. 

## Progress
- **VLIW Packetizer Integration:**
  - Finished integrating the VLIW packetizer into the compiler backend.
  - Added a new function that identifies branch and jump instructions to divide the assembly code into basic blocks for packetization.
  - Checked the output and verified that each basic block is correctly divided and that packets are following the dependency rules and latency constraints.

- **Vector Instruction Implementation:**
  - Finishing all vector instructions from the frontend to IR then to the codegen.
  - Start testing the vector instructions with some simple programs and make sure they are compatibile with the updated ISA bitmaps.
  - Fixed some problems with opcode decoding and instruction mapping that came up during testing.

- **Final Report:**
  - Started writing the final report for the project.
  - Finished the introduction part, including the problem statement, background, and significance.
  - Created an outline for the rest of the report, including solution design, results, and future improvements.
  - Each team member has been assigned to a specific section to write.


## Design Choices
- **Basic Block Division:**
  We have decided to split the assembly into basic blocks based on branch and jump instructions to ensure that the packetization stays within control-flow boundaries. This method also allows the compiler to handle instruction scheduling easier.

- **Compiler-Hardware Synchronization:**
  We have decided to Finish our vector instructions first so that we can test them in parallel with hardware updates. This can helps us validate both the ISA and packetization correctness.

- **Final Report:**
  We have decided to divide the final report sections from IR generation, packetization, and scheduling to register allocation so that readers can see how each part contributes to the system overall.


## Next Week
1. **Vector Instruction Testing:**
   - Finish testing all vector instructions with more complex programs.
   - Verify that the compiler will generate packets that execute correctly on simulation.

2. **Final Report:**
   - Finish the “Solution” and “Results” sections.
   - Start getting people to check our reports.

3. **System Integration:**
   - Run end-to-end tests to confirm the full compiler pipeline works smoothly.

