State: Quite overwhelmed with amount of information, might need help in near future

Progress:
(09/16)
- Top level, interfaces and communication with vector core, systolic array, SRAM controller and crossbar defined
- {vec, sys}_if
  - Inputs:
    - start_addr
    - row_id
    - col_id
    - row_len
    - col_len
    - is_col
  - Outputs:
    - valid_mask
    - done_{vec,sys}
    - arr_{vec,sys}
    - stall_sys [ONLY FOR SYSTOLIC ARRAY]
- Outputs of Scratchpad Frontend:
  - To SRAM Controller:
    - slot_mask
    - REN
  - To Crossbar:
    - shift_mask

Next steps:
- Figure out inner modules
- Start Working on RTL code