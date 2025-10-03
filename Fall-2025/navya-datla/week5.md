State: I am currently not stuck or blocked. 

Progress this week: 

This week we worked on finishing a mostly complete draft of the new RTL design. 
- takes into account the new packetized compiler format and removes the need for register status tables
- the issue policy is now far less complex
  - removes the need for age logic since we have removed the dependencies
- ALU contains mult/divide isntructions
- might need to bank register files - still need to confirm
- each FuST has a ready signal which will tell when the FU is done processing

At the SoCET meeting we heard Rishi present about TPUs. 

Next Steps: 
- Talk to vector core to understand their design and let them know we need a bit indicating a reduction so we know when to use 
- Communicate with other teams regarding the ISA