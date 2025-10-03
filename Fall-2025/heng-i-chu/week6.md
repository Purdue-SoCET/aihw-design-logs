State: I am not stuck with anything, don't need help right now. 

## Progress
This week we have been working on the isa mapping of intermediate representatives for all scalar instructions. We have somehow found a way to parse the IR  (which we are currently able to generate) into specific function calls that are yet to implement. We have finished all R types, I types, J types, U types and halt instructions. At the same time, we are also able to store the function tokens from the IR into an execution list. This ensures that the sequence of parsed operations can be executed in order. 

For the problems about FPs, initially we thought it stands for "floating point". So we tried to remove all "fp" instructions and instances in the entire compiler as our vector core currently does not support floating point operations. However, we later found that the program crashed because FP stands for "frame pointer", which is essential for saving function stacks.

# Next Week
- Finish the instruction mappings and tokens
- Finish J type instruction address calculation functions
- Understand how program stacks and activation records work in PPCI
- Start dividing jobs in dealling with packetization issues
- Try to get all scalar instructions architecture done
