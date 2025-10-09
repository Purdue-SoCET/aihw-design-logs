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
  - Inputs : send values when (valid && fifo_has_space)
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

# Week's Progress
## 1. UVM Team Discussion (10/7/25)
Discussion: https://docs.google.com/document/d/1wkPebjAmX3TWlar8HtL-GTniY8Vg29cWxahkBAUrI-0/edit?usp=sharing
![Screenshot 2025-10-08 at 4 11 44 PM](https://github.com/user-attachments/assets/a4aae64d-1e0a-4edf-9981-bf968c12c1c1)
![IMG_7535](https://github.com/user-attachments/assets/18ff51d2-0d71-4d54-b738-b8925a7d14cd)

## 2. GSAU Interface
![Screenshot 2025-10-07 at 2 21 18 PM](https://github.com/user-attachments/assets/b87b450e-a23e-429a-b34f-79e081dcd2f9)

latched signals  
scoreboard  
vdst[8]
valid  
weights

veggie  
vegg.n_vdata [512]
Vegg.vdata [512]
veggn_valid 
vegg.valid 

Veggie File interface (by Joseph): https://github.com/Purdue-SoCET/tensor-core/blob/jghanem/vector-core/src/include/vector_if.vh   
GSAU Interface: https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/src/include/gsau_if.vh  

![Screenshot 2025-10-08 at 3 46 45 PM](https://github.com/user-attachments/assets/0384039d-e2e1-4b02-878d-a058b8e0c052)
![Screenshot 2025-10-08 at 3 47 06 PM](https://github.com/user-attachments/assets/40aa2ea3-ea36-4729-b3b1-9d8213c2525d)
![Screenshot 2025-10-08 at 3 47 21 PM](https://github.com/user-attachments/assets/346043fe-3652-4ee9-9224-dbba68ebe6bb)  

Feedback from Jing : ```I dont see any major issues, signals are well commented. 
Scoreboard modport might not have the data field. Check with scheduler team if they still calling it scoreboard```

## 3. Valid Ready Handshake Reading
![Screenshot 2025-10-07 at 2 23 28 PM](https://github.com/user-attachments/assets/be9855b0-6ff7-46cb-ac5d-b1e654525502)
![Screenshot 2025-10-07 at 2 23 55 PM](https://github.com/user-attachments/assets/0cb2cc83-67ad-4960-a390-f623562efd64)

This handshake is useful for stalling without losing any data, pipeline friendly and doesn't need any other flags.

## 4. GSAU Source Code
Me and Nikhil have started on the source code for GSAU.  
GSAU Control Unit (top file): https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/src/modules/gsau_control_unit.sv   
GSAU RD Register Queue: https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/src/modules/sync_fifo.sv  
We will use a sync fifo for the RD register queue.  
Shifting network - We will use the Benes network from Akshath's scratchpad team which is being desgined by Haejune.  
GSAU testbench: https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/src/testbench/gsau_control_unit_tb.sv  

Pipelined or not?  
The GSAU control unit will not be pipelined. This is how it works:  
Control logic sends the instructions and data to systolic array.  
And the control logic also stores rd to the fifo.  
When systolic array has output, tt pops the fifo for vd.  
Then the output and vd will be sent out to wb buffer.  
Sending instructions to systolic array and writing output to wb buffer is decoupled.    

# Future Plan
- Complete top level GSAU completely.  
- Testbench source code with small test cases and make sure every unit works as expected.
- Complete verification of modules by 10/19
- Integration to vector core by 11/2
