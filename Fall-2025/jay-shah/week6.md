# Weekly Report – Week 6

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. Completed the schematic of GEMM controller:
   <img width="2532" height="4619" alt="Control unit FSMs" src="https://github.com/user-attachments/assets/f7bcfd4f-9754-4797-aaf5-ad933bdfa466" />
   
   Draw.io link: https://app.diagrams.net/#G1ny_7XUN3EX8rw61I_dfyoivOVixZwck6#%7B%22pageId%22%3A%226RZUXqDpa4h_-Ig4mcha%22%7D

2. Discussed changes needed in systolic array controller in the weekly meeting. The schedule of loading inputs and weights into the systolic arrary shifted to the vector core. This is done to reuse the crossbar which provides a row or column of data from the scratchpad. Since vector core already uses such a crossbar, systolic array will make use of the same logic to load its own inputs and weights.

3. In scheduler core, we decided to remove all functional unit status tables and instead issue instructions as soon as they reach the issue stage. Since operations within a packet are independent and the functional units are pipelined, we will send each instruction to its corresponding FU without waiting. As loads/stores don’t have a fixed latency, we can set up a load-store queue so that back-to-back memory operations can be processed without stalling. We will also hide memory latency by issuing other instructions while memory accesses complete.

4. Since the control part of systolic array has been merged into the vector core we discussed with vector team to discuss the interface between scheduler and vector functional unit.


---

## Next Week’s Tasks
1. Need to finaliize the responsibilities of the sys array controller now after the architecture changes.
2. Need to finalize top level diagram of scheduler core.
