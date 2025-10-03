State: I am not stuck with anything, don't need help right now. 

Progress
First semester with AI hardware, currently reading documentation to get up to speed with the rest of the team
Working with the systolic array portion of the team

## Chapter 7 

Latency: 
The delay from when an input is established until the output associated with that input becomes valid

Throughput: the rate at which inputs or outputs are processed

Both are performance metrics

Laundry Ex | Latency | Throughput
Harvard 90 min 1/90 output/min 
MIT 120min 1/60 output min

Normally if you increase throughput latency will increase as well. Ex pipelining 

General plan to increase throughput for combination logic is to utilize registers to divide the processing into a sequence of stages 

Pipeline Conventions
Def : A well-formed K=Staged pipeline is an acyclic circuit having exactly fK registers on every path from an input to an output

A combinational circuit is thus a -=stage pipeline

Composition Convention:
Every pipeline stage, hence every k=stage pipeline, has a register on its output

Always - The clock common to all registers must have a period sufficient to cover propagation over combination paths plus input register t_pd plus output register t_setup

The latency of a k=pipeline is k times the period of the system clock
The throughput of a k=pipeline is the frequency of the clock

Usual goal for pipeline a circuit is to achieve maximum throughput using the fewest possible registers 

## Chapter 14

More location for memory means longer access latencies

DRAM - Dynamic Access memories
Optimized for capacity and low cost, sacrificing latency

SRAM - Static Random Access Memories 
Low latency to a bunch of locations

Nonvotable storage
Memory conservation even with no power [Flash / HDD] 

To access SRAM
	Enough address bits to uniquely specify location i.e 3 bits for 8 locations

Composition 
	Bit Cells 
		Typical cell has 2 CMOS inverters wired up in a positive feedback loop to create bistable storage element

Both sides of the loop are connected via FET

Array of k * b cells (k words, b cells per word)
Read: precharge it lines, activate worldline, sense
Write: drive bit lines, activate worldline, overpower cells

DRAM 
Writes : Drive bitline to Vdd or GND, activate worldline charge or discharge capacitor 

1T DRAM
	Transistor + capacitor
Smaller than SRAM, but destructive reads and capacitors leak charge

DRAM arrays include circuitry to 
Write word again after every read
Refresh  every word periodically

DRAM v SRAM
20x denser than SRAM
2 * 10x slower than SRAM

Memory Hierarchy 
Expose Hierarchy
Registers, SRAM, DRAM, Flash, HDD
Tell programmers to use cleverly

Hide Hierarchy
Programming model: single memory, single address space machine transparently stores data in fast or slow memory depending on usage patterns

Locality principle
Keep most often used data in a small fast SRAM 
Refer to main memory only rarely for remaining data

Locality of reference
Access to address x at time t implies that access to address x + delta x at t + delta t becomes more probable as delta x and delta t approach zero 

Cache
A small interim storage component that transparently retain (Caches) data from recently accessed location
Very fast if data is cached, otherwise accesses slower larger cache or memory
Exploits the locality principle

Computer systems offer use of multiple levels of cache

AMAT - Average memory across time

AMAT = Hit Time = missRatio * Miss Penality

Caching improves AMAT
Formula can be applied recursively in multi-level hierarchies

Fully associative Cache 
Opposite extreme : any address can be in any location
No cache index
Flexible
Expensive - must compare tags of all entries in parallel to find matching one [Hardware - CAM]

Summary 
Larger Cache Size : Lower miss rate, higher hit time
Larger Block Size : tradeoff spatial for temporal locality, higher miss penalty 
More associativity: lower miss rate, higher hit time
More intelligent replacement: lower miss rate, higher cost 
Write policy lower bandwidth, more complexity 
How to navigate these dimensions? -> Simulate 

## Chapter 15

Begin clock cycle
	New value into program counter
Sent to main memory as the address of the instruction
Upcode decoded by control logic to determine control signals
Read from register file and routed to ALU

Output ALU serves as memory address

Pipelined Implementation
Divide data path in multiple pipeline stages 
Each instructions execute over multiple cycles
Consecutive instructions are overlapped to keep CPI = 1 

Classic 5 stage pipeline

Instruction Fetch Stage : maintaining PC, fetches instruction and passes it to 
Register File Stage : Reads source operands from register file, passes them to 
ALU stage : Performs indicated operation in ALU passes result to 
Memory Stage: If it’s a LD, use ALU result as an address, pass mem data (or ALU result oif not LD) to 
Write-Back Stage: Writes result back into register file 

Data hazard -> Execution of current instruction depends on data produced by earlier instruction
Control Hazard -> Occurs when a branch, jump, or exception changes the order of the execution 

Strategies to resolve Hazards
Stall 
Bypass/Forward
Speculate

Stall 
Freeze earlier pipeline
Uses “NOP” -> No operation instruction
Also referred as bubbles
How does it know? By comparing registers #s, Match = Stall 

Bypass 
	If detect instruction in a stage as field in another ALU stage, use output of ALU
Utilizes many input mux to read ports

NOTE: Bypassing cannot eliminate load delays because data is not available until the WB stage

Stall -> Simple, wastes cycle, higher CPI

Bypass -> Expensive, lower CPI, and still needs stalls

More pipeline stages -> More frequent data hazards 

Compilers help a lot by rearranging code to put dependant instructions far

Speculation 
Starting execution of an instruction even when we’re unsure whether we really want it executed

Branch Prediction
	Modern CPUS dynamically predict outcome of control-flow instructions 
Predict branch condition + target 
Works because branches have repeated behavior

### NO MATTER WHAT DO NOT ALTER ISA

Exceptions
	Occur because an illegal instruction or an external interrupt 
	Causes control flow hazards 

When can exceptions happen
Memory Fault
Illegal instruction
Arithmetic exception
Memory fault 
