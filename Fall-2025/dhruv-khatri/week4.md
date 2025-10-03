## State
I am not stuck with anything.

## Progress
Completed implementation and verification of all command timings except REFRESH. The REFRESH timings are implemented but need to be verified.

## More on the REFRESH logic (Just press F5)
The REFRESH command needs to satisfy 2 requirements:
1. Avg time between 2 refreshes be tREFI.
2. Maximum of 9 * tREFI by pushing or pulling up to 8 REFRESH commands.

I satisfy 1 by reducing the time from tREFI by the amount current refresh goes over. Example:
tREFI = 100
rf_count = 110
So, next rf_limit = 110 - 100 = 10

However, I may need to add the case of having a forced refresh when the time reaches 9 * tREFI - (time to read/write + time to precharge). A counter will be needed to store the number of consecutive refreshes to done (8 in this case).

## Small notes on the timing counter 
1. The counter is a count-down timer.The value to be loaded is provided for only 1 cycle. So, the counter latches it and counts down. The done signal is high when the counter reaches 0.
2. The counter takes 1 clock cycle to start counting. Hence, it loads (time_load - 1).