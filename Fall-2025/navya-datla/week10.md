State: I am not currently stuck or blocked. 

Progress: 

Came back from being out of town on Saturday, had a big exam, and was sick so didn't get as much done this week. 

- Caught up on changes from Friday meeting with Sooraj

Sunday 10/26: 
- Dependency register has changed
  - Now it is based on the status of the registers and what is being used rather than the status of the packet
  - The reasoning for this is to make the compiler team's lives easier as they don't have to provide us with 
- When we have two instructions going back to back that are writing to the same destination register, we have to make sure no WAW hazards
  - Due to this, one of our ideas is to check the destination register and stall if that is in use

Next Steps (by DR): 
- Top-level diagram finished
- Compiler Spec
- Interfaces


