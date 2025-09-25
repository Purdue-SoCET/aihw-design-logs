State: not stuck


Progress: 
- In aihw-ppci-compiler branches (personal: vihaanc-dev)
- Compiled RISC-V from object file to binary (proof of concept for future testing, device input)
- Found limitations of inline-asm (cannot actually store output in a register)
- Busy this week/next week due to outside reasons 


Future Plan: 

- Experiment with different ways to do the assembler. Eg: how to encode architecture-specific information to assembler
- Explore, for scalar core, bypassing IR to assembly, and simply doing some subsitution on RISC-V generated assembly. 
- Specify architecture-specific layout for linking, or just do manual linking. 