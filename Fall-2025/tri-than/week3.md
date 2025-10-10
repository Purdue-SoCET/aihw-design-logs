## State
Not stuck with anything
## Progess
Working on command FSM state code and the tb, discuss about memory arbiter blocking request with Aryan, Akshath and Sooraj

Command FSM state code: a blocking command FSM that interact with row open policy, if row hit -> request_state, if row miss -> act, if row conflict -> pre

Creating the testbench of initalization state

Discuss about what the interface look like between scartchpad and memory arbiter/AXI bus, and do we need PHY or nah (Not my problem - nah we do need to take a look of this for tape out issue)

Meeting with team to check the progress, mentioninng them to take over into timing constraint for setting up the non-blocking DRAM controller

Command FSM code: https://github.com/Purdue-SoCET/tensor-core/blob/memory_subsystem_tri/src/modules/command_FSM.sv

initialization state (make sure sequence work): in my mg account (will update in the future, but trust me it's work!!!)



Following updates:
1. Command FSM tb
2. Signal generator RTL design
3. Finishing writing mask because of designing the flexibility of writing in ele number (even though that would waste the bandwidth but that's okay)