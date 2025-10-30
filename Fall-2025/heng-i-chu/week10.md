# Week 10

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Packetization:**
  - We have successfully grouped IR instructions into packets of up to 4 based on dependencies.
  - We have ensured that the packets maintains correct memory operations and global load/store ordering.
  - Start researching for ways to connect the packetized DAG to codegen and alot the backend to emit properly grouped instructions.
  - Still waiting for the hardware teams to provide the latencies for each FU to implement latency-aware dependencies.

- **Register Allocation:**
  - Start researching register allocation, register banking and conflict resolution.
  - Wrote a summary of research papers for handling multiple register banks.
  - Looking up examples on how to perform a basic register allocation pass into compiler backends.

- **DAG to Integration:**
  - Start testing if the DAGs generated from the IR were correct dependencies when passed to the packetization logic.
  - Designed how to feed the packetized DAG into codegen so that packets are preserved in the emitted assembly.
  - Kind of found some ways to represent packets directly as grouped IR nodes.

```
[ Buckets for <no-group> ]
  depth 0: ['n0 LABEL', 'n1 ENTRY']

[ Buckets for main_block0 ]
  depth 0: ['n2 ENTRY', 'n3 FPRELU32', 'n4 FPRELU32']
  depth 1: ['n5 JMP']
  depth 2: ['n6 EXIT']

[ Buckets for main_block1 ]
  depth 0: ['n7 ENTRY', 'n8 CONSTI32', 'n10 CONSTU32', 'n12 CONSTI32']
  depth 1: ['n14 CONSTU32']
  depth 2: ['n9 STRI32', 'n11 ADDU32', 'n15 ADDU32']
  depth 3: ['n13 STRI32']
  depth 4: ['n16 LDRI32']
  depth 5: ['n17 LDRI32']
  depth 6: ['n18 ADDI32']
  depth 7: ['n19 MOVI32']
  depth 8: ['n20 JMP']
  depth 9: ['n21 EXIT']
```

## Design Choices
- **Packetization:**
  Packetization is done directly on the DAG by selecting dependency-free instructions and grouping them into packets of up to four. Once we receive FU latency data, we'll update the packetization logic.

- **Register Allocation:**
  Since our architecture uses register banks, we need to consider both allocation efficiency and bank conflicts. We are trying to implement a greedy allocation algorithm.


## Next Week
1. **DAG to Packets:**
   - Update the IR packetization logic and make sure packets are visible in the codegen.
   - Also add Pydot DAG visualization at the codegen.

2. **Register Allocation:**
   - Study register allocation techniques with register banking and conflict detection.
   - Start testing simple allocations with packetized DAGs.

3. **Latency-Aware:**
   - Once the hardware team provides FU latency data, begin integrating it into the packetization.
