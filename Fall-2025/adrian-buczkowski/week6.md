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
