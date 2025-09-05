State: I am currently not stuck or blocked. 

Notes: 

Chapter 7
- Pipelining
    - Overlapping processing of a sequence of inputs
    - slowest pipeline stage determines rate at which inputs move through pipeline
- 2 performance metrics: Latency vs Throughput
    - latency: time it takes for system to process a particular input
        - latency of pipelined system = num_stages * clk_period
    - throughput: rate at which system produces outputs
        - to increase throughput we use registers to divide processing into sequence of stages
- How to Pipeline Effectively
    - K-Pipeline: circuit with K registers on every path from input to output
        - If not same number of registers across all paths, we can get incorrect results
    - Strategy
        GOAL(normally): max throughput using fewest possible registers
        
        1. Draw contour line that crosses every output
        2. Draw contour lines between terminal point across the signal connection, trying to isolate slowest sytem component
        3. Place a pipelined register wherever a signal connection intersects the pipelining contours
        4. Determine system's clock period by looking for pipeline stage with longest reg-to-reg or input-to-reg propagation delay
        
        - Pros: increase throughput
        - Cons: increase latency, bottleneck problem 

    - Bottleneck Fixes (to further increase throughput): 
        - swapping out a component for a pipelined version
        - replicate the critical element and alternate inputs between various copies
        - can run pipelined systems in parallel 


Chapter 14
- Memory Technologies
    - Static Random-Access Memories (SRAM)
        - Designed for low latencies to thousands of locations (sacrifice capacity)
        - array of memory locations (mem access is reading or writing all bits ina  location)
    - Dynamic Random-Access Memories (DRAM)
        - Optimized for capacity and low cost (sacrifice access latency)
    - Non-volatile memories
        - used to maintain system state even when system is powered down
        - highest latency, highest capacity, and lowest cost per GB
        - Ex: Flash, Hard-disk drive
- Memory Hierarchy Interface
    - Expose hierarchy to user vs hide hierarchy and handle behind scenes
- Cache
    - Small, interim storage component that transparently retains data from recently accessed locations
    - very fast if data is cached
    - SRAM component of our memory hierarchy is called a cache
    - speeds up access to frequently accessed locations
    - Metrics: Hit (data in cache) ratio, miss (data not in cache) ratio, AMAT (Average Memory Access Time)
    - Direct Mapped Caches
        - each word in memory  maps into a single cache line
        - can increase block size to take advantage of locality (use AMAT formula to optimize block size - common size is 64 bytes)
    - Fully Associative Cache
        - Any address can be in any location (no cache index)
            - very flexible but expensive 
    - Set Associative Cache 
        - multiple DM caches operating in parallel
    - Design Decisions
        - Replacement Policies
            - More intelligent replacement: lower miss rate, higher cost
        - Write Policies
            - write through: update memory immediately
            - write behind: update to main memory may be buffere
            - write back: update only when replacing dirty cache line (best strategy - can use dirty bit)
    - Many Tradeoffs - best navigated by simulating different cache organizations


Chapter 15
- Original Beta CPU
    - want to improve performance
    - only executes one instruction per clock cycle
    - Cumulative delay from all components determines clock period (t_clk)
- Pipelining
    - Stages: 
        1. Instruction Fetch - maintains PC, fetches instruction and passes to RF stage
        2. Register File stage - reads source operands from reg file and passes to ALU stage
        3. ALU stage - performs operation in ALU and passes to memory stage
        4. Memory Stage - if load, use ALU result as address and pass data (or ALU result) to write back stage 
        5. Write-Back stage - writes result back to reg file
- Hazards
    - instruction may depend on something produced by an earlier instruction (data hazards and control hazards)
    - Strategies (Data Hazards): 
        1. Stall - wait for result to be available by freezing earlier pipeline stages
            - Pros: simple; Cons: wastes cycles, higher CPI
        2. Bypass - route data to earlier pipelined stage as soon as it's calculated
            - Pros: Lower CPI; Cons: More expensive
    - For Control Hazard: 
        1, 2. Same as above
        3. Speculation
            - Guess a value and keep executing
            - When value available, 
                1. Guess correctly -> do nothing
                2. Guess incorrectly -> kill and restart with correct value
- Branch prediction
    - Speculation wastes resources for jumps and taken branches so modern CPUs (ex: Intel Nelahem) use sophisticated branch prediction 
- Exceptions
    - implicit branches that cause control flow hazards
    - When exception occurs, need to ID affected instruction and annul affected and following instructions by replacing with NOP
    - exception can occur in multiple stages
    - in case of multiple exception, instruction furthest along the pipeline takes precedence

    
