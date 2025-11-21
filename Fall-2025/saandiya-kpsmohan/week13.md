## State
I am not stuck

## Progress
1. Poster Presentation - 11/18 (Tuesday): https://docs.google.com/presentation/d/1o10fFUSrwAOHQQAT6hTaaKTaAlK-VAW9MFQxh1um3-U/edit?usp=sharing
2. Meet with Jing - 11/18 (Tuesday)
   - I discussed with Jing for a strategy to come up and verify the Convolution Library
   - We also discussed how to do masking, shfiting and adding. Masking is done explicitly because Atalla doesn't have thread ID.
   - My goals and timelines also have slightly shifted and I have documented my strategy, flow, and things I can get done by this semester.
   - https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/atalla_conv.md
3. VIP Presentation - 11/19 (Wednesday): https://docs.google.com/presentation/d/15GcSIGnWCmo2z_06MPa4LrzrltFY2QFBZBuB7Gaxv4w/edit?usp=sharing
   - A question was asked by Cole that if we ever considered RISCV matrix instruction. Ans: The instructions arre already decoded so we don't care.

## Evidence of Progress
1. I have come up with the golden model in Python as per one of the strategies listed. This is to verify the C code.
   - https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/myenv/golden_model.py
2. I am also currently working on the CPU version (C Code) for the Conv library.
   - Header file: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/conv_lib.h
   - C implementation of input tiling, kernel tiling, toeplitz generation: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/conv_lib.c
   - Main file for testing/output: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/main.c
   - These are still work in progress.
  
## Future Plans
1. Finish the C code naive implementation before thanksgiving as per my timeline. Optimizations for stride, kernel, padding and dilation will be done as per the timeline as well.
2. Come up with Atalla specific code.
