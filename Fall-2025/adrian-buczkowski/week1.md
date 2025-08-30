# W1 Design Log - Adrian Buczkowski

## State: 
I am currently waiting for further meetings to get started with my work. I will do my best to find out as much as I can about the current state of the controller and work with Dhruv and Tri to get onboarded.

## Progress: 
This week I found my team after talking with Sooraj and others. We have determined that during the first semester of my senior design, I will help the DRAM controller team finalize the blocking version of the controller. The current project state can read and write, but it cannot implement the full set of functions that it is supposed to. Our intial goal is to get this version full working and verified. The final product of my seior design is to architect a non-blocking version of the DRAM controller. This architecture would maintain the entire original set of functions, but it would also not stall the rest of the system while processing requests. The new architecture will queue up requests, then use reordering, coalescing, and redundancy checks to maximize memory bandwidth. Additionally, we have more people on the project than anticipated. This could resultin the timeline for the project being advanced. 

