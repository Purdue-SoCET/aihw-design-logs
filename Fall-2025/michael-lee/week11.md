# Week 11
## State: 
- I do not need help

## Progress: 
- New project change due to time constraint
- To verify operation by Thanksgiving will implement emulator to verify correctness
- Emulator will not be cycle accurate
- Can be used as golden reference when RTL design is implemented
- General Idea
    - While not halt loop increment pc
    - Fetch 160 bit instruction
    - For every instruction in packet decode execute
- Implemented register file 
    - Read, write, and dump functions
    - Paramaeterizable to and register 
    - May add bank conflict checking
- Josh implemented memory
- Navya implemented decode

## Next Steps:
- Will continue to implement and integrate emulator (instructions and specifically vector operations)