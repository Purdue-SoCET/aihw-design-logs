## State
I'm not stuck with anything.

## Progress
* 2nd design review completed
* Updated state transition to
    + Fix always worst case latency for writes
    + Fix refresh request while precharging going on
    + Fix always worst case latency for activates
* All code changes can be found on my [github branch](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv)

## Why need to update the state transition?
* Worst case latency assumed for Writes
    + ![WRITE->PRECHARGE error](./images/week%2012/write_to_pre_error.png)
    + WRITE -> WRITE = tWL + tBURST
    + WRITE -> READ = tWL + tBURST + tWTR
    + WRITE -> PRECHAGRE = tWL + tBURST + tWR
    + Current state went to IDLE after WRITE. So, it had no way of knowing which of the above 3 time to select after going to IDLE
    + Incured the highest latency even for row hits (tWL + tBURST + tWR). Worse performance if row hits are to the same location because there's no overlapping with other requests for non-blocking controller

* Failed to handle refresh requests while precharging
    + ![Refresh request while precharge](./images/week%2012/rf_while_pre.png)
    + ![Refresh request while precharge error](./images/week%2012/rf_while_pre_error.png)
    + PRE is issued for 1 bank for row conflicts, PREA is issued for all banks for refreshes
    + After precharging is done, current design did PRE->REFRESH if refresh request received. However, this request was received after the PRE command was issued and not PREA (all banks)

* Worst case latency assumed for Activates
    + In the ACTIVATE state, the following counters were loaded
        - ACT -> READ/WRITE = tRCD - tAL
        - ACT -> PRECHAGRE  = tRAS (for refreshes)
    + After activating is done, current design did ACT->PRECHARGE if refresh request received. However, this request was received after the ACT command was issued with the lower time (tRCD - tAL)
    + So, current design assumed worst case latency for Activates (tRAS)

## How new state transition solves the problems
* ![Update Command FSM](./images/week%2012/updated_command_fsm.drawio.png)
* Writes
    + On a WR command, the highest time (tWL + tBURST + tWR) is loaded
    + There are now 3 flags, tWRITE_done, tWR_done, tWTR_done going high at appropriate times
    + Once write completes, it stays in the WRITING stage. It now knows the current state and can choose the appropriate flag for the transition

* Refresh while precharging
    + Checks refresh request while issuing PRE/A command
    + Now does PRE -> PRECHARGING_ALL for refresh, PRE -> PRECHARGING for conflicts
    + The separate states help distinguish the request being served

* Activates
    + Similar to Writes, highest time load on ACT command
    + 2 flags tACT_done and tRAS_done
    + Check the flag after activation complete for the correct transition

* Other notes
    + Like writes, Reads also stay in the READING state upon transition
    + Refreshes handled only in the ACTIVATING, WRITING, and READING states
        - If handled while issuing the requests, we would have to account for the time to PRECHARGE transition and add additional wait logic
        - Not necessary since refresh allows leeway
        - Addtionally, refresh request interval setting already set to account for this. Check [week 4 log](https://github.com/Purdue-SoCET/aihw-design-logs/blob/main/Fall-2025/dhruv-khatri/week4.md)

## Future plans
* Add the performance metrics
* Check setting of MR registers in the initialization