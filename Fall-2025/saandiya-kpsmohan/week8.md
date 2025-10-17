## State
I am not stuck

## Progress
- Fall Break 13th-14th October.
- During Vector Core meeting (10/15) we discussed on some ISA changes, verfication plans and timeline.

## Evidence of Progress
### ISA Changes
- We also need a left shift in addition to the right shift for masking to be properly done. Previously, I was under a wrong impression of how masking will happen in vector core, but turns out left shift is happening implicitly. So we do need a left shift.
- shift.vs (scalar reg) is now a vs type
- For shift.VI use imm5 to specify amount of shift and use imm8 (1 bit to specify left or right)
- Update gemm inst pseudocode (A*B + C)
- Create new load weight instruction, vi type.
![Screenshot 2025-10-16 at 9 57 37 PM](https://github.com/user-attachments/assets/a1a1f5b2-17f6-4057-8c29-9aea3d53d259)
![Screenshot 2025-10-16 at 9 57 51 PM](https://github.com/user-attachments/assets/b34526b7-4b6d-4bfb-96ff-c75fe78f8df1)
![Screenshot 2025-10-16 at 9 58 22 PM](https://github.com/user-attachments/assets/a8b3990a-f968-42f6-b155-26631fc888b1)

### Abstract
- An abstract is created and submitted by our group for the Fall 2025 Expo
- https://docs.google.com/document/d/1gBZ6_h6uZCL9Xjy55gx3o7PBXcEfP2HXks3DoknYAj0/edit?tab=t.0
- ```Convolution is a mathematical operation used in machine learning tasks but often becomes performance bottleneck in models like
  CNN (Convolutional Neural Network) and NLP (natural language processing) due to their heavy computational demands, high memory
  bandwidth requirements, and latency from moving data between memory and compute units. The SoCET AI hardware team is designing an
  AI accelerator processor using a systolic array architecture for efficient convolution execution. Our earlier implementations were
  unable to correctly feed input data into the systolic array, resulting in significant latency and wasted memory bandwidth. To address
  this, (1) we use a vector core developed to construct a Toeplitz matrix directly streaming data into the systolic array, enabling
  convolution to be executed as a General Matrix Multiplication (GEMM), and (2) each MAC uses a depth-optimized Wallace Tree multiplier
  customized for FP16 and BF16 mantissas with implicit one handling, carry-save compression and a short rounding final adder. This
  design minimizes redundant memory access and hardware usage through structured tiling and on-chip reuse while continually supplying
  the systolic array through vector registers. The outcomes of this approach include expected functionality, constant throughput, and
  decreased area. Limitations include requiring extensive compiler support, 32 or more cycles of instruction latency, and potential
  underutilization of the systolic array, which depends on the number of kernels and operations occurring at once. Next steps will
  include implementing and verifying this design, along with defining worst and best case latencies such that instruction can be
  interleaved to pipeline the process at a software level.

### Verification Plan
- Verification plan for the gsau control unit is created by me and nikhil.
- https://docs.google.com/document/d/1WN1tDZcZA2MwcfPBuD1hkEgETITvLbIamk2HCpjdNyk/edit?usp=sharing

### Best and worst case latency for GSAU
- The best latency for GSAU is 64 cycles (32 inputs cycle + 32 psum cycle)
- The worst case latency for GSAU might be 64 + 96 cycles, 96 comes from backpressure in the wb buffer.
- Need to confirm this with GTAs

### Code and verification
- The code and testbench is done.
- But the module still needs to be verified - running into some errors.
![Screenshot 2025-10-16 at 3 40 12 PM](https://github.com/user-attachments/assets/534ed06f-a20c-4699-a778-762871cd1be3)

## Future Plan
- Finish synthesis, verification by Sunday (10/19)
