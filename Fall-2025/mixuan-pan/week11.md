# Week 11 Design Log: Mixuan Pan 

## State

I'm not stuck with anything, don't need help right now. 

## Progress 
This week I modified Vinay's fp16 adder module to a bf16 one. I also successfully synthesized the wallace tree multiplier for bf16 with the help of Nikhil (finally!). 

Vinay also helped looking at the waveforms for the adder, since gtkwave was not doing so well on mac. 

However, the adder isn't simulated yet, and somehow the output of the wallace tree is just assigned to 0. 

There was some issues with boilerkey and asicfab. I heard somebody also had the same issue and asked abt it in discord, but I'm not sure which end is having the problem. Since I couldn't log into ssh asicfab through boilerkey, I was unable to push everything to the Github. 

## Next Step
The next step will be to simulate the adder module and to synthesize the Wallace Tree. Sooraj also wants me to meet with Vinay after that and modify the adder together. 
