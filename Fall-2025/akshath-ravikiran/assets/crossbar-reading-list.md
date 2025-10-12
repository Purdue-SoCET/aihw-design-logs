Your crossbar (xbar) is going to be a pipelined interconnect which takes in a 
- Input: 1x32 input vector of fp16 values
- Input: 1x5 input shift-mask vector
- Output: Rearranged 1x32 input vector of fp16 values.

Design Options. The "Why" is discussed below. 
- Benes Permutation MIN
- Batcher Sorting MIN 
- Naive Crossbar
- CLOS Permutation MIN

Keywords: 
- Switches (2x2) 
- Crossbar 
- NxN Crossbar
- How to pipeline a crossbar? 
- Benes Network
- Waksman Network  
- What control vector is needed for every stage in the network

```
interconnects - usually reserved for wires across metal layers in vlsi
crossbar - usually denotes the mesh network we discuss. it's the naive-est thing
interconnection network - some fabric connecting N:M units, usually used when discussing distributed computing
Multi Stage Interconnection Network (MIN) - What we want to build. pipelined, and promised latency through the system; useful for throughput systems 
switch - basic unit of a multi-stage interconnection network 
non-blocking - no contention of some common physical path; link-contention or output-port-contention possible
strinctly non-blocking - crossbar is strictly non-blocking; synthesized as a N:1 mux-tree (usually optimized to N(N-1) 2:1 mux trees) 
rearrangeably non-blocking - benes is the only true non blocking MIN 
self-routing MINs - banyan, delta and omega networks usually use the destination address itself to route implicitly, but its blocking - these 3 show link contention
```

Sorting MIN: 
```
What is Bitonic meaning? It means there is a sequence of numbers which can be SHIFTED in order to guarantee an increasing/decreasing sequence. Basically its not random shuffled. the sequence can always be defined as 1 OR 2 sorted subsequences.

What is Bitonic sort? It's any kind of MIN which can perform sort on bitonic sequences in parallel. 
What is Batcher MIN? It uses the Bitonic PRINCIPLE, to build a sorting network capable of sorting monotonic sequences (random shuffle, no seemingly ordering). Recursively sorts till you reach N/2 (basically 2 sorted subsequences), then uses a merging network to bring things back together.

Batcher-Banyan? Batcher always guarantees a sort in log_2^2(n) cycles. ONLY IF YOU ARE DOING N:M, where M > N, you need Banyan. This means if some data in the input is invalid, and you want to ignore it, then you need Banyan. Otherwise, YOU DO NOT NEED A BANYAN ROUTING AT THE END.

Thus, for our use-case, we focus on building Batcher.
```


Permutation based MIN: 
```
What is this Benes now? 
Benes promises Re-arrangeably nonblocking. Meaning any permutation can be realized, with NO LINK CONNECTION EVER. It's considered the SOTA for on-chip interconnects. More stages, but uses a Banyan like routing in the middle stages for a recursive permutation.

What is CLOS? 
Clos is like a Benes but has 3 stages. Middle stage has n > 2m-1 width, guaranteeing no blocking behaviour, cuz the middle switches are fatter than the start/end stage switches. Folded Clos trees are used in Data centers because you want any server to communicate to any other server through top-of-rack switching toplogies. 
Super cool and scales amazingly. Not needed for our usecase. We have a more realisitc number of 32.
```

- https://cr.yp.to/papers/controlbits-20200923.pdf
- https://www.cise.ufl.edu/~sahni/papers/benesSetup.pdf
- https://www.cs.utsa.edu/faculty/boppana/papers/Icc99xtra.pdf
- https://cw.fel.cvut.cz/b231/_media/courses/b4m35pap/lectures/11_interconnection_networks_b4m35pap-en.pdf
- https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/90-parallel/CrossBar.html
- https://www.cl.cam.ac.uk/teaching/1415/AdvAlgo/advalg_new.pdf (first 30-40)
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7538 (first 2 pages relevant)
- https://oasis.library.unlv.edu/cgi/viewcontent.cgi?article=3786&context=thesesdissertations (useful VLSI attempt of doing crossbars; actually worth reading 50 or so pages) 
- https://www.csd.uoc.gr/~hy534/06a/s52_fabrics_sl.pdf
- https://www.eecg.toronto.edu/~enright/interconnects-microarch.pdf
- https://www.ecb.torontomu.ca/~courses/coe838/lectures/NoC-Router-MicroArchitecture.pdf
- https://en.wikipedia.org/wiki/Bitonic_sorter -> Bitonic Sorting Network. So we'd add the permutation indices with the data as a tag, so the sorting happens on this. Since we always want the data permuted in 0->31 (L->R). 
- https://oasis.library.unlv.edu/cgi/viewcontent.cgi?article=3786&context=thesesdissertations -> Fixed cycle control-bit-vector generation
- https://cr.yp.to/papers/controlbits-20200923.pdf
- https://www.romjist.ro/full-texts/paper758.pdf
- https://www.cise.ufl.edu/~sahni/papers/benesSetup.pdf -> Convs with chatgpt always lead to Benes or Maksman networks. Benes is older. 
