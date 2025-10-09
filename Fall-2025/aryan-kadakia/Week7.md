# Week 7

## State:
I am not stuck with anything, would like to get a better understanding of the lock-free cahce and it functionality as it impacts a development of both the AXI bus and Non-blocking DRAM controller. 

## Progress:

## Questions:
  - Since we are split-transaction, say there is a write request from dcache, and say that the writes have been busy so the write request is stuck in the AXI queue and has not reached DRAM. Now say later in the program, a read is issued from dcache to the same address as the write. But the read passes through AXI and is in DRAM. Is that a case that needs to be handled? Does software or the cache protect against this? --ask akshath.

  - Does program order need to be maintained in AXI/DRAM controller?

  - In the AXI queues, should we pop the request when it passes through into AXI or when it gets a response back. I think it should pop when we get a response back. This is much safer but add slightly more complexity. We will need to leave a copy of the request in the queue when the original request gets passed into AXI. Then, there must be a pointer so other requests are able to get issued. Then once the response is sent out from DRAM then into AXI, we can safely clear the copy of the request from the queue. Moving foward when we add out-of-order to the non-blocking controller, we will have to copy the pointer along with the request to avoid converting the queues into CAMs.

## Future Steps:
Moving forward, I would like to finalize the top-level RTL for the AXI-bus. We have finalized the interface for the AXI bus and have a rough draft of a top-level, but would like by next week to have a finished top-level that we can present to Sooraj and make receive feedback. 
