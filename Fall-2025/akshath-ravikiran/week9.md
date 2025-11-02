> This week was focused on setting up Flowkit and the rest of the codespace for the AI HW team to work on together. Also synthesized Batcher and Benes to find their clock and area. 

## State

[STALLED] Waiting on CBG from Haejune
[STALLED] Waiting on Backend Verification from Julio

## Arch Updates
[NONE]

## Progress
- Check out the new [main branch](https://github.com/Purdue-SoCET/atalla/)! 
- Created a guide on using [Flowkit](https://github.com/Purdue-SoCET/atalla/blob/main/docs/synthesis.md), and what people have to change to get their designs synthesized. 
- Started working on the Cycle Accurate Simulator. Discussed with Emmi and Rafael on how to proceed, and what parts of the design they'll work on. 
- Discussed with Compiler Team and Scheduler on the programming model for Atalla. 
> Where is the de-markation between the SW routines and compiler frontend? 
- Created a set of guidelines, and presented on Sunday, on how people need to write code that goes into Atalla. 

## Future Plan
- Parameterize the Batcher and Benes with a REGISTER_MASK parameter to allow different latching at different stages. We're not sure which is the most efficient configuration of the crossbars. 
- Setup the core Atalla-Sim classes for others to begin experimenting. 