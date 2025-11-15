# Week 11 Design Log

## State:
Currently not stuck on anything

## Progress:
- Finished pipelining and parameterizing CBG code.
- Collaborated with Saandiya from systolic array team.
- Introduced Benes to her, and she said she needed to use it for a bit shifter.
- Told her that she would need to generate permutation array that matches the desired output order.
- Discussed on how the bit shifting and padding 0s would look like and agreed that this would need to be done from systolic array, not with Benes, because Benes only allows cyclic shifting.

## CBG pipelining and parameterization
- I first counted the amount of composeinv and find_min calls, with taking account of the number of for loop iterations.
- With the module counts, I applied the weight of load for each, considering how much work is done in each module. I decided that composeinv is double weight of find_min, because composeinv iterates through the index of search array and maps it to the value of permutation array, which requires extra iteration with muxes. Find_min, on the other hand, just needs single iteration with comparison.
- Added up all the weighted module counts and divided it into 5
- Searched through the code to determine where that divisions should be placed
- Added pipeline to start next step on the pipelined values.
- Problem with this was that the number of depth and for loop varies depending on the N value. Therefore, the load changes, meaning that location for each pipeline changes. Because the pipeline locations are specific to N=32, pipelining cannot be parameterized.
- Therefore, CBG is not parameterized and only works for N=32.
- The synthesis result was too bad for CBG, because clock speed is too slow, area and power is too large compared to Benes. Because Benes runs perfectly fine with single cycle, adding more clock to match the clock speed won't make sense, and there is really no point anymore to use such an inefficient CBG for super fast Benes.
- We are not considering CBG + Benes anymore as an optimal solution for crossbar


## Next Steps:
- Sooraj suggested that I look into clos network as an alternate solution to crossbar
- Prepare for a second design review with Prof. Anand that will happen on Tuesday.
- Work on VIP presentation poster.

## images:
- synthesis_benes.png
- synthesis_CBG.png