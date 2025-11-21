# State
I am not stuck

# Progress
## 2nd Design Review
1. We presented 2nd Design Review on Monday (11/10) with Prof. Raghunathan.
2. He recommended us to keep in mind of the other things that are in flight in the core when looping convolution instructions.
3. Other than that, everything went well.

## Evidence of Progress
1. We are preparing for the Poster Presentation on Tuesday (11/18): https://docs.google.com/presentation/d/1o10fFUSrwAOHQQAT6hTaaKTaAlK-VAW9MFQxh1um3-U/edit?usp=sharing
2. We are preapring for the final VIP Presentation on Wednesday (11/19): https://docs.google.com/presentation/d/15GcSIGnWCmo2z_06MPa4LrzrltFY2QFBZBuB7Gaxv4w/edit?usp=sharing
3. During the Vector Core meeting (11/12), we discussed several things:
  - For integration, we are not pushing to main branch anymore because of PRs, we have a new branch off main and we are pushing codes there: https://github.com/Purdue-SoCET/atalla/tree/vector_core_fa25
  - We also need to model a top level testbench for vector core, that models scratchpad, writeback, scheduler, and systolic array.
  - We need to aim to run at least a 64x64 conv tile.
  - We also need to write test vectors/kernels to test the vector core.
  - There is a couple of things assigned for me to do:
      - I need to research about the convolution library - I need to ask more details from Jing.
      - I also need to research if there is a better way to do convolution than Toeplitz, now that we have a vector core.
  - For the final report, I should include:
      - Suggestions for the next convolution team.
      - Potential things to look into for potential gain.
      - Is there a need for a specific compute unit for toeplitz or using vector core is still better?
  4. I also came up with the list of all permutation orders we need for the Benes network for Nikhil to create a LUT: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/perm_gen.ipynb
   
# Future Plans
- Research on convolution library.
- Research on better ways to do convolution than Toeplitz.
 
