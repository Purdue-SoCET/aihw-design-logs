# W6 Design Log - Adrian Buczkowski

## State: 
I am currently waiting for the Sunday meeting to discuss my ideas about the preliminary RTL for the non-blocking memory controller.

## Progress: 
This week I created a preliminary diagram to extend the DRAM controller to be non-blocking. My RTL was inspired by source materials my team has shared with me. I do have some questions that will determine the details of the implementation.

## Questions:
-	How exactly does split transaction work for our DDR4?
-	Will we need to precompute completion times for split transaction requests?
-	Are we going to try to reorder requests and track those types of dependencies?
-	What does the bus interface look like for us?
-	Thought: We will need to modify the FSM and add stuff to the timers.
-	Thought: If we keep multiple rows open, we will need a table to track the states of rows. This would also be helpful for the reordering if it happens.

## Post mid-week meeting update:
- After meeting with the team in the middle of the week, I realize most of the questions tat I had at this point were good for myunderstanding, but not crucial to the progress of the project. I was able to confirm the answers with the group.

## Answers:
- Split transaction (non-blocking) is basically just pipelining independent commands withing the DRAM
- We probably will not need to do this (things should most likely be non-dependent or stay in order)
- We will not be doing reordering at the moment, non-blocking is complicated enough
- We have an AXI bus interface mostly specified
- We will need to modify almost everything in the controller
- We already track the states of the rows

## Conclusion
In the coming week me and the team will rethink our controller architecture to match the newest specifications. I will scrap my old diagram for now.

