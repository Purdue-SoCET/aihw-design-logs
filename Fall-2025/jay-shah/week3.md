# Weekly Report – Week 3

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. I have taken up the modification of Execute stage in Scheduler Core Unit. Major changes required include interfacing the GEMM instructions with the scratchpad. Consensus of the team was to proceed with Out of Order execution similar to the functionality of scoreboard so far. Old pipeline of the scheduler core given here:
   https://app.diagrams.net/#G1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu#%7B%22pageId%22%3A%22uzxL_cWLtsVC-XBVhwOb%22%7D

   Changes were outlined by Rishi in the Scheduler Core weekly meeting:
   <img width="1865" height="537" alt="image" src="https://github.com/user-attachments/assets/64b864a8-5c5e-4169-944e-04d4d5e776af" />


3. To understand the changes required I talked to Akshath and received this green card from him that outlines how the instructions will interface with the scratchpad GEMM controller.
   
   scpad.ld
    - 7 bit opcode telling which one 
    - GPR with the DRAM Base Address 
    - base_row (starting address of the tile)
    - num_rows 
    - num_cols
    - scpad_id
scpad.st 
    - 7 bit opcode 
    - GPR with the DRAM Base address
    - base_row
    - num_rows 
    - num_cols
    - scpad_id
vreg.ld
    - 7 bit opcode 
    - base_row -> tile start
    - row_id
    - col_id
    - row/col select -> if 0, then load column col_id, else load row row_id
    - scpad_id
vreg.st 
    - 7 bit opcode
    - base_row -> tile start
    - row_id
    - col_id
    - row/col select -> if 0, then store column col_id, else store row row_id
    - scpad_id
sysarray.GEMM
    - 7 bit opcode telling GEMM 
    - scpadA (1)
    - scpadB (1)
    - scpadC (1) -> output
    - M (5)
    - N (5)
    - K (5)
    - base_rowA -> tile start
    - base_rowB 
    - base_rowC -> output
sysarray.CONV
    - 7 bit opcode telling GEMM 
    - scpadA (1)
    - scpadB (1)
    - scpadC (1) -> output
    - IH (5)
    - OH (5)
    - K (5)
    - base_rowA -> tile start
    - base_rowB 
    - base_rowC -> output
   
       
3. Participated in the Systolic Array weekly meeting. Started to learn about the systolic array controller changes required. The current controller in RTL performs tasks such as
   - checking the start of a new GEMM instruction (handles 3 instructions in flight)
   - loading the inputs, weights and partial sums into the systolic array, and tracking the status of the loading.
   - handling operations like fifo shift, checking the space left in fifo (for input and partial sums FIFOs)
   - interfacing with the memory to load more inputs and partial sums into the sytolic array depending on the buffer available in the FIFOs
   - checking the completion of a MAC operation and signalling 'done'

## Next Week’s Tasks
1. The plan is to bifurcate out the systolic array controller into 2 controllers - GEMM controller to handle matrix multiply and accumulate ops, and a Covolutional controller to handle convolution operations.
   A requirement has been outlined to create a muxing logic to give the control of the systolic array to one of the controllers, depending on the type of instruction. I will explore the design of this muxing logic.
2. Discuss with Akshath the interface of GEMM functional unit in scheduler and the scratchpad.
