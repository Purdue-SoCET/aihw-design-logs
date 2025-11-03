## State
I'm stuck with trying to change the Micron DDR4 simulation config. Will try until sunday, then move on to performance metrics.

## Progress
* Completed testing the control unit without the Micron model
* Integrated design (both Tri's and my modules) and cleaned up some of the code along the way
* Ran a coverage report for addr_mapper and timing_control modules
* All code changes can be found on my [github branch](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv)

## Completed testing the control unit without the Micron model
* Control unit combines the initialization, row policy, address mapper, command fsm, and timing modules
* The tb follows the same pattern as init_addr_row_cmd tb, only now the timing control modules produces the timing signals
* Tests covered - All tests passed
    + Power on reset
    + initialization check
    + Row miss loop - opening row 0 of all banks for the 1st time
    + Row hit loop - writing to row 0 of all banks 
    + Row conflict loop - reading from all rows expect 0 of all banks. Each loop runs to read completion
* Refresh request not covered
    + Because of the long loops, refresh request popped up in between
    + Loops weren't set to handle these refresh requests
    + So, refresh cases skipped

## Integrated design with Micron model
* All modules integrated in dram_controller_top, with some code cleanup along the way
* Some timing issues discovered by Tri that are solved by adding or removing delays. All for 4G_x8 config
    + ACT -> PRE on rf req should always assumes tRAS (worst case sceneario)
        - If refresh request is received on activating done, we still need to wait tRAS time. However, currently it waits only for tRCD - tAL time
    + ACTIVATING - Time_count_done = tRAS -12 + 1 for meeting micron requirements
    + WRITE
        - time_load = tWL + tBURST + tWR (same as act -> pre) . Need to wait longer if next stage is pre
        - Wr_en should remain high for entire writing to complete (this is fixed)
* I'm investigating the reason for these random delays, and whether or not they conform to the JEDEC standard

## Issues with changing speed of Micron Models
* "tCK SPEC violation" error from Micron model when running the top level tb. A speed was not set, so the micron model seemed to run for all speeds
* Tried settin the speed in micron provided tb with +define+FIXED_2400 command argument (found in the readme.txt file of Micron folder)
* ![](./images/week%2010/speed_set_issue.png)
    + The speed was correctly set to 833 (in ns), but changed to 1250 automatically
    + All the timing parameters are also being set corresponding to 1250 ns
    + Note from micron readme.txt file "Note: Normally the model adjusts in the input tck for timing parameters. This can be fixed
by using set_timing_parameter_lock(). Please see subtest.vh for an example."
    + No mention of the above function in the file. I will try to fix it for a few more days, otherwise come back to it later

## Coverage reports
* Address mapper - 77.77 %. Missing coverage
    + Branches - configs other than x4, x8, x16. All false case should not be possible becaause config has to be 1 of these
    + Conditions - config == x16. Skipped x16 for now because checking with x8

* Timing control - 91.65 %
    + Only major missing coverage is the toggles for the timing counters. I will fix this by adding higher time values (although they may not conform to JEDEC)

## Future plan
* Complete the coverage report for timing_control
* Try to find the way to correctly set config in Micron models (will move on if cannot find by next week)
* Look into performance metrics for the blocking controller

        
    
        

