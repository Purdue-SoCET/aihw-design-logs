# Progress:
- Did some research with the CBG python code to determine if there is a way to do any overlapping between CBG and Benes network to minimize latency.
- Added print statements for the bits produced at each level
- Figured out that the control bits of first and last stages are produced with the first iteration of recursion (N=32), then second and second-last with N=16, and so on.
- Therefore, we will have all the bits once we do calculation for N=2 (at Benes stage 4). Hence, we can overlap 4 cycles of CBG and Benes network.
- We may be able to do the whole permutation in two extra cycles from Benes network (total of 11 cycles)

- Wrote a systemverilog module for Benes network, including the 2x2 crossbar, output-input logic and pipelining. This will be tested with a hard coded control bits.
- Set up the ssh environment into asicfab
- Got into a problem where my code won't simulate. Getting errors with 'vlog' from Makefile.

# Next Steps:
- Fix the error for simulation
- Run the test and debug
- If it works fine, focus more on flattening the CBG and wait for the result from Duc about sorting algorithm.