State: I am not stuck with anything, don't need help right now.

I'll be out of town from Thursday through Monday; I plan to work remotely but may miss or struggle to attend some meetings during that time.

## Progress

- Read FSM development
  - Started implementing the read FSM (`r_fsm.sv`). A testbench (`r_fsm_tb.sv`) is also in place and exercising the basic flows
  - I'm still working through how to correctly declare and use a new `modport` in the testbench environment
  - Reference commit (current working point):

    https://github.com/Purdue-SoCET/tensor-core/commit/b1a5706ec676a91cb63280b8233223ccb7b817e2

- `scratchpad_if` refactor and cleanup
  - The interface needs significant refactoring because the design no longer connects to the TCA and now must support two Vector Cores (VCs). This change altered the expected signals and handshaking logic
  - There is still substantial debugging to do in `scratchpad_if` to ensure it correctly handles multiple requesters and the updated control flow
  - I moved several typedefs out of `scratchpad_if` into `scpad_types_pkg` because Verilog simulators (`vlog` / `vsim`) complained about the previous placement. This central package should make the types consistently visible to all modules
  - Fixed some minor typos discovered during the refactor

## Current blockers / open items

- Finalizing the `modport` usage and ensuring the testbench exercises the new interface correctly
- Verifying `scratchpad_if` behavior with two VCs and confirming there are no handshake regressions

## Next steps

- Continue working on and iterating the `r_fsm` implementation and its testbench until the modport/testbench issues are resolved
- Finish the `scratchpad_if` refactor and run a set of focused simulation tests to validate multi-VC interactions
