Your crossbar (xbar) is going to be a pipelined interconnect which takes in a 
- Input: 1x32 input vector of fp16 values
- Input: 1x5 input shift-mask vector
- Output: Rearranged 1x32 input vector of fp16 values.


Keywords: 
- Switches (2x2) 
- Crossbar 
- NxN Crossbar
- How to pipeline a crossbar? 
- Benes Network
- Waksman Network  
- What control vector is needed for every stage in the network

- https://cr.yp.to/papers/controlbits-20200923.pdf
- https://www.cise.ufl.edu/~sahni/papers/benesSetup.pdf
- https://www.eecg.toronto.edu/~enright/interconnects-microarch.pdf
- https://www.ecb.torontomu.ca/~courses/coe838/lectures/NoC-Router-MicroArchitecture.pdf
- https://en.wikipedia.org/wiki/Bitonic_sorter -> Bitonic Sorting Network. So we'd add the permutation indices with the data as a tag, so the sorting happens on this. Since we always want the data permuted in 0->31 (L->R). 
- https://oasis.library.unlv.edu/cgi/viewcontent.cgi?article=3786&context=thesesdissertations -> Fixed cycle control-bit-vector generation
- https://cr.yp.to/papers/controlbits-20200923.pdf
- https://www.romjist.ro/full-texts/paper758.pdf
- https://www.cise.ufl.edu/~sahni/papers/benesSetup.pdf -> Convs with chatgpt always lead to Benes or Maksman networks. Benes is older. 
