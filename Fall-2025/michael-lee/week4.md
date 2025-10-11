# Week 4
## State: 
I dont't need help with anything

## Progress: 
- Project was overhauled to simplify scheduler architecture to match scheduling for GPU team
- Most out of order execution pushed to compiler team 
- Project still needs ISA changes to be implemented, register changes to variable size matrix operations, branch and jump handling for new packetized instructions
- Scoreboarding is no longer necessary, still have issue queue but will no longer have any register/data dependencies
- Simplifies project since existing register status tables (RST's) are now obsolete since compiler guarantees non dependent instructions
- Functional unit status tables still necessary and can still be executed out of order to increase functional unit utilization
- Issue queue will remain along with age logic, and hazard detection
- This week we presented our hastily revised project pitch to the team leads and professor Johnson
- Tentatively responsible for branch and jump handlinjg but subject to change due to recency of project change
- Will continue understanding new ISA with given ISA card

Changes
- No more gemm controller functional unit anymore, everything handled through vector 
- Everything except vector (mem) and scalar load/store can be scheduled every cycle (which means no need for a whole status table ig)
- For matrix load/store it would justbe one cycle because they had buffers, slightly different for sclara load/store, use to have to leave - it high until it’s read
- Fetch holds instructions and schImm[2:0] is the 2 bits that tell us info about start of packet and dependencies  
- In 64 bit instruction
- bit 1 of instruction to see if it is a new packet or not
- bit 0 tells us if this packet can go if the previous one isn’t finished (do i need to wait until previous is finished or not)
- Ex: 01 means new instruction with a dependency on what is before, 00 means new instruction with no dependency on what is before 
- Fetch stage has a CAM with instructions coming in (we only store the 2 bits?)
- Vector core has 2 parts (kind of): 
- Vector L/S (Mem access) and vector computation
- Wait until everything is empty to send through an instruction with dependencies (01)
- We only need fusts for load/stores now to check dependencies since variable latency (everything else is fixed latency)
- Queuing things up in decode if things need to wait (need to figure out depths of the queues for loads and stores)
- Branches Will come somewhere that allows something to come after it

## Next Steps:
- Redo diagramming accounting for new changes to the ISA via packetized instructions