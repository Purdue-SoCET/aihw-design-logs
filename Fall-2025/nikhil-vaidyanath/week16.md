## State: I am not stuck with anything, don't need help right now.

## Progress
   This week had a LOT of work due to the report (shoudn't have procrastinated this much lol).

   In the Sunday meeting (12/7), I attempted to get my unit checked off with Jing and clarified a couple of things with others. I got a conditional check off, with all the functionality being correct, but the valid/ready protocol not being exhaustive enough. I was told to add more test cases ensuring that on a single clock pulse of valid/ready my unit would act as expected. I worked during the week to add the testcase, also updating my Makefile to a .f based approach so that when I push my code the file formats and folder structure is not disrupted.

   On 12/10 I met with Jing and got the unit checked off. Additional notes here are that it's possible to use pipeline latches within the unit along with the valid/ready protocol to squeeze a bit more performance because if a unit was not issued to every cycle it has gaps of non-valid data within the pipeline which can be shifted out when ready_in is low allowing the unit to not immediately stall the scheduler.

   I started work on my sections of the report (just shifting unit and GSAU for now, but will be more sections once I meet with Vector Core). In the Wednesday meeting (12/10), we were told to stop working on technical work altogether which I think was a surprise since we wanted to get top-level integrated by the end of the semester. This was a mistake on our part, we should have notified the GTAs that top-level would not be completed earlier, and dedicated 110% effort on the report.

   On Thursday I met with Vector Core where we spent a majority of the night on the report. I gave numerous comments to others on their writing and did many various sections that weren't covered by others. On Friday I made some finishing touches with Joseph and Vedant, and we printed, bound, and submitted the final report (yay!). 

   While we did work on this later then we should have, we believe we submitted a report that gave sufficient detail on the why and what for Vector Core as a whole and for each of our units themselves.

   Code (all related modules are located in this folder): https://github.com/Purdue-SoCET/atalla/tree/vector_core_fa25/rtl/modules/vector

   Final Report: https://docs.google.com/document/d/1_8fxII3308U6oHTUsFgIpE2MNWtf03bf1tetJ6z-sRA/edit?usp=sharing

## Tasks
    Next steps include:
     next semester work on making 3 new systolic arrays.

## Future Plans
   Next semester stuff.