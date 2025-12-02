State: I am not stuck with anything, don't need help right now. This week might be slow due to Thanksgiving and not being able to communicate with folks who are out of town. I'll be working on this regardless though

## Progress summary

### Understanding Vector Core's Scheduler

#### High-level contracts

##### Inputs

- Fetched instructions from fetch stage
- Writeback notifications
  - Reg/matrix writes
  - GEMM/load completions
- Functional unit completion flags
- Branch resolution/misprediction signals

##### Outputs
- Single issued instruction/cycle to execute (issue -> execute ctrl + ops)
- Freeze/halt/jump signals back to fetch

##### Error or other special modes

- Branch mispredictions handled by flushing the speculations
- Avoid structural hazards (RAW/WAR/WAW) via tags and busy tracking

##### Success criteria

- Only issue instructions whose operand dependencies are cleared
- Respect structural hazards
- Choose oldest-ready intruction when multiple are ready

#### Key components

##### Dispatch

- Decodes fetch instruction & decides which FU it needs
- Creates the next [FUST] (functional unit status table) entries ([diif.n_fust_*]) and tag ([diif.n_t*]) information
- Maintains reg-status tables that record which FU will write each scalar/matrix reg and a "spec" for speculative writes
- Hazards: computes hazard and WAW detection
  - Scalar side: [s_busy] depends on which scalar FU is busy
  - Matrix side: [m_busy] for matrix ld/st and GEMM
  - WAW: reg-status tables - if destination marked as busy, dispatch stalls
- Speculation: [spec] bit for instructions after branches, [flush] clears speculative entries
- Outputs [diif.out] (->scoreboard/issue) and [diif.freeze] (stall fetch when hazard)

##### Scoreboard
- Wires [dispatch] and [issue]
- Propagates fetch/dispatch outputs to [issue], passes writeback and [fu_ex] from mem/ex to dispatch & issue

##### Issue
- Hosts FUST FSM:
  - 5-entry set:
    - 3 scalar FUs
    - Matrix LD/ST
    - GEMM
  - [FUST_EMPTY], [FUST_WAIT], [FUST_RDY], [FUST_EX]
- Latches [fust_*] [<=] [n_fust_*]
- Dependency (tag) system:
  - Each FUST entry carries tag fields [t1], [t2] (for GEMM [gt1], [gt2], [gt3]) indicating producers for operands
  - [rdy] [<=] [n_rdy] checks whether tags are clear (no outstanding producers). If cleared, FUST entry is ready
- Age based arbitration:
  - [age] counter per FUST entry, incremented when new instructions for the FU arrive
  - Used to prefer older ready instructions
  - [oldest_rdy] tracks which entry has been ready for the longest
- Issue policy:
  - Single-issue core: only one FU instruction issued/cycle
  - Multiple FUs ready: prefer oldest ready
    - Tie-breaking: [single_ready]/[fu_ready] logic
  - When FSM WAIT/RDY->EX, [issue] output populated with operand values from regfile, control, [fu_en] for execute stage
- FUST FSM transitions depend on:
  - [branch_miss] -> speculative entries cleared
  - [n_rdy] and arb result -> FUST_EX and emit issue outputs
  - [fu_ex] arrives: FU done. EX->EMPTY/WAIT (if new incoming instr)
- Output to Execute:
  - [out] containing:
    - [fu_en]
    - operands [rdat1]/[rdat2]
    - [alu_op]
    - [mem_type]
    - [branch] info
    - GEMM params ([ms1]/[ms2]/[ms3])
    - [spec] for speculative execution

##### Register/matrix status and tags
- [rstsif] scalar reg status and [rstmif] matrix reg status track pending writes and tags
- Dispatch sets [rst*.di_write] when it issues an instruction that will write to regs/matrices
- WB stage clears status entries([rst*.wb_write])
  - Also provides [wb] fields that dispatch/issue use to clear tags
- Tags ([t1],[t2],[gt1],[gt2],[gt3]) used by issue logic
  - tag != 0 -> some earlier instruction will produce the operand
  - tags cleared when producing instruction completes and wb occurs

##### MEM/GEMM interaction
- GEMM treated as heavyweight FU: FUST index 4
- Matrix ld/st (index 3) and GEMM have their own tag semantics  ([n_gt1], [n_gt2], [n_gt3], [n_m_t2])
- Datapath interface connects [scoreboard]/[execute] to memory/cache interfaces and [scheduler_core] maps that to caches/scratchpad/arbiter
- Memory arbiters in [memory_systolic_array] and [memory_subsystem]
  - Serialize/conflict-resolve accesses from multiple masters (datapath, scratchpad...)

### Typical instruction flow

#### 1- Fetch

- Reads PC/instruction
- Produces [fetch]

