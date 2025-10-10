## State
Not stuck anything right now

## Progress
Working on RTL coding design of initialize state, row policy open with testbench testing.

Discussing with Dhruv again the general architecture of DDR4 DRAM controller in blocking request, setting up sources of DRAM learning for new members with Dhruv and create the timeline and goal of what to achieve within this semester

RTL code of initialization state, row open policy diagram and code should be in the DRAM controller draw.io

prove and decribe:

initialization state : A sequence of power and configuration of DDR4 DRAM

Code: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/src/modules/init_state.sv

Row open policy: Page track
Code: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/src/modules/row_open.sv



Updates progress:
1. RTL code of initialize state
2. RTL diagram of row open policy
3. RTL code of row open policy and tb 