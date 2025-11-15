# Week 11

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Instruction Packetization:**
  - Successfully filled instruction packets with up to four IR instructions and padded with NOPs if a packet wasn't full.
  - The packetization dependency check generally looks good as we are not seeing any conflicting instructions that are grouped together so far.
  - We found out that we cannot implement the packetization in the IR level. The IR still contains label nodes that do not translate to a real machine instruction and labels may appear multiple times especially for entry and exit points.
  - We also found out that some IR instructions expand into more lower-level instructions during codegen. This will be a problem because packet boundaries would not match real instruction boundaries.


- **New Way of Implementing Instruction Packetization:**
  - Problem:
    - Packetization after the IR phase but before code generation will lead to wrong instruction length issues.
    - Packetization after assembly code generation would be extremely difficult to track register uses and dependencies.
  - Solution:
    - Packetization right after IR codegen but before register al
    
    location with instructions using virtual registers. This might work because at this stage dependencies, operand usage, and instruction expansion are all known, but registers haven't been allocated yet.

- **Register Allocation:**
  - Research on register allocation techniques like PresCount that track bank pressure during register allocation.
  - Had a small talk with the scheduler team on how packetization and register-bank conflicts might interact later when packets are issued together.
  - We will ask Professor Jingbo Wang about paper and resources on designing a lightweight bank-aware register allocation algorithm.


```
[ Buckets for <no-group> ]
  depth 0: ['n0 LABEL', 'n1 ENTRY', 'NOP', 'NOP']

[ Buckets for main_block0 ]
  depth 0: ['n2 ENTRY', 'n3 FPRELU32', 'n4 FPRELU32', 'NOP']
  depth 1: ['n5 JMP', 'NOP', 'NOP', 'NOP']
  depth 2: ['n6 EXIT', 'NOP', 'NOP', 'NOP']

[ Buckets for main_block1 ]
  depth 0: ['n7 ENTRY', 'n8 CONSTI32', 'n10 CONSTU32', 'n12 CONSTI32']
  depth 1: ['n14 CONSTU32', 'NOP', 'NOP', 'NOP']
  depth 2: ['n9 STRI32', 'n11 ADDU32', 'n15 ADDU32']
  depth 3: ['n13 STRI32', 'NOP', 'NOP', 'NOP']
  depth 4: ['n16 LDRI32', 'NOP', 'NOP', 'NOP']
  depth 5: ['n17 LDRI32', 'NOP', 'NOP', 'NOP']
  depth 6: ['n18 ADDI32', 'NOP', 'NOP', 'NOP']
  depth 7: ['n19 MOVI32', 'NOP', 'NOP', 'NOP']
  depth 8: ['n20 JMP', 'NOP', 'NOP', 'NOP']
  depth 9: ['n21 EXIT', 'NOP', 'NOP', 'NOP']
```

## Design Choices
- **Packetization Implementation:**
  We decided not to implement packetization at the IR-level because labels and instruction expansion will be very annoying. Assembly-level packetization will also not work because we need to maintain dependency information and this is extremely hard. We decided to implement the packetization after IR codegen and before register allocation. This is because virtual registers are easier to manipulate and all dependency data is still available.

- **Compiler Pipeline Integration:**
  This is a good idea because it keeps packetization close to codegen and we will have more control over instruction emission and can later integrate it into register allocation for latency-aware scheduling.


## Next Week
1. **Implement New Packetization Method:**
   - Move the packetization to right after IR codegen and before register allocation.
   - Test the pipeline to see if the packets are correctly filled and padded with NOPs when fewer than four instructions.

2. **Figure Out Dependency Handling:**
   - Fix the DAG builder to skip label nodes and handle multi-instruction expansions properly.
   - Make sure that memory operations and branches maintain correct ordering within packets.

3. **Start With Latency-Aware Scheduling:**
   - Still waiting for hardware team to finish FU latency table, but after that we can integrate it into the new packetization pass to schedule instructions accordingly.
   - Link the packetized output to the register allocator's vreg tracking system.