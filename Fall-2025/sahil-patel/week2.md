I'm not stuck with anything. 

Progress 
-Progessing on understanding PPCI's backend and fronend support
-finding ways to implement changes to PPCI front and backend
-implementing new keywords in parser 

Notes

-The ISA team is working on a 64bit ISA. 
-Research PPCI or LLVM and decide which implementation is better
-Implement theta parser handling in order to see if compiler has possibility to compile to assembly 
-Focused on understanding data type handling within the parser. We looked at registers, vector, and scalar instructions to be able to understand how each could be handled in the PPCI Library. 



Progress

Progressing on understanding PPCI's backend and frontend support.

-Read PPCI docs and looked at example custom architectures to see how tokens, registers, and encoders are wired.
-Traced the flow: source > parser (AST) > IR (where used) > instruction selection/encoding > asm printer.
-Identified where we will plug in our ISA forms (VM, VV, VS, VI, SA). We will not add forms that the ISA does not define.

Finding ways to implement changes to PPCI front and backend.
-Frontend: added grammar hooks for our keywords (register names, vector notation, and “theta” syntax placeholder).
-Backend: outlined token field maps for 64‑bit instructions (opcode, rd, rs1, rs2, imm types). 
-Wrote small “round‑trip” checks to make sure a line of pseudo‑assembly parses into the AST without errors.

Implementing new keywords in the parser.

-Keywords added: basic register names (e.g., x0, x1, sp, ra, gp), vector registers (v0, v1, …), and simple op names for testing (add, addi, mov).
-Added immediate literals with size checks (imm and imm12 placeholders). Parser now rejects out‑of‑range immediates with a clear message.
-Set up a placeholder rule for theta so we can parse it now and decide exact semantics later.

Notes

The ISA team is working on a 64‑bit ISA.
-We standardized on a 64‑bit instruction word layout.
-Chose consistent names for fields: opcode, rd, rs1, rs2, imm, imm12.
-Defined the instruction forms we will support first: VM, VV, VS, VI, SA. We will not introduce a VU form because it is not in the ISA.

Research PPCI or LLVM and decide which implementation is better.
-PPCI: lighter, easier to modify quickly, faster to prototype custom encodings and asm printing.
-LLVM: heavier setup (TableGen, passes), but has many optimizations and ecosystem tools.
-Decision for Week 2: use PPCI for the initial prototype to reach “compile to assembly” faster; keep an LLVM path as a future option once ISA details stabilize.
Implement theta parser handling to see if the compiler can compile to assembly.
-Added a simple non‑semantic node in the grammar so code can parse without failing.
-Left a lowering step to be defined later (e.g., expand theta into a small sequence). For Week 2, goal is parse + print, not final semantics.

Focused on understanding data type handling within the parser.
-Confirmed default integer type as 64‑bit. Avoid accidental 32‑bit fall‑throughs in grammar and AST nodes.
-Clarified vector element types vs vector width (number of lanes). Parser enforces consistent width within an instruction.
 

![alt text](images/graphviz-07d396de43fdc9590d14a0c95cb83415db7a7601.webp)

Next Step
-implementing support for basic instructions 



