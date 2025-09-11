# Week 1 Design Log

## State:
I am not stuck with anything, don't need help right now. 

## Progress:
Review MIT Open Course chapters 7, 14 and 15.

## Chapter 7
Latency: Time for a system to process a single input and produce the corresponding output.
Throughput: Rate at which outputs are produced.
Propagation Delay: Time taken for a signal to pass through a combinational circuit or component.

Pipelining
- Use registers to hold intermediate values while other parts process the next inputs.
- Clock period set by the slowest stage's propagation delay.
- To increase throughput you divide logic into stages separated by registers.
- Each input advances one stage per clock cycle.
- Higher throughput may cost slightly higher latency.

Pipelinng Conventions
- Trying to create an acyclic circuit with exactly K registers on every path from input to output.
- Every stage has a register on its output.
- Clock period must be greater or equal to the input register propagation delay + logic delay + output register setup time.

Latency = K x clock period
Throughput = 1/clock period

## Chapter 14
Problem
- The more memory we add, the longer it takes to reach a specific location.
- Latency becomes a key design tradeoff when building larger storage arrays.

DRAM (Dynamic RAM)
- Designed for high density and low cost.
- Stores bits using a capacitor + transistor (1T).
- Downsides: slower, destructive reads, capacitors leak charge → requires refresh cycles.

SRAM (Static RAM)
- Optimized for speed rather than density.
- Stores data with bistable latch (two inverters in positive feedback).
- Faster and simpler reads/writes, but larger in area than DRAM.

Non-volatile Storage (Flash, HDD)
- Preserves data without power.
- Used for long-term storage, slower than volatile memory.

Cache
- Small, fast memory holding recently used data.
- Fully Associative Cache: Any block can go to any cache line.
- Flexible, but expensive (need hardware to compare all tags in parallel).
- Set Associative / Direct Mapped: Tradeoff between cost and flexibility.

Design Tradeoffs
- Larger cache size → lower miss rate, but longer hit time.
- Larger block size → better spatial locality, but worse miss penalty.
- Higher associativity → fewer misses, but higher hardware cost.
- Replacement policies (LRU, FIFO, random) → affect miss rate and complexity.
- Write policies (write-through vs. write-back) → trade bandwidth vs. complexity.

## Chapter 15
Single-Cycle
- PC → memory → fetch instr → decode → read regs → ALU → (mem if LD/ST) → write back.
- Clock period set by worst-case path.

Pipelined (5 stages)
- IF - fetch instr, PC+4
- RF - decode, read regs
- ALU - execute / addr calc
- MEM - load/store access
- WB - write result
Throughput = 1 instr/cycle. latency = 5 cycles.

Hazards
- Data hazard (RAW): consumer needs producer's result.
- Control hazard: branch/jump/exception changes next PC.
Fixes
- Stall: hold IF/RF, waste cycles, increase CPI.
- Bypass: forward result from ALU/MEM/WB to RF, reduces stalls.
- Speculate: predict PC+4. modern CPUs use branch prediction.

Tradeoffs
- Deeper pipeline = shorter clock, but more hazards.
- Compilers can schedule to reduce stalls.
- ISA must stay fixed (no mandatory NOPs).