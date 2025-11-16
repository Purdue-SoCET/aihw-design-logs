# Week 12
## State: 
- I do not need help

## Progress: 
- Integration of emulator
- The emulator can now successfully run basic programs
- Memory subsystem altered to have to regions instruction and data
    - Instruction memory is 160 bits or accessible every 20 bytes
    - Data memory is word adressable
    - REASONING for this is that if instruction were word addressable each instruction would be split across multiple addressing making pc addressing very confusing
- Vector registers will now hold float32 but converted to fp16 at the very end for correctness and simplicity
    - numpy only has float32 no bf16 
    - Operations will be performed in float32
- Similar structure to scalar register file for mask registerfile
- Decoder takes 160 bit packet and returns an array of dicts with each field in the dict, ie. mnemonic, imm, rs1 etc
- Will check type/mnemonic and issue to execute units along with rs/vs
- Scratchpad need to ask Akshath since scratchpad instr not in ISA doc

- Design review 2 finished

## Next Steps:
- Final Senior Design Presentation
- Research expo
- Final Report
- Clean up emulator