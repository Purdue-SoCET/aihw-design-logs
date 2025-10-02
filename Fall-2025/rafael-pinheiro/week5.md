State: I am not stuck with anything, don't need help right now.

Progress:
- A lot of stuff changed from week 5 -> 6
  - Scratchpad not talking to TCA anymote
  - VC1 + VC2 <-> scpad <-> [xbars] <-> SRAM controller <-> SRAM
  - In practice, not a lot will change on frontend side of things
  - handshake signal will be sent to VC's, indicating scratchpad is ready for new signals
- Presentation presented at AI Hardware Design Review presentations
- VC folks seem to understand what's going on on our end & how VC's <-> scpad.frontend communication is.

- RTL Diagrams done
  - https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22%7D
  - Flow: 1R1W request per VC. Both VC's may request at the same time
    - Writes:
      - write data sent frontend -> crossbar, will take a couple cycles swizzling
      - write description either latched or FIFO'dso it is synchronized with wdata swizzling
      - {wdata, desc} latched and sent to SRAM controller
      - SRAM controller sends response
    - Reads:
      - read data sent SRAM -> crossbar, will take a couple cycles swizzling
      - response description either latched or FIFO'dso it is synchronized with rdata swizzling
      - {rdata, resp} latched and sent to SRAM controller
      - SRAM controller sends response
  - FSM's:
    - Both reads and writes are very similar
    - Might merge them together into just one FSM, since requests will be 1R1W
    - IDLE -[req.valid && (w/r)]-> MAKE_XBAR_DESC -> REQUEST_XBAR -[!ctrl_ack]-> ISSUE_SRAM -[sram_(r/w)_res.valid]-> RESP_DONE -[complete & (!_req)]-> IDLE
      -  -[complete & (_req)]-> MAKE_XBAR_DESC
   -  Busy r/w bits activated when not in IDLE/RESP_DONE

Next Steps:
- Start coding FSM's