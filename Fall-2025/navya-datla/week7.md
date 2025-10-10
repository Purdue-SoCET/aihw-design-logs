State: I am currently not stuck or blocked. 

Progress this week: 

Meetings: 

10/3 - Team meeting with Rishi and Sooraj (VLIW proposed)
10/5 - Worktime where we focused on reading papers and learning more about VLIW
10/6 - Work time with senior design teammates to clarify aspects of microarchitecture (mainly predication and dealing with stores) and making top-level RTL diagram
10/7 - Scheduler core meeting with Rishi
10/8 - Meeting with vector core to clarify vector implementations
10/9 - Meeting with Sooraj and Rishi to clarify VLIW microarchitecture

Notes: 

10/3 - We met on Friday to discuss updates to our RTLs with Rishi before our design review, however we ended up making major changes to our design. We met with Sooraj and Rishi to discuss changing our format to support a mix of VLIW and EPIC instructions in order to simplify the burden on the compiler, as the packet size is fixed. This entails having multiple instructions in one packet and separating them into separate pipelines based on the functional units they use. Sooraj shared multiple resources with us on this topic linked below that I will take a look at to better understand how to implement the microarchitecture:  
- https://www.engineering.iastate.edu/~zzhang/courses/cpre581-f06/lectures/Lecture24-1p.pdf
- https://www2.seas.gwu.edu/~bhagiweb/cs211/lectures/epic.pdf
- https://prod.tinker.cc.gatech.edu/symposia/lcpc01.pdf
- https://zoo.cs.yale.edu/classes/cs323/CAAQA6E/Appendix_H_online.pdf
- https://www.youtube.com/watch?v=FvJTnPEGVWg&t=70s
- https://www.youtube.com/watch?v=jBzj24--_uE

10/5 - Read through the links provided above. *I cannot figure out how to attach my notes. 

10/6 - Senior design group met to work out more details of the VLIW/EPIC architecture in our implementation. We focused a lot on trying to dig deeper into understanding predication, and how stores would work in this context. As we understand it, a predication bit would be set in predication register when the comparison is done, and the if and else instructions would be tagged a certain way to indicate if they correspond to taken or not taken. Then, instructions would only be written back if they match the predicate register value. In this case, however, we were unsure how it would work in the case of a store, where if we executed that instruction into memory there would be no way to nullify it. We figured out that we would need to forward the value from the predicate register in order to do this. We also discussed whether or not we wanted to do a full crossbar from the instructions in the packet into all 10 functional units or if we instead wanted to create segments of functional units that each instruction in a packet corresponded to. We opted to use the full crossbar method as this would allow us to more easily parametrize our design for packets of 2, 3, or 4 instructions to compare performance. We created a rough draft of our top-level diagram by the end of this meeting. 

10/7 - Met with Rishi for our weekly scheduler core meetings. We had a lot of questions for him after our discussion the day before, including predication register specifics, how to handle memory accesses, and how to access shared resources (ex: reg files). We learned we need to meet with vector core team again to further clarify aspects of veggie file access. Another realization we came to that we need to add in the microarchitecture is that vector loads/stores will need access to the scalar register file in order to get addresses. Set up meeting with vector core for Wednesday. 

10/8 - We learned more about the specific microarchitecture of the vector reg file and core. The vector reg file will have 4 register banks and 2 mask banks. Can have up to 2 vector operations in the same cycle. Everything other than division can be sent out every cycle - there will be a ready signal that tells us when we can send another instruction. Jing suggested that a way we could keep track of dependencies when we get a new dependent packet by having a counter that we increment when an instruction goes in and decrement when an instruction comes out. When the counter hits zero we know we are ready to start decoding the next dependent packet. 

10/9 - Our team met with Sooraj to clarify some of our questions about VLIW and set out some of the architecture. 
- Branches: we decided that branch instructions will come in a packet with none of the other instructions dependent on the branch. We will implement a forward not taken, backwards always taken predictor as it is good for loops which is majority of our workload. We move everything in lockstep until execute. In the case we have a nested loop, jumping to another branch is the uncommon case (as normally it will just be jumping to the beginning of the inner loop). 
- Banks: The veggie is banked four ways. When we design the instruction packet types, we need to generate a full list of all packet types to prevent bank conflicts. 
- Stall Counter: This will help us with loads and stores. This is an adaptation of the method Jing suggested during the meeting on Wednesday. Each packet would come with two bytes of metadata (check|set) and we would have a unit with a bitmap corresponding to 8 different packets. The set byte would set the correct bits in the register to let subsequent instructions know, and the check byte will tell this packet what bits to check in the bitmap register. Due to this, we will also need an instruction buffer as we will have to send instructions through if certain ones need to wait.

Next Steps: 
- Generate a comprehensive spec to provide to the compiler detailing everything, including a full bit spec for all subunits, an explanation of VLIW, a worst-case latency guarantee (green zone), and explain things not to do
- Finish creating top-level diagram with adapted microarchitecture
- Re-do scalar FUs
- Prepare abstract for our poster presentation