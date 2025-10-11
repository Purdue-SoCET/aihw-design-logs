
# Week 7 (October 3rd to October 9th)

## State: 
    Still stuck on acessing asicfab. After some conversation, I did ask itap if they could
    reset my asicfab account, however they reset all of my purdue accounts instead.
    After regaining access to my Purdue accounts, I messaged itap again with a video
    explaining my issue. Hopefully they can understand better and fix it this time around.
    Additionally, my previous blocker on not knowing what is going on with the non-blocking 
    controller is gone because we now have a coherent plan to make progress in that area.

## Progress

### October 3rd
    Had meeting with Dr. Swabey about using a PHY chip and DFI protocol. After this meeting, I am unsure whether
    our technology node can even support DDR4, or if we will have any chance at finding a PHY for DDR4. I addition,
    placing DDR4 on a pcb will require a lot of work. Dr Swabey suggested we switch to DDR2 in the future. 
    This will be cheaper, easier to tape out, however we would have to undo some of Tri's and Dhruv's work and 
    we will not benefit from having bank groups. 
    Additionally, we discussed using 
    verification IP from Synopsis. According to him, this should not be difficult 
    to acquire, and should conveniently find potential faults.
    
    Personally, I am considering trying to find a way to keep
    using DDR4 because having bank groups is extremely beneficial,
    and DDR2 is essentially ancient technology. However, I would use DDR2 if 
    it were necessary for tapeout. 
### October 5th
    At our team meeting, we began discussing what to look for in the non-blocking memory controller.
### October 7th
    Took notes on memory controllers. Sources included an ETH lecture 
    on memory controllers, as well as a Waterloo's student masters thesis
    posted online. Pdf of notes in week7 directory.
### October 8th
    Had another meeting with the team to plan top level for the non-blocking memory contoller. Photo of design 
    ideas in this week7 directory. Our two ideas involved using a queue for load and a queue for store. 
    A scheduler would then choose between the two, maximizing throughput from bank parallelism, and 
    trying to maximize row hits. The other idea involved one queue per bank, which would ultimately increase 
    throughput even more. An arbiter would choose which queue to dequeue from, trying to maximize 
    row hits. We made no decisions at that time for which design or combination thereoff should be final. 
### October 9th
    Finished my first draft of the non blocking controller on draw.io
    and discussed design choices with the rest of the 
    team and Sooraj at our weekly DRAM meeting. We decided that 
    having per bank queues was a more simple and efficient idea.
    It helps maximize throughput be leveraging 
    bank parallelism, and also reduces problems with dependencies. We now have CAM considerations
    though, as well as how we will store data to send back through AXI. 
    There is a screenshot of the diagram posted in this week7 directory.
## Near Future Goals
### Fall Break and next week
    1. Create interface diagram from AXI subordinate to address mapper.
    2. There was talk of having a load queue and a store queue before the bank queues.
        I am still not exactly sure why, so I would like to understand the reasoning
        for sort of combining the two design ideas in order to finalize our design.
        I will have to ask the dram team over fall break, or before our next meeting 
        for a detailed explanation so I know how they are integrated between the 
        address mapper, fsms, and the bank queues.



