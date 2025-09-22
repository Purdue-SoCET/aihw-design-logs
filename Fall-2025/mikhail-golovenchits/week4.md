State: I am not stuck with anything, don't need help right now.

## Progress

- Frontend now (probably) correctly parses theta into IR
- Created the senior design idea pitch presentation and presented to team leads
- Nailed down specific problem statement, solution, and challenges
    - Problem:
The AI Hardware Team’s processor currently requires manual programming in assembly, making development time-consuming and error-prone. Developers need a higher-level interface to improve productivity.

    - Solution:
Design a compiler that translates and optimizes C code into the team’s custom ISA machine code. We will extend Pure Python Compiler Infrastructure (PPCI) according to our hardware specifications.

    - Possible challenges:
Extending the existing codebase of PPCI and the general architecture of the compiler. 
Modifying both frontend parsing to accommodate new instructions, and creating a custom backend architecture to match the specifications of the processor.

- Received feedback from Dr. J: include optimization of instructions into out senior design plan (possibly for next semester)

## Next steps

- Create a method to lower IR to RISCV assembly
    - to do that, most likely need to modify the instructions.py file in the riscv architecture to add parsing for theta IR
- Continue helping other members with creating a new architecture