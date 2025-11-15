# Week 12

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Instruction Packetization**
  - I think we are done with packetization as we have a working script that satisfies the requirements.
  - We started to test our packetization script across straight-line code, basic branches, and mixed memory ops. The latency aware, scoreboarding, and greedy packing all worked as expected.
  - We have verified that global the load/store ordering is preserved and no RAW, WAR, or WAW hazards in each packets.

- **Register Allocation and Bank Conflicts**
  - Register allocation and bank conflicts are two big issues we have to solve next.
  - Started researching register allocation strategies that account for register banks and conflict.
  - We came up with two ways to implement this. One is to keep packetization separate and run bank-aware allocation after it. The other is to integrate latency-aware ordering with allocation so the allocator sees packet timing and bank pressure together.

- **Design Review**
  - Worked on the slides and presentation for the design review.
  - Worded on the Purdue Research Expo poster outline and artifact list.


build_dependency_graph
```
For each instruction i:
    start = 0
    For each source register s:
        start = max(start, last_write[s])
    If memory op:
        If single LSU:  start = max(start, last_mem_cycle + 1)
        If same addr as previous store: start = max(start, last_store_at[mem_key])
    ready_time[i] = start
    last_write[dst] = start + latency(op)
    If store: last_store_at[mem_key] = start + latency(op)
    If mem op: last_mem_cycle = start
Return ready_time
```

greedy_pack
```
While there are unscheduled instructions:
    Create empty packet for this cycle
    For each instruction in order:
        Skip if already scheduled or not ready yet
        Skip if control mixes with others
        Skip if memory op and one already in packet
        Skip if RAW/WAR/WAW hazard inside packet
        Add instruction to packet
        Mark as scheduled
        If packet has 4, stop
    If packet empty:
        Record empty packet (bubble → 4 NOPs later)
        Advance cycle
    Else:
        Record filled packet
        Advance cycle
Return list of packets
```

packetize_basic_block
```
Parse assembly → (text, op info) list
Compute ready_time = build_dependency_graph(...)
Compute packet_indices = greedy_pack(...)
Convert each index list → instruction text list
Pad each packet to 4 instructions with "nop"
Return all packets
```


## Design Choices
- **Packetization Stage**
  We have decided to run packetization after assembly codegen on physical registers because it gives us a stable instruction count and accurate dependencies.

- **Latency Handling**
  Right now our pass enforces simple latency and scoreboarding constraints. We might have to look deeper into latency modeling combined with scheduler.

- **Bank Conflict Awareness**
  We might integrate the packetization with register allocation if that creates fewer stalls or fewer bank conflicts in flight.


## Next Week
1. **Integrate Packetization Into the Compiler**
   - Create packet markers generators in the lowered output generator.
   - Add checks that NOP padding is preserved through emission.

2. **Register Allocator**
   - Do research on register allocation and bank conflict resolution. Form a research report and talk to the hardware teams about integration.

3. **Latency-Aware Ordering**
   - If the hardware team publishes final FU latencies, insert them into the packetizer.

4. **Design Review and Poster**
   - Fill in the poster sections for background, method, and preliminary results.

