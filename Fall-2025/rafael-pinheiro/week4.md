```markdown
State

Quite overwhelmed by the amount of information and details right now. I may ask for help soon to clarify interfaces and implementation responsibilities

## Progress

### 2025-09-16

- Defined the top-level block and the primary interfaces that govern communication between the key components: the Vector Core (VC), the Systolic Array (SA), the SRAM controller, and the crossbar. The system diagram is available here:

  https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22Tro5ICBytG0uPzhBu2ZE%22%7D

- Interface summary (`vec_if` and `sys_if`):

  - Inputs (from VC / SA into the scratchpad frontend):
    - `start_addr` — tile or transfer start address
    - `row_id` — logical row index used for swizzling/addresses
    - `col_id` — logical column index
    - `row_len` — length of the row in elements
    - `col_len` — length of the column in elements
    - `is_col` — direction flag (column-oriented vs row-oriented transfers)

  - Outputs (from the frontend back to the requestors / system):
    - `valid_mask` — per-lane or per-bank validity mask for partial transfers
    - `done_{vec,sys}` — transfer-complete signals for the Vector and System interfaces
    - `arr_{vec,sys}` — aggregated or per-lane data returned to the requestor
    - `stall_sys` — back-pressure to the Systolic Array (only used for SA)

- Outputs produced by the Scratchpad frontend toward lower-level blocks:

  - To the SRAM controller:
    - `slot_mask` — which bank slots are active for the current beat/transfer
    - `REN` — read-enable / request enable signal to the SRAM controller

  - To the crossbar (when relevant):
    - `shift_mask` — used to align lanes/columns when routing data through the crossbar

### 2025-09-21

- Attended the Sunday design meeting and made updates to the diagrams. The main changes focused on how the frontend communicates with the SRAM controller; that communication is now represented more explicitly

- Summary of the current arbitration and service model:

  - Both the Vector Core (VC) and the Systolic Array (SA) send requests to the Scratchpad frontend (SC.FE). The frontend is responsible for arbitrating those requests

  - Inside the scratchpad, an arbiter decides which request to service next. At present VC requests are given priority over SA requests. If VC and SA both assert requests simultaneously, the SA is stalled until the VC request is handled

  - Each accepted request is processed by a Service FSM inside the frontend. The Service FSM encapsulates the sequence of steps required to issue lower-level requests to the SRAM controller and to complete the high-level request once a `RESPONSE DONE` is received from the SRAM controller

  - The frontend's external communication surface is intentionally limited: it directly talks only to the VC, the SA, and the SRAM controller. It does not talk directly to the crossbar for request arbitration (the crossbar is handled downstream)

  - Updated diagram (reflecting the SRAM-controller changes):

    https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22inImMLElQ-h5i9CkQv97%22%7D


## Action items / TODO

- Complete the remaining microarchitecture work inside the frontend (my immediate responsibility is finishing the Service FSM logic and verifying its interactions with the arbiter and SRAM controller)
- Update the diagrams and RTL to use the signal names from the package (`pkg`) interface that Akshath provided, so the documentation and implementation use the same naming conventions

## Next steps

- Confirm the set of inner modules for the frontend (the current draft suggests the service FSM, arbiter, slot-mask generator, and swizzle units) — status: mostly identified
- Start implementing RTL for the frontend and the Service FSM

```markdown