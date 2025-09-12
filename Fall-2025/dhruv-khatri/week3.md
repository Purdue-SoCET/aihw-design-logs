## State
I am not stuck with anything.

## Progress
Completed the testing of the address mapper module written last week. Also, started implementation of the timing control module, with emphasis on verifying all the timing requirements.

More on the Address Mapper (Reach destination faster):
1. As decided last semester, the mapper follows Ra-R-B-BG-C mapping. Since the accelerator is expected to access large number of continuos memory locations, the mapping allows for efficient interleaving. Since columns will be access most often, the lower bits are used for columns. BG are places between/end of the columns to switch BG for each column accessed. And so on for the heirarchy of DRAM.
2. Initially, 512Mb versions of x4, x8, x16 are mapped and are intended to be used for testing. Once these single versions are verified for correct operations, the aim is to add mapping for all other configs are intended for final integration.

More on the timing control (Not too late, not too early. Just in time):
Verification of the timings requirements is crucial for correct operation. Implementation is more or less counters loaded with different values based on the command being sent.
1. For ACT command
    a. ACT -> PRE = tRAS
       ACT -> Read/Write = tRCD - tAL (AL is 0 if not set)
    b. The following timing requirements are not include because they assume consecutive commands. The current controller version serves only 1 request at a time.
        i.   tRRD for consecutive activates
        ii.  tFAW for 4 consecutive activates with tRRD_s? (Need to check if only tRRD_s or tRRD_l as well)
        iii. tRC for ACT -> ACT / REF commands to same bank   
2. Timing for other commands needs to be verified and added.
