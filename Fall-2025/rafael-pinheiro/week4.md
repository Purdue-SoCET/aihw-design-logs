State: Quite overwhelmed with amount of information, might need help in near future

Progress:
(09/16)
- Top level, interfaces and communication with vector core, systolic array, SRAM controller and crossbar defined
- https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22Tro5ICBytG0uPzhBu2ZE%22%7D
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

(09/21)
- Attended Sunday meeting
- Changed some stuff at the diagrams, more specifically related to the communication with the SRAM controller
- Long story short:
  - Requests are sent from Vector Core (VC) and Systolic Array (SA) to Scratchpad (SC), arbitrated by frontend (SC.FE)
  - Whithin Scratchpad, arbiter decides which request to take. VC > SA
    - If both asserted, stall SA
  - Request handled by a Service FSM
    - Handles logic related to issue requests to SRAM and finish requests when receiving RESPONSE DONE.
  - Frontend only communicates w/ VC, SA and SRAM controller
    - Not XBAR!
  - https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22inImMLElQ-h5i9CkQv97%22%7D
- TODO:
  - Adjustments and finish microarchitecture whithin frontend (on my end, Service FSM)
  - Use signals used in pkg interface provided by Akshath in diagrams
Next steps:
- Figure out inner modules [done?]
- Start Working on RTL code