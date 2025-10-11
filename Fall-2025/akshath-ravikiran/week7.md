## State

I am stuck on DRAM Cntrl. <=> Scratchpad-Backend interactions. Tags: Aryan Kadakia, Tri Than. 
- Context: 
    - I initially thought we'd have a {512b-data, 6b-id, 32b-mask} FIFO between the AXI-Bus and Backend. Backend would fill this up with load/store requests async, and "Req.FSM." goes offline. 
        - Note: The responses to Backend from the AXI-Bus would be async too. AXI-Bus would have to hold data if the Backend asks it to stall. Only reason for a stall (latency in accepting AXI-Bus response back ino Scratchpad) would be because the SRAM stalls. 
            - Remember, we always prioritize Backend over Frontend, so issue-pipe won't stall. 
    - But, the DRAM interactions with a single DIMM are 64b wide. This means the DRAM Controller can't meet the bandwidth we want, even if we accomodate for it now.
    - My suggestion. Make the FIFO {64b-data, 8b-id, 4b-mask}. Have the Backend contain an FSM which breaks each 512b request into 8 of these mini-requests. 
        - How does this help? We offload some work from the DRAM Controller. 
        - How will DRAM Cntrl. team deal with the UUID situation. Simple! 
- Update: 
    - 
- What's pending? 
    - Formal RTL handshake between Backend and AXI-Bus. (@Julio)
        - Aryan and Tri are consulting DRAM documentation. This is question of FSM => PHY => DIMM interactions. Requires lit.review. 

## Arch Updates
- Scratchpad-Backend will now contain some kind of FSM, taking care of this throttling of every request into 8-deep bursts. All of these mini-requests within a burst will be seperated by 2 bits. 

## Progress
- 

## Future Plan
- 