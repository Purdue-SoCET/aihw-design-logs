# Week 6
## State: 
- I do not need help 

## Progress: 
- Diagram for packetized instructions and full crossbar created
- Diagrams at https://drive.google.com/file/d/1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu/view?usp=sharing
- Meetings with vectorcore team to flush out width of execution units and cycle time guarantees
- Primary issue for packetized instructions is stalling for multiple issues to same functional unit
- We have fixed latency guarantees from all of our functional units other than load/stores
- we also have guarantees that the functional units are pipeline so that we can issue an instruction every cycle

Vectorcore
- Veggie banked special 5th mask reg
- Vector Controller? Check lengths 
- Control Signals: Vector_types.vh -> Control_t
- We do broadcasting for vector scalar(fp16) or immediate ops
- Vm = 1 when we need to tell them to check the mask
- 16 masks each mask is 32’b 
- Vm for veggie has index
- If vs2_ren then must be imm or scalar(fp16) op
- 2 cycles for normal operations ++ for bank conflicts
- Need fust for all vector ops???
- Writeback is one data at a time
- For now implement counter may replace with ready signal
- First value of vector for scalar to fp16
- Wait for timmy/souraj about mv vector to scalar or fp16 to scalar
- GEMM is now vector ops


## Next Steps:
- Ask Sooraj and Rishi about design changes and how predication