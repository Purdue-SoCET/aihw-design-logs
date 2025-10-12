> This week was spent in getting students up-to-date with changes, finalizing with Haejune his design (good job!), and then completng my portion of the RTL. Design freeze!! Also, got started with the Functional Simulator in Python. 

## State

[STALLED] I am stuck on DRAM Cntrl. <=> Scratchpad-Backend interactions. Tags: Aryan Kadakia, Tri Than. 
- Context: 
    > Note: Dr. Swabey limited number of DRAM DIMMs to 1. Not 8. Bandwidth cut down 8 times. 
    - I initially thought we'd have a {512b-data, 6b-id, 32b-mask} FIFO between the AXI-Bus and Backend. Backend would fill this up with load/store requests async, and "Req.FSM." goes offline. 
        - Note: The responses to Backend from the AXI-Bus would be async too. AXI-Bus would have to hold data ONLY if the Backend asks it to stall. Only reason for a stall (latency in accepting AXI-Bus response back ino Scratchpad) would be because the SRAM stalls. 
            - Remember, we always prioritize Backend over Frontend, so issue-pipe won't stall ever.
    - But, the DRAM interactions with a single DIMM are 64b wide. This means the DRAM Controller can't meet the bandwidth we want, even if we accomodate for it now.
    - My suggestion. Make the FIFO {64b-data, 8b-id, 4b-mask}. Have the Backend contain an FSM which breaks each 512b request into 8 of these mini-requests. 
        - How does this help? We offload some work from the DRAM Controller. 
        - How will DRAM Cntrl. team deal with the UUID situation. Simple!   
            - Maintain `log_2(64b/ELEMENT_SIZE)` bits at the end of the UUID -- to encode position of each 16b value in the 64b packet within the 512b burst. 
                - Sounds complex, but it's super simple. 
            - They will continue to have the same logic to group together seperate requests that are within the same "burst/operation". 
            > UUID[MSB] only maps to "burst" level. UUID[MSB-1:0] maps to requests within the burst.
    - Ok great. This sounds easy. What about TKEEP signal? 
        > This is a Store problem; doesn't translate to Loads. 
        - AXI Busses use a TKEEP signal to encode how many values within the "burst" (64b packet) need to be stored into the DRAM 
        - Remember, we have a 4b-mask telling DRAM which of the 16b ELEMENTs within the 64b packet need to be stored. 
            > These masks are always contiguous. {1111, 1110, 1100, 1000} are the only possible options, where 0 means don't store. 
        - **But!!!!!!!!!! DRAM Controller interactions with the PHY are fixed to 64b :( Which means, they give a single address, and 64b to store -> this is the level of atomicity with the PHY**
        - They cannot handle this fine-grained control of the data storage between 16b slices within the 64b packet. 
        - Result == Cooked. 
- Update: Aryan and Tri are combing through DRAM literature to understand if this is possible. Blocked.  
- What's pending from Scratchpad? Formal RTL handshake between Backend and AXI-Bus. (@Julio needs to make another FSM additionally. Trivial.)

## Arch Updates
B3: Backend will now contain some kind of FSM, taking care of this throttling of every request into 8-deep bursts. All of these mini-request IDs within a burst will be seperated by `log_2(64b/ELEMENT_SIZE)` bits indicating which slice of the burst it belongs to. 
C2: We've decided to analyze different designs, implement in RTL and then synthesize them. 
    - Naive Crossbar. Baseline. Lat = 1. Area = Worst. Freq = Horrible.
    - Benes MIN. Lat = 9 + 5. Area = Better. Freq = Mid. 
    - Batcher MIN. Lat = 15. Area = Little worse than Benes. Freq = Better than Benes. 
T3: Here is the latest [RTL Diagram](./assets/v4_rtl.png) outlining the **[Frontend/Backend -> Head -> Stomach -> Tail -> Frontend/Backend]** flow within the scratchpad.

## Progress
- Completed the [V4 RTL Code](https://github.com/Purdue-SoCET/tensor-core/tree/scratchpad_main/rtl/modules/memory/scratchpad). 
    - Literally, only Frontend and Backend units are left. 
    - Crossbar modules just extract all the required design choices. Naive is implemented. Haejune needs to make his network parameterizable, and then embed it into the `rxbar.sv` and `wxbar.sv` modules.
- [Crossbar Reading List](./assets/crossbar-reading-list.md) has been updated with a summary of the designs we're going for, and the "What" of the options. 
- Completed [7 weeks worth](https://github.com/Purdue-SoCET/aihw-design-logs/blob/main/Fall-2025/akshath-ravikiran/) of Design logs :) 
- Re-arranged the [codebase](https://github.com/Purdue-SoCET/tensor-core/tree/848ad6f5c47980ae20f4b58c27c00f1f7caf042a), and made a cleaner Makefile for people to work with the code. 
- Compiled an [instruction-scheduling-reading-list.md](./assets/instruction-scheduling-reading-list.md). Want to work on the IR -> CodeGen optimization flow w/ Timmy and help the compiler team. 

## Future Plan
- Sit down with Haejune regarding Crossbar Synthesis! 
- Setup UVM-like verification infra for others to build off of. 
- Core Functional Simulator classes. Build one similar to how the GPU Team is building. 