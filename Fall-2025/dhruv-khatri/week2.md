## State
I am not stuck with anything.

## Progress
Started the implementation of the blocking DRAM controller architecture designed last semester. Nothing too technical, just added a few package/interface files and updated the address mapper based on the new interface.

Following updates were made:
1. A dram package file like the cpu_types in 437. It has parameters for changing the DRAM config like word size, timing, x4, x8, x16, etc.
2. The address mapper and timing signal interfaces, as the name suggest, define the signals decided in the RTL diagram.
3. The address mapper is updated with the new interface. Not tested yet.