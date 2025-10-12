# W4 Design Log - Adrian Buczkowski

## State: 
I am currently waiting for our Sunday meeting so I can begin to help Dhruv and Tri with the verification of the individual modules. There are some outstanding problems with the current testing that I hope to help resolve. Additionally, we have begun discussions about the shape that our non-blocking DRAM controller will take. After meeting with Sooraj, I have a better understanding of what we need to target with the new deign was. Also, due to previous work on the controller, we should be able to focus on the logical design of the controller without as much concern for signal timing.

## Progress: 
This week I verified the signal timing that Dhruv and Tri made earlier in the project. Additionally, I read and watched source material about how non-blocking DRAM controllers are designed. I still have some questions about some timing parameters thatthey came up with, but I get the general idea. 

To verify the signal timings, I consulted the JEDEC standard linked here.
file:///C:/Users/buczk/Downloads/JESD79-4%20(1).pdf

I have some additional comments about the signal timings that I verified this week. There were certain timings that both me and Aryan were unsure about how to calculate. In the linked google sheet:

https://docs.google.com/spreadsheets/d/13PtLaNb6d3P4XnwW7sbp-T2ta2oH8RB8WwMKiGVsl7s/edit?gid=0#gid=0

You can see certain timings marked with question marks. These cases were either not well documented or just hard to find in the JEDEC standard. 

Another question that came to my mind was how will these timing chage when we dispatch multiple requests at once. What I currently know is that every few cycles we can dispatch a command independent of the previous one. What we need to figure out is if the commands will always come back in order and if any intra-command timings change.
