# AXI + Scratchpad meeting

## Overview: 
  Dram controller team met with Akshath to discuss progress on AXI bus and any changes the back-end of scratchpad must make. 

## Meeting notes:
  - DRAM team had formulated a question:

      "Since we are split-transaction, say there is a write request, and say that the writes have been busy so the write request is stuck in the AXI queue and has not reached DRAM. Now say later in the program, a read is issued to the same address as the write. But the read passes through AXI and is in DRAM. Is that a case that needs to be handled? Does software or the cache protect against this?" 

    We were able to ask Akshath and confirm that this is not a situation we need to worry about. The scheduler will ensure the write must be acknowledged before the read gets issued. 

  - I then began presenting the interface I had created between scratchpad and AXI bus (Please check my week 7 design log to view interface image). We discussed mainly over the .size, .len, and .burst signals that the scratchpad will send to AXI upon a request.

      - .size  = "how wide each data beat is". This refers to the size of a burst. In our case the MAX physical DRAM can handle in a beat is 64 bits. This signal will be fixed to '011' which represents 8 bytes (64 bits). 4 scratchpad elements will be processed within a beat. 
      - .len   = "how long each data beat is". This refers to how many beats per transaction. So if the scratchpad wants to write a full 32 element vector: .len = 0111 (8 beats) and .size = 011 (8 Bytes).
      - .burst = Burst type. Can be fixed, incrementing, or wrap. We will keep this set to incrementing (01) as within 1 transaction, the address for each burst will just increment. 

    We also discussed about a ".last" signal that signifies the last burst of a transation. The scratchpad will generate this signal on a write. The AXI will generate this signal on a read. 
 
  - We then discussed the changes the scratchpad back-end will have to make to follow the AXI protocol. There will need to be logic to break up a scratchpad line into 64 bits (8 packets). The reasoning is the physical DRAM can only take in 64 bits at a time.
  - There also will need to be a way to encode the bursts for 1 transaction back to the scratchpad. I am thinking 3 bits since there can be MAX 8 packets in flight.
  - We discussed about data masking. My team has resolved how to mask a full burst within a transaction but the scratchpad needs masking within a burst. At initial glance this might not be possible with just the DDR masking feature and more thought must go into a solution to support masking within a burst.  
      
