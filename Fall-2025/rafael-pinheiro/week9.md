State: I am not stuck with anything, don't need help right now.

## Progress summary

Headstarting potential Senior Design project: Cycle-Accurate Simulator for Atalla

### What?

Funcitonally accurate simulators, or cycle-accurate simulators (CAS) reproduce the functional behavior of the emulated object at the granularity of individual clock cycles. We can model the ISA, pipeline stages, local cache and provide I/O signals at each clock transition.

-> We can deliver precise clock cycle counts for code execution

Instruction set simulators (ISS) simulate the ISA, values on memory and registers, but they do not model the pipeline effects or accurate clock cycle counts. They are usually faster than CAS's, but they do not model pipeline effects or accurate clock cycle counts.

Timing accurate simulators (TAS) provide full timing accuracy, simulating detailed timing behavior, including I/O signals to change at unique times. Usually much slower than TAS and CAS.

### Why?

Atalla rely on a complex memory hierarchy, dataflow, and parallel compute pipelines. ISS tools fail to capture these interactions, while RTL simulations are slow. A CAS offers the middle ground - precise cycle counts for workload characterization and microarchitectural exploration.

CAS provide a detailed simulation of the IC's internals, and enables determination of the exact number of clock cycles required for execution of the program. Thus, exploration of the microarchitecture of the design, pipeline verification and cache modelling are leveraged by the CAS.

The CAS will be built with knowledge of Atalla's operation, so it can take into account microarchitecture behaviors that can affect execution time.

### How?

The CAS needs to model fundamental hardware components. Having the inner structures modeled in the CAS will accurately provide the programmer any stalls in the system. Being able to predict more accurately the CPI and instruction count of a program execution makes a CAS more useful in the architectural analysis of a design, compared to an ISS that will only provide the instruction count, once it only takes into account the ISA of the system.

A CAS is implemented using a discrete and fixed timestep called "tick". At every tick, the simulated system is updated given the described functionality modeled.

In other words, the CAS is a discrete event simulator. At each timestep, the event at the head of the queue is dequeued, executed and the modules evoke new events, added to the queue.

Every modeled component needs to recognize this global tick and update accordingly. They need to maintain internal state, I/O buffers and expose a ```tick()``` method that reads inputs from the input buffer, computes the next internal state given the described functionality and spit out an output in the described latency.

i.e.,

```Producer → [output buffer] → [input buffer] → Consumer```

E.g. of pseudocode in python:
```python
def tick():
    # stage reads previous cycle's inputs
    if input.valid and can_accept():
        next_state = compute(input.data)
        output_buffer.data = next_state
        output_buffer.valid = True
    else:
        output_buffer.valid = False
```

The tick-level update order is usually done in two schemes. Either:
1- Lockstep global tick
    - Every model updates at every tick
    - Use double buffering to avoid race conditions (read from old state, write to next state)
2- Event driven (Like gem5, likely the scheme to be implemented)
    - Only modules affected by a ready event are updated
    - Implemented via event queue

Note: possible to mix them up: e.g. lockstep tick for MAC's in the Systolic Array, event queue for Scratchpad accesses.

### Some design guidelines to take into account
- Updates must be synchronous: all updates advance on the global tick
- FSM-like state separation between current state and next state
- Latency modeling per-unit configurable delays
- Propagate stalls using valid/ready to enforce backpressute
- Parametrize each module’s latency, bandwidth, and queue depth to be configurable for exploration
- Record per-cycle traces (e.g., CPI, stalls, utilization)

## Next Steps
- Research more into gem5 and GPGPU-sim, specially the gem5 bootcamp[https://github.com/gem5bootcamp]: seems to be quite descriptive on modeling new structures on gem5, might get some inspiration from it
- Think on what structures the modules should have:
  - how to store its state and determine the next;
  - how to handle I/O queue;
  - if decide to do the mix of the lockstep global tick and event driven CAS: how to integrate both of them;
  - how to handle the event queue