## State
I am not stuck with anything.

## Progress
* Discussion with Prof Swabey about PHY and tapeout
* Initial discussion with the team for the top-level RTL diagram of the non-blocking MC
* Continue the integration testing of the control unit from last week. I missed my goal of finishing the control unit testing this week

## Discussion with Prof Swabey about PHY and tapeout (higher number not always better)
* Using the DFI interface for MC <-> PHY is a good idea for standardizing the communication since it's industry standard. We can use Synopsys/Cadence IP for the PHY to skip the analog part for now. Later, a dedicated team can make a custom PHY but with the same DFI interface.
* For the tapeout don't use the DIMM version of the DRAM that has the 64 bits of data (used in laptops/computers) for the following reasons
    - 64 bits of data means more overall pins for the address as well. Such high amounts of pins makes analog stuff difficult. Instead use a single x16 (16 bit) chip soldered on the board
    - In addition, the DIMM pins create interference even when not in used. More care needed for the PCB design, on top of the already high IO speed of the DRAM
    - DDR4 speeds might be unachievable with the current skills. So a very strong suggestion to SWITCH TO DDR2 WITH SINGLE X16 CHIP

## Initial discussion of 2 designs with the team for the top-level RTL diagram of the non-blocking MC (non-blocking but not reordering. 1 step at a time)
* Separate Store and Load queues with global scheduler
![](./images/week%207/global_scheduler.jpg)
* AXI sub modules 
    - Handle the handshake between the MC and the AXI bus
* Load/Store queues
    - Queue read/write requests from the AXI sub into separate queues
* 2 timing modules
    - Inter timing - For tracking time between sending the commands
    - Intra timing - For tracking time of the command being serviced by the DRAM
* Scheduler
    - Arbitrates between the load and the store queues based on some policy (not decided yet)
    - Takes into account the bank/row conflict (from address mapper and row policy), the intra and inter timings, and the current command state for choosing the next request 
    - Refresh and ZQ calibration are given the highest priority


* Per bank queue
![](./images/week%207/per_bank_queues.jpg)
* A request queue for each bank
* Arbiter
    - Chooses between a request from one of the BQs
* Needs a load/store queue after AXI Sub and before mapping
    - For storing requests that come from the AXI

* Other general notes for both designs
    - Need to discuss the pros and cons of both the designs along with the resource usage
    - RAW/WAR/WAW hazards
        + Should not be a problem because the non-blocking caches should handle these cases to maintain memory consistency
    - Sooraj mentioned CAM may be needed for returning the request to the AXI bus
        + If the index of the requests remains constant in the queue for popping the request from the load/store queue, can we use the index of the queue? Once the arbiter chooses the request, it will also save the queue index of the request. Then we simply use the index to get the other AXI metadata. Cole also suggested a similar table for tracking the request return

## Continue the integration testing of the control unit from last week
* The following cases were tested (reasons discussed in week 5)
    - Init fsm transistions and init_done flag
    - row miss status and corresponding command FSM transitions
    - row hit status and corresponding command FSM transitions

* Fixed delayed init_FSM state transisitons
    - In the init_state FSM, the overflow flag is now set when count = (overflow_value - 1). Because it takes one more cycle to state transition
    - Each init state took 1 extra cycle, so the total extra cycles were ~10

* Fixed row status registering issue
    - The row status tracks the open row in each bank and gives the status whether the new row will be a HIT, MISS, or CONFLICT
    - This status was registered for clock speed purposes. However, it delayed the row status information 1 cycle.
    - ![](./images/week%207/row_status_issue.png)
        + Above is a write request which should result in row hit
        + When dWEN goes high, the row_stat is updated 1 cycle later
        + The command_FSM sees the row_hit and then updates state to WRITE 1 cycle after that
    - Deregistering the issue solved it

## Future plan
1. Add the row conflict status case to the above testbench, then test the entire control unit with the timing control module
2. Generate the toggle coverage report for the address mapper to check it any corner cases emerge (will come back to the module synthesis goal discussed in previous weeks later)
