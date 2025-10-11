# Week 6

State: I am not stuck with anything, don't need help right now. 

## Progress

- **Instruction Tokens:**
  - Created token classes for each instruction type based on the Atalla green card.
  - Defined 64-bit layouts with fields for opcode, rd, rs1, rs2, and imm/imm12 as needed.
  - Verified that scalar instruction encodings match the ISA specification and can be disassembled consistently.

- **Scalar Instruction Implementation:**
  - Built initial code templates for scalar ALU instructions in the architecture file.
  - Connected the bit mappings of each token class to their corresponding instruction templates.
  - Verified round-trip consistency (encode, decode, print) on simple ALU programs.

- **IR to Machine Code:**
  - Successfully lowered from IR to machine instructions using PPCI backend infrastructure.
  - Studied register allocation in PPCI to better understand how to support our 64-bit GPR class.

- **Packetization:**
  - Started planning packetization (bundling independent instructions into parallelizable packets).
  - Read preliminary material on VLIW-style static scheduling to understand hazards (RAW, WAR, WAW).
  - Identified IR stage as a likely location for packetization logic, since dependencies are most visible there.

- **Evidence:**
  - Commits with token classes and scalar instruction bring-up pushed to repo (see Discord for links).
  - Parsing simple arithmetic C functions through AST, IR, and Attala assembly.


## Design Choices

- **Scalar Instructions:** Began with scalar instructions only, since they provide the foundation for ISA bring-up and debugging. Floating point and vector ops will build on this once the scalar pipeline is stable.
- **Encoding Consistency:** Chose to mirror RISC-V-like field layouts to reduce confusion (opcode/rd/rs1/rs2/imm12) and simplify assembler/disassembler implementation.
- **Packetization Timing:** Decided to begin packetization research early instead of waiting until after scalar/vector completion, to ensure compiler infrastructure can support bundling without major refactoring.


## Plans for Next Week

1. **Design Review Prep:**
   - Prepare and rehearse design review slides and demos.
   - Summarize scalar ISA progress and initial packetization strategy.

2. **Scalar Instruction Completion:**
   - Meet with team to finish remaining scalar templates.
   - Validate encoding/decoding against sample C programs.
   - Debug edge cases (branch immediates, offset calculations).

3. **Begin Advanced Features:**
   - Start implementing vector instruction skeletons alongside scalar ISA.
   - Prototype packetization algorithm at IR stage:
     - Detect independent instructions.
     - Group into packets of up to 4.
     - Emit bundles in Attala assembly.

