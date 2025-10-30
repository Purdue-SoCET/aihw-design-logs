# Weekly Report – Week 8

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week

1. Discussion points this week:
   a. Need to conserve the usage of dependency bits, do not needlessly propagate dependency to downstream instructions. Eg - Dependency of register 0 should not
   needlessly propagate to (n+1)th instruction if (n)th instruction is going to be executed only on the clearance of register 0 anyways. Reasoning: to conserve
   dependency bits.
   b. Changed the vector and scalar mov instructions based on discussion with the vector team. There will be a new mask register file which will store the
      mask register bits. Instructions added to move data between sceggie and veggie files. For sceggie -> veggie use implicit type conversion and broadcast.
      For veggie -> sceggie, take an immediate an input that specifies index, move the element of tha index to sceggie. Also support for sceggie -> mask reg file.
      Have also added a conversion instruction to convert a data from INT32 -> BF16, but not sure of its usage.
   c. Possible expansion of dependency registers from 8 -> 16. This is completely based on the number of instructions present in the pipe at a time. If all of the
      instructions in pipe are independent, we will need more than 8 registers to capture this scenario. Need to fine tune the number later, but keeping 16 registers
      for now.
   
3. Completed the scheduler core design spec that we were working on since last week..
https://docs.google.com/document/d/15TX6ejTXwMY4YGQDDYGwEilZKdPOWRFbuzRXQ77uAfM/edit?tab=t.0

4. Presented the Design review on Monday. Discussed the usage of vector Mov instructions in the presentation. Also discussed the on the compiler's job of
   setting the dependency bits. 
   https://docs.google.com/presentation/d/1VntG-ZXWseMChrpcM8x8SDW8myC_xpgNyK9JG81pr1I/edit?slide=id.p#slide=id.p
---

## Next Week’s Tasks
1. Update the diagrams with new changes
2. Meeting with the vector teams to finalize on writeback, move instructions and latency of operations.
3. Need to start RTL and testpplans.
