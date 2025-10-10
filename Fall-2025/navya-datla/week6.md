State: I am currently not stuck or blocked. 

Progress this week: 

Prepared diagrams and slides for scheduler core for design review. 

On Sunday, we found out that our design was changing significantly again.
- GEMM Controller FU no longer needed as these instructions are now handled through vector dp
- Everything except Loads/Stores can be issued every cycle -- removes need for FuSTs
- 2 bits in packet tell us info about start of new packet and dependencies. 
  - Bit 1: New packet (0) or no (1)
  - Bit 0: Dependencies
  - Ex: 01 means new packet with dependency on what cam before, 00 means new instruction with no dependency on what is before
- Fetch stage has a CAM with instructions coming in 
- Queuing instructions up in decode if things need to wait for a functional unit
- only need FuSTs for load/stores due to variable latency

On Tuesday, we met with the vector core team to learn more about their design and what was required for us to interface with them correctly. 
- Veggie has 4 register banks and special 5th mask register
- Broadcast vector scalar (fp16) and immediate ops
- Vm signal will need to be high so we can tell them to check the mask 
- There are 16 masks and each is 32 bits
- 2 cycles for normal ops, but more in the case that there are bank conflicts
  - this will take longer to resolve
- Writeback happens one at a time
- GEMM now goes through vector ops

Throughout the week worked on updating RTL diagrams to the specifications we discussed. 

Next Steps: 
- Finalize top-level diagrams
- Make significant progress on lower-level diagrams so we can start coding soon
- Meeting with team tomorrow (10/03) to finalize presentation for design review
- Ensure correctness of scheduler core ISA