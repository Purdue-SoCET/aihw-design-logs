## State
I'm not stuck with anything.

## Progress
* Listed a few performance metrics which will be useful
* Initial fix for random time delays being added in the timing controller to meet requirements
* All code changes can be found on my [github branch](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv)

## Possible performance metrics
* Maximum throughput
    + Can be measured using sequential accesses which will result in maximum row hits and interleaving
    + Sequential reads - for max read bandwidth
    + Sequential writes - for max write bandwidth

* Minimum throughput
    + Row conflict on every access
    + Gives the worst case minimum bandwidth

* Realistic throughput
    + A stream of random reads/writes, which will lead to row conflicts
    + Can set a % of reads vs writes
    + May not be accurate representation for an AI accelerator which does sequential access
    + As a work around, blocks of reads/writes can be random, but addresses within the block can be sequential

* Average latency
    + Can measure average read/write latency after the command is issued

* Time spent in each state
    + Ex - time spent in ACT, PRE, REF, vs data transfer
    + Will measure command overheads
    + Can help measure improvements to Refresh policy
        - Currently I satisfy refresh requirements by reducing the time from tREFI by the amount current refresh goes over. Check [week 4 log](https://github.com/Purdue-SoCET/aihw-design-logs/blob/main/Fall-2025/dhruv-khatri/week4.md) for more details

* Real workloads
    + Take some memory access pattern for a real AI model and benchmark against that

## Issue where some delays had to be added
* A few timing parameters are set in the initialization state with the mode registers
* Currently, the mode register settings are set to the same value as the Micron TB. Timing parameters target one particular speed, need to change those for a different speed
* Tried a small fix for  delays in the timing control with the following changes (discussed in [week 10 log](https://github.com/Purdue-SoCET/aihw-design-logs/blob/main/Fall-2025/dhruv-khatri/week10.md))
    + Since the clock was being set to 1500, I set the speed to 1333 MHz
    + AL was being set to 0 in MR1. However, it was 1 in dram_pkg. I changed it to 0
    + I used my timing control module with the original logic and without the additional delays
    + The first write and read test pass without any errors. To verify, I tried subtracting 1 from all ACT, READ, and WRITE time loads and it showed an error
    + For some reason tCK violations also don't show
* Still need to check if MRs are being set correctly in the initialization

## Future plan
* Check the MR loading in the initialization for correctness
* Implement the performance metrics capturing (will mostly be counters)