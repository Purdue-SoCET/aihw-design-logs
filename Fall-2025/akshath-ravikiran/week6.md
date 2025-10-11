## State

I am stuck on Vector Core <=> Scratchpad-Frontend interactions. Tags: Chase Johnson, Jing.
- Context: 
    - How do we maintain throughput in the VC -> Scratchpad pipe?
        - Remember how Scratchpad loads have N cycle latency? How do we ensure we're able to load back-to-back, and avoid having to want N cycles every single load? 
    - My suggestion. Ensure SW compiler packs all related loads back-to-back, and avoid scheduler requiring a handshake from GVLS on `vc.load` instructions. 
        - What would Chase need to keep? FIFO-like structure which just has a `stall` signal going back to sched.FU telling it to wait before clearing current request. 
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
- Add all the crossbar knowledge here. 

## Progress
- Share the new diagram. 

## Future Plan
