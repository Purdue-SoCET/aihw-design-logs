## State
I am not stuck with anything

## Progress

RTL of signal generator and memory arbiter discussion with Aaryan, discuss about the memory arbiter and round-robin logic with FSM
Finalizing the timing constraint thanks to Aaryan, Jason, Aidan!!!! and finishing the wirting mask, the signal generator RTL

RTL of signal generator: depend on the state and the row conflicted or not and whether we are power up, we will issue the command according to the command 

Writing mask debugging: Ideally we want to reconfigure DDR4 DRAM in such a way that we can issue writing mask, due to specific setup and addresses bit that I lack of, it caused the DRAM not able to perform my write mask as I expected, but I fix and work

TB integrated of DRAM controller partially (initial FSM, row open policy, command FSM and timing control)

## Prove:
-RTL of signal generator : https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/protected_modelsim/src/signal_gen.sv

-Writing mask: debugging image on discord

-TB integrated: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/src/testbench/dram_top_tb.sv (Partial code, the full-coverage is on my mg account)

## Following updates
1. TB integrated of DRAM controller everything with DDR4 DRAM
2. Keep discussing on AXI-bus and memory arbiter
3. Preparing for the design review on Sunday