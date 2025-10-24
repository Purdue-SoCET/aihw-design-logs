State: I am not currently stuck or blocked. 

Progress: 
- met on Friday, Saturday, Sunday, and Monday

- I worked on writing up the intro sections of the paper, discussing the drawbacks of scoreboard and superscalar for our applications. We decided not to do them due to power and area constraints. 
  - Widening the superscalar -> way too much area, power, hardware complexity
  - Scoreboard -> Max CPI = 1 due to Flynn's bottleneck
  - VLIW allows us to exploit ILP while keeping hardware simple (more difficult for compiler)

- Compiled design decisions for dependency register
  - Green Zone Guarantee: if a packet depends on an instruction that is guaranteed to complete within a known maximum number of cycles, then any packets issued after that latency window can safely assume that the dependency has been resolved
    - Why? - Don't need to check an extra thing if you KNOW it will be done
  - Suppose we have two packets, packet 1 and packet 2, both dependent on packet 0, and packet 1 is going to be issued before packet 2. Let us say packet 0 has a set field of 16’b00001000, so bit 3 is set high. In this scenario, only Packet 1 needs to check bit 3 in the dependency register. Packet 2 does not need to check this bit because once Packet 1 is issued, we already know that the dependency on Packet 0 has been accounted for
  - Every packet's check field must check the bit it is trying to set to avoid clobbering state and overwriting something 
  
- Considered implementing a CSR for vector ops
- Vector also might need to access scalar data so have to be aware of this to avoid bank conflicts
  - Will need to access for mask, l/s and vector scalar operations

- I wrote the architecture portion of the spec 
- We developed the slides for our design review
  - Presented design review to GTAs and compiler team and answered their question
  - Sooraj brought up the point that if we don't put short latency intr together with long latency instructions, we might not actually be improving performance with this method - need to look into to see how this idea plays out in our design to see if we are making the performance improvements we want


Next Steps: 
- Low level diagrams
- Complete and deliver the compiler spec with all worst-case latencies
- Need to meet with vector team



