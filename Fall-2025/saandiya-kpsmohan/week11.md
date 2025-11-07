## State
I am not stuck

## Progress
1. I talked to Haejune on Tuesday (11/4) to get to know more about the Benes network structure and did some work on that.
2. We also are preapring slides for second design review on (11/10 Monday) with Prof Raghunathan.
3. For making the FIFOs in GSAU to SRAM, we found that it is not possible as cacti only allows minimum block size of 64 bytes: https://github.com/HewlettPackard/cacti/blob/master/sample_config_files/diff_ddr3_cache.cfg

# Evidence of Progrss
## Shifting network - Benes
So the order for the shifting network to work would be:
1. Feed the permutation order into cbg_benes: https://github.com/Purdue-SoCET/atalla/blob/scratchpad_main/rtl/modules/common/xbar/cbg_benes.sv
2. Use the control bit output from cbg_benes and input the actual input array to do permutation for benes_xbar: https://github.com/Purdue-SoCET/atalla/blob/scratchpad_main/rtl/modules/common/xbar/benes.sv
3. benes_xbar will output the final permuted array

- Note that right now, the benes_xbar takes 9 cycles and the cbg_benes takes 1 cycle. But in the future, cbg_benes will be pipelined because for 1 cycle the critical path is too long.  
- Also, the Benes network now only works for N = 32 array, which is what we are using to construct the Toeplitz. 
- We need to support shifting 16 bit width of 32 elements both left and right.  
- The permutation orders are hardcoded into the cbg_benes, so we will store all the possible combinations in a read only memory (ROM) using flip flops for now. There might be a way to optimize this table by combining entries. For example, for shift amount 13, we can use entries for shift amount 1,4, and 8.
- The permutation array will look something like [7, 8, 3, 4, …] this means 7th input will end up in i=0, 8th will end up in i=1, etc, assuming LSB on the left.  
- All possible permutation orders are generated here: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/perm_gen.ipynb
- The testbench for Benes is here: https://github.com/Purdue-SoCET/atalla/blob/scratchpad_main/tb/unit/common/xbar/benes_full_tb.sv
- We just need to hardcode the permutation orders.
- More info on the permutation orders can be found here: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?tab=t.87ak068hn4zr

## 2nd Design Review
- We are preparing slides for the 2nd design review.
- Slides can be found here: https://docs.google.com/presentation/d/1Zvsp4IP0i2unWWiJ6kCAU7zrRmTwQtLhmXGO6vBT3G8/edit?usp=sharing
- The contents to be included are:
1. Overarching design - what, why
2. Pivot from TCA to GSAU - why - swizzle, xbar stuff, details of how it didnt work/work
3. Get PPA numbers - from synthesis
4. (Estimate) numbers from vector core and sys arr
5. How conv and gemm should be used 
6. Mention ISA instructions 
7. Include iterations of adder and multiplier
8. Next steps
- The presentation is 17 mins & 3 mins Q&A

## Future Plans
1. Work on the slides.
2. Integrate GSAU with vector core.
3. Finish ROM for Benes network.
