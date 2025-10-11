# Week 4

State: I am not stuck with anything, don't need help right now. 

## Progress  

- **Team Meetings:**
  - Attended compiler group meeting to coordinate division of tasks.
  - Participated in the Senior Design Idea Pitch to present our problem statement and proposed solution.

- **ISA Green Card Review:**
  - Received the draft ISA green card and began analyzing it to understand instruction formats and register conventions.
  - Questions:
    - Register size and count(64-bit GPRs, TBD count).
    - Do we need stack pointer (SP), program counter (PC), and other architectural registers?
    - Should the ISA include separate FP registers or rely on compiler-level typing?
    - Deciding between “Atalla” and “AMP” for the architecture label.

- **Architecture Bring-up:**
  - Began working on the compiler backend architecture files.
  - Arch.py defines all instruction formats and provides the connection between tokens, encodings, and higher-level compiler passes.
  - Looked at how PPCI handles RISC-V instruction layouts as a reference for structuring our own.

- **Role Assignment:**
  - Assigned responsibility to complete arch.py by next week. This will establish the base skeleton for our ISA support, enabling the compiler to parse, encode, and print scalar instructions.

- **Evidence:**
  - Notes from the Senior Design Pitch summarizing problem, solution, and challenges.
  - Arch.py skeleton finished in Github codebase.


## Design Choices

- **ISA Assumptions:** Assume 64-bit instruction layout with consistent field naming (opcode, rd, rs1, rs2, imm/imm12).
- **Incremental Bring-up:** Focusing on scalar instruction formats first (VM, VV, VS, VI, SA), leaving floating-point and vector operations for later once scalar support is complete.


## Next Week

1. **Architecture Development:**
   - Finish implementing `arch.py` with all scalar instruction formats.
   - Ensure consistent field naming across tokens and instruction definitions.

2. **Testing:**
   - Create round-trip tests for scalar instructions (parse, encode, disassemble, print).
   - Add error handling for invalid registers, operand counts, and immediate overflows.

3. **Collaboration:**
   - Sync with hardware team to resolve open ISA questions (register file size, SP/PC requirements, FP support).
   - Confirm final architecture naming (Atalla vs AMP).
