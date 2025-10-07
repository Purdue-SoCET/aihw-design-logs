## State
I am not stuck.

## Progress
- Not much progress has been made since it was midterm week. We just had the GSAU RTL ready to be presented during Sunday meeting (10/5) to be checked before we started coding.
- We also started working on interface files and source codes.

# Evidence of Progress
## Sunday Meeting (10/5/25)
We sat down with the UVM team to come up with a test plan and go over data flow between GSAU and Systolic Array

## 1. Weights, inputs and psum_in flow in the Systolic array
- We load weights in the systolic array first (32 cycles).
- Then we load inputs and psum_in at the same time (32 cycles).
- psum_in here refers to the previous tile's psum_out which we can just be added to the current tile's psum_out.
- We load both of them at the same time to save extra 32 cycles.
- Valid/ready signals in sys arr
  - Inputs : send values when (ready && fifo_has_space)
  - Weights: share the same port but theres no FIFO so you can load whenever you want
  - Psum: should be a signal
- Changes in systolic array (informed Vinay)
  - Psum ready signal (currently the psum just keeps being accumulated without checking if the value is actually ready)
  - If there is backpressure from wb arbiter, we need to stall the whole sys arr as it is - adding stall signal.
 
## 2. Minor changes in GSAU
- Stall signal for backpressure
- Psum_enable signal - to check if psum_out is ready

## 3. Finalized ISA & Bit Spec
![Screenshot 2025-10-06 at 10 07 22 PM](https://github.com/user-attachments/assets/711ed13e-d2ee-4e2b-b371-3d760f528c6a)  
![Screenshot 2025-10-06 at 10 09 14 PM](https://github.com/user-attachments/assets/670f0691-6ee9-4ca9-84bf-efaa19d5eb0e)

Instruction 81 is added for future use cases - using scalar reg to shift amount.
Shift is its own instruction.
GEMM has its own instruction to either send input AND psum at the same time OR weights.

## 4. UVM testing
![IMG_7521_3](https://github.com/user-attachments/assets/df9c61c9-753f-4b35-adc5-96de87c8f3ff)
![IMG_7520_3](https://github.com/user-attachments/assets/af3588a3-d65b-4e72-b298-ae39bd00875a)

From these images you can see the cycles it takes for 1 operation, and the new instruction of sending psum & input together.

## 5. Valid/Ready Handshake
From Jing: ```For modules that requires handshake, for example valid ready, you might need to add a buffer in between the stages to handle the timing for the handshake. If the control logic is not combinational, consider this:```
https://chipmunklogic.com/digital-logic-design/designing-skid-buffers-for-pipelines/  
There are some works that should be done aka bufferings to be added for valid ready modules because we need to latch values since its pipelined. Combinational control logic will have terrible critical path.

## 6. Advice from Jing
After finishing hardware coding, we should also do some python script that outputs the set of instruction needed to carry out convolution for any arbitary sizes. This is for compiler folks.

## Week's Progress
## 1. GSAU Interface
## 2. GSAU Source Code

# Future Plan
- Testbench source code with small test cases and make sure everything works as expected.