#### 2- Dispatch

- Decodes instruction
- Computes:
  - FU target
  - Destination/source registers
  - Mem types
  - Speculation bit
- Hazard check (structural and WAW)
  - If a hazard exists, [freeze] is asserted (freeze fetch and hold instruction)

#### 3- Scoreboard

- Copies dispatch comb outputs into [issue] inputs

#### 4- Issue

- Reads current FUST entries and tags and regfile values
- Computes [n_rdy] (dependency-free) by checking tag fields; update [age] counters
- Selects which ready FU to issue this cycle using tie-breaking policy (oldest/single)
- When chosen, [issue] asserts fu_en for that FU and supplies operands and control signals to [execute]
- On issue, FUST entry goes to [FUST_EX]. [fu_ex] tells the issue when FU finishes

#### 5- Execute

- Perform ALU, mem LS, matrix LS, GEMM ops
- Mem/GEMM operatuins interact with [dcif] and arbiters to access scratchpad/DRAM as beeded
- On completion, [execute] sets [fu_ex] bits and relevant complete flags ([load_complete], [gemm_complete]...)

#### 6- Writeback

- Completed results written back (regs/scratchpad), writeback signals clear reg/matrix status tags
- Clearing tags causes dependent FUST entries to become [rdy] in next cycle
  - Age logic as tie-breaker when multiple are ready

### Issue policy and arbitration details
- Single-issue core
  - Only 1 instruction issued at a time
- Readiness
  - Scalar FUs (indices 0-2) ready when scalar tag fields for the FUST are 0 (no pending producers)
  - Matrix LD/ST ready when matrix tags are 0
  - GEMM ready when [gt1]/[gt2]/[gt3] are zero
- Arbitration
  - If exactly one FU is ready, issue it
  - If multiple are ready, prefer oldest-ready based on [age] and [oldest_rdy] logic
  - [single_ready] and [fu_ready] logic compute single-bit masks to simplify tie-breaking
  - Branch-misprediction handling: speculative FUST entries cleared (the ones with [spec]). [fetch] and [dispatch] flushed
- FU busy detection and re-entrancy
  - Dispatch checks [fust_*.busy] and [fu_ex] to know whether FU type is currently busy/finishing
  - E.g.: dispatch's scalar [s_busy] calculation uses [fu_ex] and [fust_s.busy] to determine if it can allocate new scalar FU instruction

### Speculation handling

- Dispatch marks speculative instructions with [spec] when they follow a branch
- Issue respects [spec]
  - Some FUs treat [spec] specially and wpn't advance speculative instructions the same as non-speculative instructions (see [FUST_Next_State]) 
- On [branch_miss], dispatch/issue clear speculative entries (set [FUST_EMPTY]) for instructions that were speculative (and also clear branch-related state)

### Memory/GEMM schedulung notes

- GEMM and matrix loads are structurally heavy - dispatch sets [m_busy] and prevents issuing conflicting operations
- Memory arbiter modules serialize accesses from multiple masters and present [load_complete]/[gemm_complete] back to [sc_datapath], which informs the scoreboard
- [n_fust_g.new_weight] and similar fields manage GEMM-specific behavior like reusing weights loaded in scratchpad

### Signals to look at

- Dispatch
  - [out] - dispatch output (-> issue)
  - [freeze]
  - [n_fust_*], [n_t1-2], [n_gt1-3] - comb FUST/tag updates
  - wb - carry wb completes (-> dispatch)
- Issue
  - [out] - issue output (-> execute)
    - [fu_en], operands, control
  - [fust_state] - curr states of FUST entries
  - [fu_en]/[fu_ex] - issue enables and FU completions
  - [branch_miss]/[branch_resolved] - control for speculation
- Global
  - [sbif] (scoreboard interface) - combined interface b/w dispatch + issue + execute + writeback
  - [dcif] (datapath cache interface) - memory signals (imem/dmem/gemm interactions)

### Edge cases

- Branch missprediction
  - All [spec] [FUSTs] and certain register status are cleared
  - [branch_miss] shows flushing
- WAW detection
  - [dispatch] uses reg-status tables
  - If tables are stale/writeback signals delayed, [dispatch] may unecessarily stall
  - Single-issue bottleneck
    - GEMM and matrix LS can block throughput if they’re long latency and many scalar instructions are waiting on them due to shared tags
  - Tag clearing
    - tags are cleared on the specific kinds of writeback ([alu_done] / [load_done] / [gemm_done] / [jump_done])
    - ensure the path from execute -> writeback -> scoreboard -> dispatch/issue is not losing cycles if you trace timing

## Next Steps

- Start modelling Scheduler Core on atalla-sim
- Write unit-tests for scheduling instructions to the Vector Core
- 