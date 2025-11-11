# Weekly Report – Week 10

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week

1. Discussion points this week:
   a. Changes proposed in the packet dependency logic. The earlier design of compiler encoding the dependency bits in the packet metadata is too complicated
   for the compiler team, so instead we will have a dependency bit with every single register in the register file. When an instruction issues, it sets the
   dependency bit of its destination register. Subsequent instructions check the dependency bit of their source registers, and only issue if they are cleared.
   RAW hazards will be handled by this, but I think we still need to see if it handles WAR and WAW hazards. Same scheme will apply for scalar, vector and mask
   register file.
   b. Compiler will try to fill independent instructions in the packet as much as possible, but no guarantees, so scheduler has to check dependencies. They
   will also try to make use of the green zones as much as possible based on the hardware latency information we provide them.
   
2. Starting work on the interfaces. We have planned the interfaces in this way:
   a. There will be an interface among the back-to-back pipe stages of the scheduler (Fetch <-> Decode1. Decode1 <-> Decode2 etc.).
   b. Decode2 interface to Scalar, Vector, Mask register files.
   b. Interface from the scheduler Execute stage to each Scalar FU, Systolic array, Vector lane and scratchpad.
   c. Writeback interface to Scalar, Vector, Mask register file.

## Next Week’s Tasks
1. Update the diagrams with new changes.
2. Design review prep
3. Complete the interfaces.   
---

## Next Week’s Tasks
1. 
