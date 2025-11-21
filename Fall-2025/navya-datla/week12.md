State: I am not currently state or blocked.

Progress:
- We finished up the emulator Python script this week
  - We integrated all of the different components: Decode which I worked on, Memory which Josh worked on, reg files which Michael worked on, and a lot of execute which Jay worked on
  - Modified the memory subsystem so that Instructions could be 160 bits, whereas data could be 32 bits
    - We decided that only data memory would be word addressible and instruction memory would not since if we had instruction memory be word addressible, instructions would be split up from each other 
    - We decided to separate I and D memory with a line that says "DATA MEM" for now, and once we align with compiler team we will figure out formatting
  - Current functionality: 
    - Large main loop
      - 160 bit instruction fetched
      - decoded into four packets returned in a dictionary with relevant parameters like opcode, instr type, source registers, dest. registers, etc. 
      - first: halt check - if halt, then we will halt execution (break out of the loop fetching instructions and dump a mem_out.txt)
      - If-Else block will check instruction names from packet and execute them by sending them to relevant functional units, updating pc, etc. 
  - Functionality to Test: 
    - Vector and scratchpad operations
    - Need to get clarity on some instructions before implementing as we don't want to implement them incorrectly
    - Need to implement scratchpad by better understanding the instructions
- Might need to change up the bit spec as it is ambiguous 
- We presented to Professor Raghunathan and rest of the AI HW team 


Next Steps: 
- Talk to scratchpad and vector teams for clarity
- Finish poster presentation
- Finish slides
- Give spec sheet to compiler team