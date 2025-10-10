## State: 
I am not stuck with anything, would like to discuss size options for axi queues. Max amount of requests till we start backpressure. 

## Progress:
This week I spent time reading over the ARM AXI protocol overview and documentation. I will like both below. After reading the documentation. I was able to establish a good understanding of the protocol. And what feature of AXI, we should include in our implementation.
I decided that the features would consist of: 1) Split transactions 2) 5 Channels: AR/R (reads), AW/W/B (writes) per memory system​ 3) Transaction tags to track requests​ 4) VALID/READY handshakes​ 5) INCR Burst​. The documention mentioned other features like out-of-order write interleaving and atomicity in AXI. I choose at this time, they will not ne needed in this implementation. 

I was able to then read on the 5 channels used in the protocol and put together a very abstracted view of the interface between the AXI bus with the I$/D$ and Scratchpad. I have placed this top-level view in the images/folder. 

Then, this past sunday. Me and the DRAM team presented our design review where I shared my progress on verifying the timing requirments, understanding the blocking controller, and efforts towards non-blocking. 

Into the week, I begin looking at the interface files from the scratchpad and the non-blocking cache to understand what signals and sizes they are sending to the DRAM, and how the AXI bus can adapt to those signals and if any changes need to be made. Now I am finishing up the full interface of the top-level where I go into each of the 5 channels and determine the size and specific signal needed into the AXI bus. I will finish up this diagram and begin looking into components needed for the non-blocking conttoller for next week. 
