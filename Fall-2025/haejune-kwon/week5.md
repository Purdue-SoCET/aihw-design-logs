# Progress:
- Understood the logic of connecting output of a stage to the input of next stage: It includes a specific assignment for N=32. Since this is a pre-defined value, no specific calculation or logic is needed.
- The control bit generation (CBG) is more complicated that expected. We fould a python code for control bit generation logic.
- The CBG logic includes multiple forward and reverse permutations, which is simply a comparator using xnor and 32 into 1 muxes.
- The problem with this logic is the recursion with N=16, 8, 4, 2. This may not be easily mapped to hardware.
- One option to do recursion in hardware is simply extending the recursions to happen one after another. This increases load.
- Due to the high load, CBG also needs to be pipelined, increasing latency of permutation.
- Realized that all the CBG needs to be completed before the execution of Benes network. This means that we cannot overlap the CBG stages to the crossbar stages

- Did a design review presentation with the researched information above.
- Personally, I was less worried at myself after the design review, because I thought that I simply did not have the skills to figure out the logic for CBG and Benes network. During the design review, Sooraj, Akshath, and some other students also mentioned the difficulty of implementing Benes network.

# Next Steps:
- Akshath suggested trying the LUT, which Duc will look into, while I do more logical thinking on the CBG.
- Dig deeper with the workload of each recursion stage to divide them into equal pipelined stages.
- Understand ways to minimize latency of CBG.
