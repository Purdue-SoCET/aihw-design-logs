Week 3

State: I am not stuck with anything, don't need help right now.

## Progress

- **Compiler Meetings:**
  - Attended compiler group meeting to align on responsibilities and immediate deliverables.
  - Discussed ISA green card status and the importance of finalizing register and instruction formats.

- **Backend:**
  - Traced the backend flow in PPCI AST, IR, instruction selection, encoding, code generator and assembly printer.
  - Understood IR module relationships and how classes (tokens, instructions, registers) are wired together.
  - Attempted to generate IR directly through commands (bypassing the parser) to better understand how IR nodes are instantiated and connected.

- **Naming Convention:**
  - Proposed a general naming convention for registers, tokens, and instruction fields to maintain consistency across the architecture files.
  - Standardized on bitmapping names (opcode, rd, rs1, rs2, imm/imm12).

- **ISA Green Card:**
  - The hardware team is still finalizing details of the Atalla architecture.
    - Total register count and width (likely 64-bit, TBD exact count).
    - Special-purpose registers (SP, PC, RA, GP).
    - Whether floating-point registers will exist separately or be handled by the compiler.
    - Final instruction forms (VM, VV, VS, VI, SA).
  - Continued backend exploration so the compiler skeleton will be ready to integrate once the green card is released.


## Design Choices

- **Compiler Base:** Decided to commit to PPCI for now instead of LLVM, given its lightweight structure and ease of modification. LLVM remains an option once ISA details stabilize.
- **Instruction Layout:** Standardizing on a 64-bit instruction word with consistent field names (opcode/rd/rs1/rs2/imm/imm12) to simplify parsing and encoding.
- **Code:** Get assembly working first before handling parser integration of advanced constructs.


## Plans for Next Week

1. **IR Format:**
   - Study PPCI IR formatting conventions in more detail.
   - Write small test cases that generate IR directly (without parser) to confirm formatting rules.

2. **IR Generation:**
   - Begin creating simple custom IR nodes that represent placeholder instructions.
   - Run round-trip tests IR, backend lowering, Attala assembly, disassembler, and compare text output.

3. **Architecture Preparation:**
   - Begin drafting arch.py with token layouts based on current ISA draft.
   - Coordinate with hardware/ISA teams to resolve green card questions (register count, SP/PC, FP).

4. **Documentation:**
   - Record backend tracing results and naming convention decisions for the rest of the team.
   - Add diagrams of PPCI frontend/backend flow to design notes. 