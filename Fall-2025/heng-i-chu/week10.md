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


## Design Choices
- **Packetization:**
  Packetization is done directly on the DAG by selecting dependency-free instructions and grouping them into packets of up to four. We made sure to preserve memory order and dependency correctness. Once we receive FU latency data, we’ll update the packetization logic to schedule based on latency as well.

- **Register Allocation:**
  Since our architecture uses register banks, we need to consider both allocation efficiency and bank conflicts. We plan to experiment with simple greedy allocation first and then look into more advanced approaches once we have testable workloads.

- **Scheduler Team:**
  Even though the scheduler team passes their issues to us as expected, we still have to keep up with changing FU and register-bank configurations. This helps make sure our compiler output stays compatible and scalable as the hardware design evolves.


## Next Week
1. **Finish DAG to Packet Integration:**
   - Finalize the IR-level packetization logic and make sure packets are visible in the lowered code.
   - Add DAG visualization to verify that dependency edges are correct.

2. **Register Allocation Work:**
   - Continue studying register allocation techniques with a focus on register banking and conflict detection.
   - Start testing simple allocation behavior with packetized DAGs.

3. **Latency-Aware Scheduling:**
   - Once the hardware team provides FU latency data, begin integrating it into the packetization process for more accurate scheduling.
