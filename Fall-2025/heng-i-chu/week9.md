# Week 9

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Basic Block:**
  - Successfully found a way to break down the IR into basic blocks with each representing a straight-line sequence of instructions with single entry and exit points.
  - Complete the PPCI frontend so that it correctly emits labels and terminators for branch and jump targets.
  - Added instrumentation hooks to mark block boundaries for DAG creation.

- **DAGs:**
  - Wrote a script that builds the DAG for each basic block to represent instruction dependencies.
  - Each node corresponds to an instruction and edges capture data dependencies (RAW, WAR, WAW).
  - Specifically marked memory operations so that global load/store ordering can be preserved during packetization.
  - Found that DAG construction can reuse IR DEF/USE information that is already in PPCI.

- **Packetization Algorithm:**
  - Wrote a simple script that implements some packetization algorithms that selects ready nodes from the DAG.
  - Currently each packet is filled maintaining global load/store ordering.
  - Kinda found a way to packet ordering to minimize total execution latency.
  - Packet sizes should not hardcoded. This provides hardware design flexibility (bruh).


### **Design Choices**
- **Basic Block & DAG:**  
  We will directly use the basic block boundaries from the PPCI IR. The DAG construction functions allow DEF/USE sets to capture dependencies while keeping compatibility with probably other optimization passes.

- **Packetization:**  
  We have decided to implement packetization on the DAG by selecting ready nodes and then build packets according to the global memory order and FU latencies. This way allows flexible packet widths and dynamic reordering.

- **Scheduler Team:**  
  Although the scheduler team dumps their problems to us like they are supposed to, we still have to adapt to changing FU and register-bank configurations. This ensures that compiler output can scale with future hardware updates.


### **Next Week**
1. **Finalize DAG to Packet:**
   - Implement IR level packetization and print out the lowered code.
   - Add visualization of DAGs to check dependency edges.

2. **Register Allocation Research:**
   - Research register-bank allocation methods and related papers and conflict detection methods.
   - Start integrating our scripts into the backend register allocator.




