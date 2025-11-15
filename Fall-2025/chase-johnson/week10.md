## State: I am not stuck with anything

## Sub-Team - Vector Core
The Vector Core is a seperate piece of hardware from the rest of the tensor-core as it aims to focus on processing vector-based instructions. The purpose of the vector core is speed up AI model learning processes and work in conjunction with other pieces of hardware in the tensor core.

## Progress: 
This week I spent my time finalizing the vls unit and the vexp unit in time for the design review but unfortunately both units were not function at time of the design review due to some logical errors on my end. I realized that I had not calculated the taylor approximation correctly during verification and some major logical errors were present. Additionally in the l/s unit most of the signals were metastable and the destination registers were not being popped of the fifo queue correctly. I met with Jing discussed finding the percent error for each taylor series approximation and found that 4 terms would be sufficient for BF16 and 5 terms would be sufficient for FP16. The l/s unit was handed off to Vedant to finish I my main focus now was to work on the exponent unit.



## Future Plans:
- Research New Implementation for Exponent Unit