## State
I don't need any help

## Progress
Finalizing the top level integration of blocking dram controller, but not including the writing burst mask featuring, due to adding extra logic for the referrence model

## Explain verification: 
Integrate with DDR4 DRAM, writing classes, and such and perform test and comparing the the load data with the creating cache referrence model and use the assert + $fatal
() and strengthing the verification progress

Spending 3-4 hours for debugging, following the Micron timing track, and fixing the timing_signals module

1. Initialization - Test1 (Passed)
2. Refreshing independently - Test2 (Passed)
3. Writing and loading at the same address (row hit) - Test 3 (Passed)
4. write -> read -> write -> read - Test 4 (Passed) (row missed)
5. 3 Consecutive writes of different addresses (Passed)
6. Performing 2 row conflicting case (Passed)
7. Performing 16 consecuting writes of different banks (checking the refresh cycles work in consecutative requests) (Passed)
8. Perfoming 1000 random consecutive writing or reading in random addresses (Passed)


## Prove:
- dram_top_tb.sv: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/protected_modelsim/tb/dram_top_tb.sv (still this one)


## Following updates
1. Preparing for exams and interview
2. Hopefully make a report of synthesis