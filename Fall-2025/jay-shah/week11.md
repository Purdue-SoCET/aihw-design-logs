# Weekly Report – Week 11

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week

1. Semester project goals changed from complete RTL to creating a functional emulator. It will work as a software checker to ensure correctness of the hardware, 
can later use it in verification of the RTL. It can also be used by the compiler team to understand the hardware architecture model. The emulator will also inform
them about the packet design constraints.
   
2. Discussion points on emulator. High level design of the Python emulator as follows:
   
   a. mem.txt file -> loaded as memory. Read and write to the indexed blocks in the file as if it is a memory
   
   b. Fetch will read N instructions (packet size) at a time from mem.txt.
   
   c. Decode1 to classify the opcodes, and check legality of the packet. Will use the earlier created script for this.
   
   d. Decode2 to identify the functional units of each instruction, and identify all dependencies and hazards. For RAW hazards, we can record them in a
      txt file to identify number of times processor will have to stall. Also similarly create a report for structural hazards (FUs in use, bank conflicts etc).
   
   e. Execute will encompass all functional units. Will put each FU in a separate file.

   f. Emulator branch in github.

5. Requirement from vector team - addition of support for BF16 arithmetic operations on the scalar reg file. BF16 elements stored in the lower 16 bits of sceggie.

---

## Next Week’s Tasks
1.  Work on the emulator. Try to get as many pipeline stages done as possible. I will work on the execute stage FUs.
2.  Design Review on Monday.
