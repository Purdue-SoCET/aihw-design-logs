> This week was focused on finishing the Benes + ROM and CLOS Synthesis. Also uploaded a more complete emulator for the Scheduler team! 

## State
[STALLED] On Haejune for CLOS. 
[STALLED] On Julio for the Verification.

## Arch Updates
We've explored the option of having a ROM next to the Benes, instead of the Cabbage.
    - The single-cycle Benes is the [smallest design](https://docs.google.com/spreadsheets/d/1_Gi4uXS2h3LPqtJLWhsDoud7xXXNh3VplB5GbnDfr48/edit?usp=sharing) we have, and fast enough for our needs. To operate it however, we needed a large ass cabbage unit, which in itself is 10x Benes area. 
    - So, I ran some tests on the emulator, and found that only 1024 unique permutations exist when we are writing and accessing over 1x1->32x32 tiles. 
    - To ensure this is indexable, I had to guarantee all the (base_row, row_id/col_id, num_rows, num_cols) mapped to [unique indices in said ROM](https://github.com/Purdue-SoCET/atalla/blob/scratchpad_main/rtl/modules/common/xbar/controlbits.mem).

## Progress
- Reviewed Saandiya's convolution kernel code. Looks a-ok. 
- Edited the [Swizzle RTL (SHA-3ec499b9376d0)](https://github.com/Purdue-SoCET/atalla/blob/scratchpad_main/rtl/modules/memory/scratchpad/swizzle.sv) and the [Emulator code](https://github.com/Purdue-SoCET/atalla-sim/tree/master/sim/components/scratchpad).
- Working on the Scratchpad [Final Report](https://docs.google.com/document/d/186o7OMmD8pstcT0LBeVNRixO5y7Undeff-K4Qaho2tY/edit?usp=sharing).
- Finishing synthesizing [CLOS](https://docs.google.com/spreadsheets/d/1_Gi4uXS2h3LPqtJLWhsDoud7xXXNh3VplB5GbnDfr48/edit?usp=sharing) on MITLL90nm. 2x Benes size, 2x Clock Freq, 4nW less power. As long as the Benes + ROM is smaller, we'll keep this as the 2nd choice. 

## Future Plan
Focusing purely on writing the Final Report. 