# Week 9
## State: 
- I do not need help

## Progress: 
- New design choice using 1 status bit per register that operate the same as the prior dependency registers
- Scalar Vector and Mask
- Each register instead of being explicitly set and checked will be check and set implicitly using the decoded rd, rs1, rs2
- Reason is to simplify the compiler since this way the compiler team doesn't need to have additional meta data per packet
- Also this enables as many instructions in flight as there are registers, with a few exceptions
- Working on interfaces to vectorcore and within datapath
- Need to clarify interface ports with vector team

- Met with compiler team to detail changes to VLIW's

## Next Steps:
- RTL coding will begin/continue
- Interfaces flushed out next will code individual pipeline portions