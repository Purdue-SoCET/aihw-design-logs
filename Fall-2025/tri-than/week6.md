## State
I am not stuck with anything

## Progress
Integrate all the modules with DDR4 DRAM
Have some issue with timing during data transition, but fixed it temporaried (the tBURST that we recorded is off by 2 cycle, which is interesting)

Discussed about the non-blocking DRAM and search some ideas about DRAM DDR4 non-blocking requests (The document is not old !!!!!)


## Explain verification: 
Integrate with DDR4 DRAM, writing classes, and such and perform test
1. Initialization - Test1 (Passed)
2. Refreshing independently - Test2 (Passed)
3. Writing and loading at the same address (row hit) - Test 3 (Failed)

## Prove:
- dram_top_tb.sv: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/protected_modelsim/tb/dram_top_tb.sv




## Following updates
1. Meeting with the team to discuss about non-blocking dram memory request
2. Fixing the verification of the top level
3. RTL AXI-bus discussion and and detail of it with Aryan