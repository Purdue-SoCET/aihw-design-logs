## State: I am not stuck with anything, don't need help right now.

## Progress
   During the week I helped on slides for the Design Review 2 with prof Rangunathan. We need to get sufficient detail on how we're implementing the operations and the changes from the TCA to show the full scope of the work. Saandiya mostly handled the TCA slides as she's much more familiar with how that functioned. I made some additional diagrams and diagram changes to better fit the presentation like the shifting unit and a zoomed in diagram of where it connects within vector core.

   On Sunday (11/9) I attended the Sunday meeting. I did lots more work with Saandiya on the slides and which slides we decided to take. I also worked on the control and permutation generation. Saandiya provided the permutation order for Left/Right 0-31 value shifts. After going through contrl bit generation, we come out with 64 total 18 byte sequences (64*18 = 1152 bytes). I did some analysis and had a script made such that I can view all of them side by side. After doing this, I saw two easy optimizations. 

   1. First/Last (depending on ctrl mode or bits) 10 bytes are 0s
   2. Right_shift(n) = Left_shift(32 - n) for all values. I verified this with a script after visually looking at it. 

   The results of these savings are that we can go from ~1.1 kB to ~.32kB of FFs. We do need their outputs as fast as possible so I believe that FFs are needed for this unit. There are potentially more optimizations that can be made (I think last 2-3 bytes follow some sort of pattern), so if absolutely necessary we can make additional changes for better area.

   On 11/10 we presented in Design Review 2 to professor Rangunathan and all the GTAs.

   In the Vector Core Meeting (11/12) we decided to instead of PRing to main and getting a delay of a couple days for a GTA to review, we would make a vector core branch and simply push to that, PRing all changes to main at the end. I made my branch the "vector core branch", and that closed the open PR.

   Slides for Design Review 2: https://docs.google.com/presentation/d/1Zvsp4IP0i2unWWiJ6kCAU7zrRmTwQtLhmXGO6vBT3G8/edit?usp=sharing

   Github Code Links (not simulated or integrated yet):
   https://github.com/Purdue-SoCET/atalla/blob/vector_core_fa25/rtl/modules/vector/rom.sv
   https://github.com/Purdue-SoCET/atalla/blob/vector_core_fa25/rtl/modules/vector/rom_init_data.svh

## Tasks
    Next steps include:
     Creating and integrating ROM into top level shift unit module
     Create testbench and exhaustively verify shifting unit
     Investigating SRAM config for simulating area for small block sizes w/ cacti
    Deadlines:
     Poster Presentation: 11/18
     VIP SoCET presentation: 11/19

## Future Plans
   We will be using much of the same diagrams/slides for the poster presentation for next week and the final SoCET presentation as well.

   (Below text is pasted from last week as it's still the case)
   As for the work itself, we need to wait for systolic array to test the entire Vector Core because now that they are offloaded from vector core, we can't verify any GSAU/GEMM/CONV functionality without it. I believe they will need to overhaul their control signals along with the changes to the adder and multiple for BF16. 