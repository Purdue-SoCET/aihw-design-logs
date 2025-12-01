## State: I am not stuck with anything, don't need help right now.

## Progress
   This week had many presentations, and thus less unit related work. (Some of the work for this log is work done during Thanksgiving week).

   On 11/16 I attended the Sunday meeting where I continued work on the shifting unit. I've had some difficulties with the lack of a standard Makefile and have been using Akshath's version which requires many changes to the folder structure. There were also some difficulties related to differences between main and other branches. I have talked with Akshath and Haejune to find latest versions of Benes and related files (that are verified).

   On 11/18 we had the poster presentation, so some time before that was spent on the poster creation. We ran our poster by Malcolm and made some edits. Because this event had many in audience who aren't very knowledgeable in our field, we prepared explain to that level, using examples like ChatGPT and explaining how specific hardware can do inferencing very quickly and efficiently.

   On 11/19 we had the senior design/SoCET presentation. We used much of the skeleton/content from earlier presentations (Design Review 2), adding more for the further progress and additional insights into tiling and other theory (since not every GEMM is less or equal to  32x32). 

   On 11/19 we also had the vector core meeting where we discussed where the shifting unit is at and details of the final report.

   I also worked further on the shifting unit, getting it to successfully simulate with the Makefile and making a testbench with some LLM prompting. Further work needs to be done to verify it as currently it's not behaving as expected.

   Some things I noticed along the way:
   1. The single cycle wrapper also instantiates the cabbage single cycle, so shifting unit must act as a wrapper
   2. Register mask needs to be set to 0 (I think this should be documented better) to make benes combinational
   3. I need to reverse the control bits to make them correct for the benes, I've done this in the ROM data svh instead of comb logic as there's no need for that logic to be synthesized

   Note: sv source files are not pushed yet because I have made lots of changes to the folder structure to make it simulate correctly with all dependencies. If I were to push it the structure would be inconsistent compared to the rest of vector core. I will push (and include links in design log) once verified.

   Poster: https://docs.google.com/presentation/d/1o10fFUSrwAOHQQAT6hTaaKTaAlK-VAW9MFQxh1um3-U/edit?usp=sharing

   Senior Design/SoCET/VIP Presentation: https://docs.google.com/presentation/d/15GcSIGnWCmo2z_06MPa4LrzrltFY2QFBZBuB7Gaxv4w/edit?usp=sharing

## Tasks
    Next steps include:
     Finish verification of shifting unit
     Work on final report, detailing GSAU and especially the logic for our decisions and transition away from the TCA
     Investigating SRAM config for simulating area for small block sizes w/ cacti (in the backlog now as 437, final report, and finals are ramping up)
    Deadlines:
     Final Report - 12/19 @ 5 PM

## Future Plans
   As the end of the semester is approaching, I believe I and the rest of the team have built a decent amount of reference material and such. Hopefully, other teams in the future will find these helpful and I may spend some time touching things up for future students. If I were to work in the same team next semester, I will use these to make the presentations and such much quicker to give more time to project work.