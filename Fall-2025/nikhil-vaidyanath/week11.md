## State: I am not stuck with anything, don't need help right now.

Note: Progress is a bit less this week due to an illness and midterm

## Progress
   On Sunday (11/2) I attended the Sunday meeting. I helped Mixuan synthesize her multipler wallace tree. I spoke with other members of vector core and refined interfaces of where the shifting unit will go, which is from the pipeline latch from Scheduler/Veggie to the WB arbiter which will output the result to WB Buffer and Veggie. I also worked on using cacti to model SRAM buffers instead of the flip flop based FIFOs for register tracking we have for the GSAU. To achieve the most "square" footprint I derived the length and width to be 48x32 (1536 bits). Note, the dimensions can get more square but then reading will not be nearly as easy (could be a situation where we need to read two entries for a single register). When configuring the cacti program to use these values, I ended up getting stuck as the message was "Block size must be at least 64". Assuming this means bytes it would not be possible to model this.

   Later in the week I reported my progress in the Vector Core Meeting. I also spoke with Haejune about permutation generation and how that would work for the shifting unit. He provided a script which I will need to understand and configure to run my specific permutations for left and right. Sooraj also provided me a doc page on using cacti with smaller block sizes so I will look at that and hopefully get to it next week.

   I have started a PR to merge gsau into main branch. I spent some time cleaning up code but more work is likely needed. The link is here:
   https://github.com/Purdue-SoCET/atalla/pull/120

## Tasks
    Next steps include:
     Getting permutation values for shifting unit using Haejune's script
     Getting ctrl bit values based on those permutations
     Investigating SRAM config for simulating area for small block sizes w/ cacti
    Deadlines:
     Design Review 2 w/ prof Rangunathan: 11/10
     Poster Presentation: 11/18

## Future Plans
   Many presentations are next and we're likely to present much of the same items in these presentations, so it's likely helpful to spend a lot of time on making one of these such that we have good talking points and diagrams for the others. 

   As for the work itself, we need to wait for systolic array to test the entire Vector Core because now that they are offloaded from vector core, we can't verify any GSAU/GEMM/CONV functionality without it. I believe they will need to overhaul their control signals along with the changes to the adder and multiple for BF16. 