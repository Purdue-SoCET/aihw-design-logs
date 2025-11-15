State: I am not currently stuck or blocked. 

Progress: 
- this week we decided that we will be aiming to complete an emulator that can serve as a golden model for the hardware
- the emulator will not be cycle accurate
- we will also be providing this to the compiler team so that they can verify the validity of their packets 
- I worked on the decoder logic for the packets 
  - These functions overall take in a 160-bit packet
    - extracts each instruction
    - based on opcode extracts necessary parts of the instruction
    - this can be found on the emulator branch in the decode.py file 
- We also added support for floating point packets to our design
  - They are stored in lower half of scalar registers

Next Steps: 
- Finish Decode checking logic
- Work on design review
- Finish compiler spec
- Work on poster for presentation