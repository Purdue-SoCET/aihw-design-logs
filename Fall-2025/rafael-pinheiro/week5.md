```markdown
State

I am not stuck on any tasks right now and do not need immediate help.

## Progress summary

- System topology changes (week 5 -> week 6):
  - The scratchpad is no longer communicating directly with the TCA (that connection was removed)
  - Current data path (logical): VC1 and VC2 <-> scratchpad frontend <-> [crossbars] <-> SRAM controller <-> SRAM
  - These changes do not significantly affect the frontend’s internal design—most frontend responsibilities remain the same
  - A handshake signal will be provided to the Vector Cores to indicate when the scratchpad frontend is ready to accept new requests

- Presentation:
  - Presented the design at the AI Hardware Design Review. The VC team appears to understand the frontend contract and how VC ↔ scratchpad.frontend communication will work

## RTL diagrams

- Diagrams are complete and show the data/control flow and module boundaries:

  https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22%7D

- Transfer flow and synchronization notes:
  - Each Vector Core issues 1R/1W request capability; both Vector Cores may request at the same time and the frontend arbitrates between them

  - Writes:
    - Write data produced by the VC is sent to the frontend and then routed through the crossbar. The crossbar/swizzle path takes a few cycles to complete the swizzling/aligning of per-lane data
    - The write descriptor (meta information that describes the write) must be synchronized with the write data. It can be latched or FIFO’d so that it lines up with the write data after swizzling
    - Once the aligned write data and its descriptor are ready they are latched together and forwarded to the SRAM controller
    - The SRAM controller eventually issues a response indicating write completion

  - Reads:
    - Read data flows from SRAM through the SRAM controller and crossbar; the read data path also requires a few cycles for swizzling/aligning before it reaches the frontend
    - The read response descriptor (metadata describing the response) must be synchronized with the read data; it can be latched or buffered so the two arrive together
    - The frontend latches the `{rdata, resp}` pair and forwards it to the requester
    - The SRAM controller issues peripheral responses as part of the completion handshake

## FSM design notes

- Observations:
  - The read and write control flows are quite similar in structure. Given the 1R/1W nature of requests from each VC, it may be simpler to implement a unified FSM that handles both directions rather than two separate FSMs

- Sketch of the intended state sequence (compact form):

  IDLE -[req.valid && (w/r)]-> MAKE_XBAR_DESC -> REQUEST_XBAR -[!ctrl_ack]-> ISSUE_SRAM -[sram_(r/w)_res.valid]-> RESP_DONE -[complete & (!_req)]-> IDLE

  - If another request remains after completion, transition back to MAKE_XBAR_DESC to service the next request
  - Busy read/write indicators should be asserted whenever the FSM is not in IDLE or RESP_DONE

## Next steps

- Begin implementing the FSM(s) in RTL and iterating on the synchronization logic between wdata/rdata swizzling and descriptor handling
```markdown