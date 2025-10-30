## State
I don't need any help

## Progress
Finalizing the top level integration of blocking dram controller with Dhruv and Sooraj to ensuring the blocking verification meet expectation. After discussion, we agree upon moving to timing configuration issue of DDR4 DRAM (figuring out a way to set up the speed of the DRAM clock and changing the DRAM timing constraint from there). Debugging the synthesis issue (Solved thanks to Akshath and Sooraj)

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