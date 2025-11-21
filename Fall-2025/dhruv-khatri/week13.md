## State
I'm not stuck with anything.

## Progress (Technical progress little less because of poster/final presentation and 565 PA aissgnment)
* Controller RTL is complete. No major changes should be needed except checking the MRs in the initialization
* Performance metrics captured
* Completed [poster presentation](https://purdue0-my.sharepoint.com/:p:/g/personal/khatri12_purdue_edu/ERJcejGcZClEjonheBk5-_ABRHwRc9x-Y3Tx-bW1ig75bw?e=U9C2Ps) for Purdue Undergradute Fall 2025 Research Expo
* Completed SoCET [final presentation](https://purdue0-my.sharepoint.com/:p:/g/personal/khatri12_purdue_edu/EbXqKhA3ksBHk-aYS7zTROUBDCCOpFNsAgxMCNt5N9y2gA?e=I5XrT1)
* All code changes can be found on my [github branch](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv)

## Performance metrics
* As a preliminary test for the updated design, ran 1M test of the random case already present and passed without any errors
* Tested with a Micron DDR4 simulation model running at 1333 MT/s speed with 32-bit data bus. Peak bandwidth = 5.33 GB/s
* 100K sequential (row hits), non-sequential (row conflicts), and random accesses done to get best-case, worst-case, and average-case bandwidth. Test cases added by Tri
* Following data bus utilization and bandwidth achieved
    + Best case = 7.39 % / 0.39 GB/s
    + Average case = 2.48 % / 0.13 GB/s
    + Worst case = 1.96 % / 0.10 GB/s
* Tried with 10K and 1M tests as well. Since the controller is blocking, bandwidth numbers were the same
* <10 % utilization even in the best case. Non-blocking design update should fix this

## Future plans
* Still check setting of MR registers in the initialization
* Start final documentation