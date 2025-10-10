## State
Maybe I stuck something with AXI-bus, but I'm not sure yet

## Progress
Fixing issue of test3 case (Passed)
The issue is writing mask again!!!!, there are 1 signal that causing the random bit, but I fixed it and it looks fine as I believe and right now the current verification is write -> read -> write -> read of same address but the 2nd transaction will indicate we are write mask to prove that write mask is happened, but currently stuck in WR state behave weird after I change a certain way of my tb that I havent had chance to fix yet, but look into it

Helping the team to finalize the the DDR4 non-blocking request (just helping them to finalize and told them what modules they should keep and what modules they should change for the non-blocking dram). I like our idea, but need to considerate trade-off, queues in write, read? 16 bank queues????? that's a lot and where would we use CAM in AXI-bus and DRAM controller???? I will update that on Sunday, Sooraj

AXI-bus RTL with queues but I will discuss more on Friday with Aaryan and Aakshath about something then I will design in detailed with Aaryan




## Explain verification: 
Integrate with DDR4 DRAM, writing classes, and such and perform test
1. Initialization - Test1 (Passed)
2. Refreshing independently - Test2 (Passed)
3. Writing and loading at the same address (row hit) - Test 3 (Passed)
4. write -> read -> write -> read - Test 4 (Failed) ??? (the whole thing, I will take a look)

## Prove:
- dram_top_tb.sv: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/protected_modelsim/tb/dram_top_tb.sv (still this one)

- RTL AXI-bus: DRAM_contreller draw.io

## Following updates
1. Continue on testing
2. Hoping to finalize AXI-bus RTL in detailed