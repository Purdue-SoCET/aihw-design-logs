# Week 8

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Packetization Research (Primary Focus):**
  - Completed research on instruction packetization and grouping of independent instructions into packets that can execute in parallel.
  - Studied data, memory, and control dependencies, focusing on RAW, WAR, and WAW hazard detection through DEF/USE set analysis.
  - Built a conceptual framework for representing dependencies as a directed acyclic graph (DAG), where each instruction is a node and edges represent dependencies.
  - Designed a topological-sort-based packet-formation algorithm: at each iteration, select all ready (dependency-free) instructions and pack up to four into a single packet.
  - Based on Professor Wang's suggestion, the IR-stage implementation was deemed most practical, since dependencies are explicitly visible and easily analyzable.

- **Vectorization Background Study:**
  - Reviewed modern SIMD and vector ISA models SSE, AVX, AVX2, and AVX-512.
  - Studied the relationship between compiler auto-vectorization and manual intrinsic usage. understand how loops can be transformed into vector operations when no inter-iteration dependencies exist.
  - Mapped the AVX architectural evolution to our own vector-core design.

- **Compiler Integration Planning:**
  - Determined that packetization will occur immediately after IR generation but before instruction lowering. This allows packet-level grouping to be embedded in the emitted Attala assembly.


### **Design Choices**
- **Packetization:**  
  We decided to handle packetization at the IR stage since it gives us a clear view of instruction dependencies while still being flexible to modify. Doing it later at the assembly level would make it harder to track hazards or aliasing, and doing it earlier (like during parsing) wouldn't give us enough instruction-level detail.

- **Hazard Resolution:**  
  For now, if there's any uncertainty about dependencies (like possible overlapping memory accesses), the compiler won't group those instructions together. Once we have better alias analysis, we can safely relax this rule to get more parallelism.

- **Vector ISA:**  
  We used AVX2 and AVX-512 as references when planning Atalla's vector design. They helped us think through key design points like how many lanes to support, how to handle masking, and how to keep the scalar and vector instruction formats consistent.

### **Next Week**
1. **Begin Packetization Implementation:**
   - Write the initial IR-level pass to analyze DEF/USE sets and build the dependency graph.
   - Prototype the topological sorting and packet-filling mechanism for up to four instructions per packet.
   - Integrate early debug output to verify packet boundaries in the generated IR.

2. **Expand Vector Instruction Set:**
   - Implement core vector operations (vadd, vsub, vmul, vld, vst).
   - Validate register allocation behavior when mixing scalar and vector registers.
   - Test small C programs compiled end-to-end to ensure both scalar and vector instructions flow correctly through the pipeline.
