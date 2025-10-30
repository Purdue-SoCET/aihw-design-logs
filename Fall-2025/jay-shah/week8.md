# Weekly Report – Week 8

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. Created the top level diagram for the VLIW pipeline:
https://app.diagrams.net/#G1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu#%7B%22pageId%22%3A%22l9r9ZbctkA58CtwA39yn%22%7D

2. Further discussion on the Tainted VLIW within the team. Following points were decided upon:
   a. No instruction queue before decode. Earlier we thought of having an instruction queue before decode to select independent packets which can be issued.
   But the level of inter-packet paralelism that we can exploit is not clear. So add instruction queue on a need-basis.
   b. Each functional unit will send a ready signal to indicate that it can accept a new instruction. Scheduler will use this information to schedule the packets. So
   the latency handling is done by scheduler, not the compiler.
   c. Dependency registers will hav counters associated with them. Counter max value = Max instructions in packet. Each completed instruction will decrement the corresponding
   counter.
   d. SDMA instruction needs special handling by the compiler while checking the dependencies. Because the source register in SDMA instruction is technically a destination register.
   So the compiler cannot clobber that register if the SDMA has finished reading it.

3. Worked on the scheduler core report for the compiler.
https://docs.google.com/document/d/15TX6ejTXwMY4YGQDDYGwEilZKdPOWRFbuzRXQ77uAfM/edit?tab=t.0
   Created the sections on scoreboarding, superscalar, VLIW and EPIC, found references for each.

4. Worked on the Design Review slides.
https://docs.google.com/presentation/d/1VntG-ZXWseMChrpcM8x8SDW8myC_xpgNyK9JG81pr1I/edit?slide=id.p#slide=id.p
---

## Next Week’s Tasks
1. Finish the Design review slides and present them
2. Finish the compiler report.
3. Analyze the possible instruction combinations per packet produced by Josh's script.
