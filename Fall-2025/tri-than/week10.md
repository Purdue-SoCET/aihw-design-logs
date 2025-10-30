## State
I need some help with merging the code into the main branch.

## Progress
My progress this week is purely organizing the code and cleaning the folders so that I can merge with the main code, but I have issues in runnning the makefile (Following the instructions from Askshath as well), but got issues in setting up. So I decide to make a DRAM branch, clean it as attlas format to make it work, so that DRAM teammembers can pull it and use it with DRAM blocking-version.

I move on AXI-bus arbiter RTL design, the arbitration between AXI-queue and Load and Store queue that going to the non-blocking DRAM controller (2-3 hours). Me and Aaryan discussed upon arbitration logic and design choice. We decide to choose the lock requests, meaning we will handle requests 

## Explain Synthesis Report: 
The synthesis of blocking dram controller consists of initial_state_fsm, row_open_policy (Page status check), command_FSM, timing_signal, signal_generator, the integrations of block.

The Flowkit synthesize indicate the blocking dram controller work with 667MHz with Net Area 5662.871 um^2, total area (Cell+Physical+Net) is 18938.212 um^2

## Prove:
- dram_top_tb.sv: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/protected_modelsim/tb/dram_top_tb.sv

-Synthesis report:
1) qrt report (area report) : ./doc/qrt.txt
2) critical path report : ./doc/critical_path.txt


## Following updates
1. Moving to AXI-bus logic
2. Cleaing the DRAM-blocking code and and organized the files