State: I am stuck on how to properly bank my vector register file and what the internal structure will look like. 

Progress:
1) Top level RTL diagram:
<img width="854" height="586" alt="Screenshot 2025-09-21 122608" src="https://github.com/user-attachments/assets/13d125b3-58ec-43a8-b955-7ea3d74129cf" />

With the Vector Core being implemented as a "Vector Datapath" the top level needs to look a little different. The Veggie File and Scoreboard sit in the Dispatch/Issue stage, the vector execute stage lives in the Scheduler execute stage, and it gets outputted directly to the scheduler WB stage. The vector top level was designed to service all the main instructions that we are hoping to support.  

-SVFU (specialized vector functional unit) supports all the "specialized" instructions such as e^x, sqrt etc 
-Reduction FU supports all reduction instructions 
-VALU (Vector ALU) supports FP16 adds, subtracts, bitwise ops for masking, etc 
-VLS (Vector Load Store) is what interfaces with the scratchpad memory for vectors.  
-Veggie File (Vector register file of course) is the vector register file  

 
Since power and area are not a concern in this design it was optimized to support maximum instruction parallelism. The VALU has 32 instances to accommodate the full 32 lanes so adds, subtracts, etc can be done in 1 cycle * FU latency. Since the SVFU contains larger FUs it has 8 lanes to accommodate for area constraints. The Reduction FU will have 16 lanes and operate in a "tournament bracket" fashion. VLS does not need any duplicated logic as it only needs to load/store 1 vector at a time that happens in one go. Notable design decisions include registers within the FUs to store intermediate values to prevent high Veggie File write/read bandwidth. Additionally reducing the number of lanes in Reduction and SV FUs to reduce the area. These are the uncommon case so it is okay to add a little bit of latency for more area. You are only able to issue 1 instruction at a time although you can store instructions in multiple FUs 

2) Vector_if.sv & vector types 
<img width="376" height="890" alt="Screenshot 2025-10-10 200953" src="https://github.com/user-attachments/assets/7747a7b7-6678-4a7d-bc72-9fdcdc7e0288" />
<img width="488" height="981" alt="Screenshot 2025-10-10 200935" src="https://github.com/user-attachments/assets/adbba9d0-f416-4ce1-86c2-ab3e338fb727" />

Created vector top level interface file and started created a vector_types.vh file that the rest of the vector team can use that will contain all of the structs and datatypes we used. I left a snippet but it includes a lot of things. Design choices include having 1 large interface file for vector core to prevent congestion of if files. In addition I created the vector types to be fully parameterizable so that all the objects vreg_t, vsel_t, etc will be correctly sized.

3) Vector ALU implementation
<img width="488" height="955" alt="Screenshot 2025-10-10 201353" src="https://github.com/user-attachments/assets/2d37160d-ac35-45f5-99a4-d2431bbe8fbb" />

I drafted an example of what a vector module may look like for my own practice. As I do not have the sub modules for it yet I tried to lay down the overall structure. This includes how I am considering masking, how I will consider FP16 special cases, and how I will use for loops to unroll hardware. My goal is that by the time my teammate finishes the add unit I can plug it directly into here.

5) Vector ISA green card

<img width="1620" height="376" alt="Screenshot 2025-09-14 165110" src="https://github.com/user-attachments/assets/ae36f3b1-c059-499d-956c-938dcbbfccec" />

Detailed custom ISA for vector core with bit spec. I decided to devise the ISA into 3 types VV = Vector Vector, VS = Vector Scalar, VI = Vector Immediate. Instead of specifying another 8 bits for a vector mask select I included only 1 bit to specify if you are using a mask or not. If it is high it will automatically pull from the v0 register which is the specialized mask register. This saves 6 bits in the ISA and allows us to do it entirely in 32 bits. Tradeoffs include only being able to store 1 mask and maybe having an extra instruction to set the mask before using it.  

  
Future Plan: 

- Vector Register File Microarchitecture 

- Veggie system verilog implementation 


