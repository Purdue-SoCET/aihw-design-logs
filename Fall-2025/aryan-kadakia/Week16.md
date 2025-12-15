# Week 16

## State
I am not stuck with anything. I would like to spend time viewing the blocking RTL code and testbench along with understanding the DDR simulator model.

## Progress:
This week, during the weekly AI Hardware meeting (12/7/25), the DRAM subteam and myself completed compiling all resources and structuring a layout for the final report. I begin writing my sections starting with an introduction specific to the split-transaction bus. I disscussed that we want to optimize to initial memory controller to be nonblocking controller and to do that, the currect bus is not feasible as if one unit is nonblocking, all units must be nonblocking in the path which motivates the need for a split-transaction bus. 
I then, in depth, wrote on design choices and the microarchitecture for the split-transaction bus and displayed all the work and contribution I made. I then discussed about my verification plan. I ensured this was detialied as this is what I will follow next semester when I implement the bus. I disscussed how I want to test with the already confiugured and tested DDR model and also explore the ramulator simulator.

By Wednesday (12/10/25), I completed writing and proofreading my sections. On Thursday (12/11/25), the DRAM sub-team and myself met to finalize the report. We went through all sections and proofread everything. We spent time formating and ensuring all points were hit and everything is detailed and explained. Once this was complete. we all did one final read through to agree the report was finalized. Then on Friday Morning (12/12/25), we went to the Knowledge Lab in WALC library to print our final copy of the report and bind it. Once this was complete we were able to submit it to our team lead, Sooraj.

# Future Steps:
At this point, no work in regards to the AXI-bus will be done this semester so I can focus on my final projects and exams. During winter break, I plan to write the RTL code for the full bus and begin testing as next semester begins. My hopes for next semester is that I can develop a version of the bus that can be integrated and tested.
