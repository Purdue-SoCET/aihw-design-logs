# Week 5 Design Log

## State:
I am a bit stuck on figuring out how to deal with the recursion and the extra latency caused by it.

## Progress:
- The logic assumed from the previous week was wrong.
- I understood the logic of connecting output of a stage to the input of next stage.
- The control bit generation (CBG) is more complicated that expected. We fould a python code for control bit generation logic.
- The problem with this logic is the recursion with N=16, 8, 4, 2. This may not be easily mapped to hardware.
- One option to do recursion in hardware is simply extending the recursions to happen one after another. This increases load.
- Due to the high load, CBG also needs to be pipelined, increasing latency of permutation.
- Realized that all the CBG needs to be completed before the execution of Benes network. This means that we cannot overlap the CBG stages to the crossbar stages

- Did a design review presentation with the researched information above.
- Personally, I was less worried at myself after the design review, because I thought that I simply did not have the skills to figure out the logic for CBG and Benes network. During the design review, Sooraj, Akshath, and some other students also mentioned the difficulty of implementing Benes network.

## CBG and Benes network logic:
- Connection of input to the output of next stage includes a specific assignment for N=32. Since this is a pre-defined value, no specific calculation or logic is needed.
- The CBG logic includes multiple forward and reverse permutations, which are consisted of comparators using xnor and two of 32 into 1 mux each. The example circuit of N=8 is shown in the "reverse_permutation" image. To compute the reverse permutation, we first select the desired target to compare using 32 to 1 mux. This may be represented as a mux tree of multiple 2 to 1 muxes. Then, this value is compared with all the permutation values using xnor gates. For the value that matches all the bits as the target, the corresponding index value is taken. Then the 1 to 32 reverse-mux is used to put the matched index value to the index of target, creating a inverse permutation array. For forward permutation (finding pi[target]), the index value is connected to the xnor instead of the actual value of pi.
- The recursion exists for CBG, which will need to be dealt.
- the main point of my crossbar is that there is no handshake signal. The CBG and Benes network stages are constantly doing calculations through pipelines and producing output, even if there is no meaningful input. It simply does the caluculations with the input data and permutation index.


## Next Steps:
- Akshath suggested trying the LUT, which Duc will look into, while I do more logical thinking on the CBG.
- Dig deeper with the workload of each recursion stage to divide them into equal pipelined stages.
- Understand ways to minimize latency of CBG.

## Reference and images:
- control bit generation logic is from "controlbits" pdf. A screenshot of the python code is "CBG_python_code".
- An top level RTL of the crossbar is "crossbar_RTL_top"
- A simple breakdown of CBG workload for N=32 is shown in "CBG_pipeline_N32".