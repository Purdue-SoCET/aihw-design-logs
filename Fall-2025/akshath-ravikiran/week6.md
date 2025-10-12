> This week was spent discussing and solidifying everyone's logic. This comes after 2 weeks worth of uphauling the entire compute architecture in Atalla. Moreover, discussions with Digital Circuits folks to understand how our ideas propogate and get optimized in the RTL world. While Haejune works on the Crossbar RTL, I'll try to implement the switches in Virutoso with TSMC180.
> I had 559 and 371 Midterms back to back. 

## State

[FIXED] I am stuck on Vector Core <=> Scratchpad-Frontend interactions. Tags: Chase Johnson, Jing.
- Context: 
    - How do we maintain throughput in the VC -> Scratchpad pipe?
        - Remember how Scratchpad loads have N cycle latency? How do we ensure we're able to load back-to-back, and avoid having to want N cycles every single load? 
    - My suggestion. Ensure SW compiler packs all related loads back-to-back, and avoid scheduler requiring a handshake from GVLS on `vc.load` instructions. 
        - What would Chase need to keep? 
            - **FIFO-like structure which just has a `stall` signal going back to sched.FU telling it to wait before clearing current request.**
            - This structure also has in-order pop, and writeback into Veggie file. Trivial to implement.
        - How does this help? By avoiding a scheduler handshake, we ensure II=1 pipelining. We'd also "split-transaction" the GVLS. Since scpad returns loads in-order, no need for ID generation and out-of-order tracking.
        - How does this improve throughput? You're guaranteeing that the load pipe to VC is always full. Except on FE-Stalls (check Scratchpad.Frontend RTL) which happen when we prioritize Backend <-> SRAM communication (uncommon case).  
- Update 
    - Discussed with Jing (in class) and Joseph (in MSEE). Never had a formal meeting for this. 
    - Everyone is up-to-date through the VC Discord Channel where Jing explained it. 
        - Implementation might be different, but reasoning is the same. 
- What's pending? 
    - Need a formal RTL handshake between GVLS and Frontend. 
        - Frontend is already built to sustain this behaviour (@Emmi and @Rafael)

## Arch Updates
- [Crossbar Reading List](./assets/crossbar-reading-list.md) outlines the resources we've collated for our literature review. 

## Progress
- This week was spent brainstorming the Crossbar, and discussing with Thomas Munson and Abinands regarding how tradeoffs map into VLSI Design. I think this is very important, and we need to think about it. 
    - Setup TSMC180 on Virutoso with Abinands. 
- Meetings with Jing, Vector Core and Systolic Array to understand their changes, and how it'll trickle down/up to us and SW. 
## Future Plan
- Propogate the changes into the SV RTL, so that students can complete their code. 
- Setup the Functional Simulator core classes. Performance Modelling is very required. 