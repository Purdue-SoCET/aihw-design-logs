# Week 5

State: I am not stuck with anything, don't need help right now. 


## Progress

- **Instruction Tokens:**
  - Implemented token classes for all scalar instruction types according to the Atalla green card.
  - Defined 64-bit field layouts (opcode, rd, rs1, rs2, imm/imm12) consistent across instruction types.
  - Verified that encodings follow the bitspec and match expected positions for operands.

- **Scalar Instruction Templates:**
  - Built initial code templates in the architecture file for core ALU operations.
  - Connected the token bit mappings to their corresponding scalar instruction definitions.
  - Modified our ISA custom opcodes based on PPCI RISC-V backend structure.

- **IR:**
  - Successfully lowered PPCI IR instructions into Atalla machine instructions.
  - Gained a better understanding of PPCI register allocation scheme and how it maps into our 64-bit GPR model.
  - Conducted small round-trip tests by parsing C program, IR, Atalla assembly, disassemble, to confirm encoding consistency.

- **Packetization:**
  - Learned during the Sunday meeting that packetization will be required for sending instructions to hardware.
  - Approaches:
    - Integrate packet formation during codegen optimization.
    - Apply a post-processing pass over the generated assembly.
  - Current plan is to defer implementation until scalar support is fully stable.

- **Evidence:**
  - Commits pushed to amp_arch branch (see repo/Discord links).
  - Scalar ISA can now parse and encode simple test programs with correct instruction layouts.


## Design Choices

- **Scalar:** Started with scalar instructions since they form the foundation of the ISA and compiler. Vector and floating-point features will follow once scalar paths are stable.
- **RISC-V Layout:** Modeled instruction formats after RISC-V for familiarity and easier debugging, while adapting for Attala-specific operations.


## Plans for Next Week

1. **Design Review Prep:**
   - Draft and rehearse slides for the 9/28 design review.
   - Summarize scalar instruction progress and packetization strategy.
2. **Team Work Session:**
   - Collaborate to finish remaining scalar instruction templates.
   - Validate encoding/decoding for edge cases (branches, immediates, offsets).
   - Confirm parser rejects unsupported types (e.g., floats).
3. **Packetization + Vector Work:**
   - Split tasks after scalar instructions done:
     - Prototype packetization algorithm (likely IR-level pass).
     - Start building vector instruction skeleton (tokens, basic ops).
