- think about when reads comeback, since its double data rate. how can it be safely implemented (CDC issues)

- think about when the arlen can come back to axi bus. Would want a "rlen" upon a read response so nwe know how much beats did to be de-appended from the reading response. The "rlen" should be known on the first cycle of a read beat but we then we need to decide when to pop the read request off of the load queue in the memory controller.  
