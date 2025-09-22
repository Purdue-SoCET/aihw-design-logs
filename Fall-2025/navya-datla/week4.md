State: I am not currently stuck or blocked. 

Progress: 

Last Sunday we met as a team to discuss the project and our progress in understanding the material. I have been working on understanding the architecture and developing RTLs. We worked on creating our senior design pitch for the out of order scheduler, and finished up our slide. 

On Monday we found out that the scheduler core was changing significantly. During our meeting on Tuesday, we learned the specifics of how it has changed. Rather than dispatching and issuing the instructions out of order in the scheduler core, we are going to have a new compiler format that will send us the packets out of ordered already. We will get packets with a bunch of independent instructions and we can execute them in order. This significantly changes the scheduler core's architecture. 

We created our senior design idea pitch we presented on Wednesday. We decided on the following: 
- Problem: we can get similar performance by simplifying the scheduler greatly, and we need to adapt it to a new ISA, vector core, scratchpad, and new packetized compiler format
- Our Approach: Learn the current implementation and modify it in diagrams and code before deploying and verifying integration
- Biggest Challenge: We anticipate that our biggest challenge will be integration with all of the new changes. It will definitely require a lot of constant communication. 

I will be mainly working on the new decode logic. 

Next Steps: 
Continue RTL diagramming and fully understanding everything about the current implementation by Sunday so we can get ready to make changes. 