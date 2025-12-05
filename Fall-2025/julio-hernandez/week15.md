## Project Update

### State: I am not currently stuck or blocked.

### Progress
1. Week 14 was skipped due to Thanksgiving.

2. Attended Tuesday meeting where the wrapping up of the scratchpad was discussed. The final task would be to verify the entirety of the scratchpad.

3. Went back to the backend testbench to increase coverage of the test. More addresses and stalls were tested for this purpose.

4. Work began on instantiating the entirety of the scratchpad. There were some minor bugs such as incorrect importing of the pkgs, and the swizzle wasn't able to detect a size 0, in our case size 0x0 would mean a 1x1 matrix, so the condition was changed from < to <=. With this out of the way it should be possible to begin writing test for the scratchpad as a whole.

### Next Steps
1. Finish testing the scratchpad.

2. Create a coverage report for the scratchpad.

3. Finish writing the report.

