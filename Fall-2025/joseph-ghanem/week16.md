**State:** Debugging 1 issue

# Progress

## 1) Implemented Result Collector (result_collector.sv)
Built a top-level `result_collector` that instantiates one `rc_fu` per FU and fans in per-lane results (`result/valid/vd/elem_idx/last`). Wired writeback-valid/result/vd per FU to `rc_out`, and generated a per-FU ready aggregation across lanes.

## 2) Integrated RC + Reduction into Top-Level (vector_datapath.sv)
Integrated:
- `result_collector` as the normal FU writeback path (`rc_out -> vector_out`)
- VALU reduction path via `vreduction_if` + `vreduction` when `rm=1` and `fu_sel==VALU`
- MaskU hookup (select-first-valid issue slot) feeding each lane’s mask slice
- Robust lane input mapping: kept **ready** combinational, but **registered** v1/v2/vmask/vd/vop/rm/valid_in to stabilize what lanes sample under backpressure and multi-issue.

## 3) Built End-to-End Datapath TB (vector_datapath_tb.sv)
Created a full top-level TB that:
- Drives `vector_in[0]` with slice-expanded vectors
- Adds MUL-specific WB backpressure by toggling `vif.rc_in.ready_in[*][MUL]`
- Runs directed SQRT + MUL tests and stress tests:
  - upstream starvation (random gaps)
  - heavy WB backpressure
  - long random run
  - all-zero-mask “no results allowed”
- Uses scoreboard + (vd, elem_idx) matching (bag semantics for random tests) and a handshake-observer monitor (`valid && ready`).

## 4) Standalone RC TB (result_collector_tb.sv)
Built a standalone smoke/directed TB for `result_collector + rc_fu` that directly drives `rc_in` (no lanes) and checks:
- correct FU routing (MUL then DIV)
- WB backpressure stability (result/vd must not change while stalled)
- a “fast last lane” race test to expose ordering/collection bugs

# Bug Being Investigated (suspected handshake / backpressure)
Observed a failure where **RC applies backpressure to the lanes and metadata gets lost** (vd / elem_idx mismatch or dropped items). I suspect a **valid/ready handshake mismatch** where:
- lanes may advance/retire metadata when RC is not truly accepting, or
- RC/`rc_fu` may be sampling inputs without holding state stable across stall cycles,
causing drops or misalignment between `result` and `(vd, elem_idx, last)` under WB backpressure.

evidence: https://github.com/Purdue-SoCET/atalla/tree/vector_core_fa25

## 5) Report
Sections contiribtued to:
- 1.3 Valid/Ready Handshake
- 1.4 Predication

- 2.2 Vector Datapath Architecture
- 2.2.1 Considerations
- 2.2.2 Prior Work
- 2.2.3 Initial Design
- 2.2.4 Vector Datapath Architecture
- Lane Datapath

- 2.3 Vector Register File
- 2.3.1 Considerations
- 2.3.2 Prior Work
- 2.3.3 Vector Register File

- 3.1 Lane Unit
- 3.2 Vector Register File
- 3.2.1 Overview
- 3.2.2 Banking
- 3.2.3 Control Logic & Conflict Management
- 3.2.4 Operand Collector

- Section 4: Results
- 4.1 Unit Performance
- 4.3 Power and Area Breakdown
- 4.4 PCacti Results

- Section 5: Results Discussion
- 5.3 PCACTI Analysis

- Section 6: Limitations
- 6.3 Future Work

Evidence: https://docs.google.com/document/d/1_8fxII3308U6oHTUsFgIpE2MNWtf03bf1tetJ6z-sRA/edit?usp=sharing

# Future Plans
- Fix/verify the RC↔lane handshake so stalls never drop or reorder metadata
- Extend top-level tests beyond MUL (DIV/SQRT/VALU) and add reduction-specific system tests
- Re-run stress with randomized WB backpressure across multiple FUs
