> This week was focused on completing the Design Review slides, and synthesizing different versions of the crossbars. 

## State

[STALLED] Waiting on Backend cleanup from Julio. 

## Arch Updates
[NONE]

## Progress
- Check out the [Synthesis -- Atalla](https://docs.google.com/spreadsheets/d/1_Gi4uXS2h3LPqtJLWhsDoud7xXXNh3VplB5GbnDfr48/edit?gid=0#gid=0). 
    > Highlights: We will go with a 1024 ROM + Benes, or a Batcher (3 cycle), or a 32-entry RAM + Benes. CLOS is being explored by Haejune as of now. 
- Interesting discussion on how we can perform transpose using scratchpad. 
    > Question: Can we utilize the Scratchpad to perform a transpose operation on some tile in the DRAM and store it into memory. 
    > Answer: Yes. Remember how swizzling happens? Moreover, Backend loads it data using the Swizzler and row_id++ increments. Similarly, when storing if we just make the Backend do col_id++ increments, we'll be done with transpose! Just use SDMA.ld and SDMA.st! 

## Future Plan
- Get onboarded onto Compiler's workflow. 
- Decide programming model.