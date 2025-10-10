# Weekly Report – Week 4

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. For the scheduler core architecture, it has been decided to ditch the Out-of-Order execution and let compiler take the burden of arranging instructions in such a way that RAW hazards are avoided. It can do this by arranging mutliple independent instructions in between any 2 dependent instructions. If Out-of-Order execution is removed, we will not have to deal with WAR/WAW hazards.
The idea is that the compiler will send a packet of instructions at a time that will not have dependencies within the packet. Any dependent instructions will be moved to the subsequent packet. A packet can contain 2,3 or 4 instructions, we will decide on the exact number. Across the packets, we can still have dependent instructions, but the compiler should try to schedule independent packets in between 2 dependent packets as much as possible.

Reasoning behind this choice: ML/AI workload instructions offer a ton of parallelism, much more than CPU. There is much more scope for software scheduling to take advantage of this ILP. If we remove OOO execution from hardware, we can save a lot of are and power as we can either get rid of or minimize load/store queues, issue buffers etc. Currently, the performance gain provide by all this OOO stuff in hardare is not worth the amount of are it takes. So it was decided to move all this scheduling buren to compiler.

2. Akshath provided some updates to the scratchpad instructions.
   scpad.ld
    - 7 bit opcode telling which one 
    - GPR with the DRAM Base Address 
    - base_row (starting address of the tile)
    - num_rows 
    - num_cols
    - scpad_id (1/2) 
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
sysarray.ldtile 
    - 7 bit opcode 
    - base_row 
    - num_rows
    - num_cols
    - scpad_id
no need for loading a vector into sysarray -> TCA from Saandiya does it implicitly. 
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

   Further discussion happened on how the instructions for the weight loading should be designed.

3. Attended the systolic array's weeky meeting, further dived into the reading for systolic array from these sources:

   Older design: https://app.diagrams.net/#G1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR#%7B%22pageId%22%3A%229D6ffl-pBdOOQ0Yu_FEU%22%7D

   Overview of systolic array: https://docs.google.com/presentation/d/1lIEHfZK9VRijk5NyIesDra1bx8vj_TPr8nyfB-8WLEc/edit?pli=1&slide=id.g347cecf6f23_1_567#slide=id.g347cecf6f23_1_567

   https://app.diagrams.net/#G1DRmwK1PmweZ2aiFaTrbGhgJA1F0VDL2X#%7B%22pageId%22%3A%22CrdqlVTdd1bBr1gekedv%22%7D

   GEMM and Convolution operations flow: https://docs.google.com/presentation/d/1NUsgPNHckD6SQqHwr7apMZsKGGzt-dGIDLM42nVq9yI/edit?slide=id.g383b35a1ff2_0_1&pli=1#slide=id.g383b35a1ff2_0_1
   
   Gained an understanding of the functioning of systolic array and the flow of data through the module. Now, need to apply this knowledge to separate out the GEMM controller from te current systolic array controller.

   Reasoning for separating out the GEMM controller and convolution controller: Design of PEs in the systolic aray gives us the flexibility to do both GEMM ops and Conv ops, with the only difference being in how we load the inputs and weights into the array. If we deign 2 controller such that one takes care of the GEMM ops and the other takes care of the conv ops; we can reuse the whole array os PEs for both the operations by simply switching out which logic controls the systolic array at the moment.

4. Logged into the ASICFAB to clone the code repo. Got Systolic Array testcases to run on any RTL changes. Ran the test commands on vanilla code to see if the setup is working properly:
   verilator -f [my file]
   
   - verilator -f [my file] from tensor_core folder
   - obj_dir/Vsystolic_array_tb`
   - gtkwave waves.vcd / dump.vcd
   Path to my directory: /home/asicfab/a/shah1470/tensor-core/

## Next Week’s Tasks
1. To complete a draw.io diagram of the GEMM controller of systolic array by reusing some portion of the design from the current systolic array. Currently the detialed draw.io of the older systolic array controller does not exist, so need to create the diagram from the current RTL and microarch discussions.
2. To explore VLIW and other methods that help to handle the branch instructions in scheduler core. In the new approach to the scheduler core, packets will have independent instrctions among them, but the question remains on how to handle branches. Simplest option would be to explore the basic branch prediction and flush the pipeline on a misprediction. Need to analyse the impacts of different ways of handling branches.
