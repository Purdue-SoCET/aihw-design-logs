## State
I am not stuck.

## Progress, Design Choices
- Design Review went well on Sunday.
- Attended vector core meetings to give updates and start working on Global Systolic Array Unit (GSAU) which interfaces between Vector Core and Systolic Array.
- Me and Nikhil worked on GSAU RTL: https://app.diagrams.net/#G1JW5Jguhs4vChq-sziK6ZME-tJgycms2J#%7B%22pageId%22%3A%22soUAP3OVNAC-PgTYQMAo%22%7D
- ISA: https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?gid=0#gid=0
- We added a new instruction : stsys.st	Store Image/Kernel to Systolic Array Imm	1000111	for (i=0; i<VL; i++) if (mask[i]) systolic_input_fifo.push(vs1[i[);.vdst[offset+j] = systolic_output_fifo.pop(j); load_weights = imm; PC = PC + 4	VI	71
- For shift, we added 5 bits to existing instructions. Shifts are always to the right.
    - add.vv	Add	0101001	for (i=0; i<VL; i++) if (mask[i]) vd[i] = (vs1[i] + vs2[i]) >> shift[4:0] ; PC = PC + 4	VV	41
    - addi.vi	Add Immediate	0111000	for (i=0; i<VL; i++) if (mask[i]) vd[i] = (vs1[i] + imm) >> shift[4:0]; PC = PC + 4	VI	56
- I made an instruction set for convolution for compiler team to refer: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?tab=t.1nzcifmpqvr6
- Me and Nikhil met with Vinay to go over the design and confirmed its compatible with the current systolic array.
- We planned to use valid-ready handshake protocol for our design because it is what used in industry.
- Upon discussing with Vinay, systolic array needs to be modified to add a valid/ready signal for psum outputs.
- Me, Jing and Nikhil also decided to load weights into the systolic array using the vector core.
- Hence, in the stsys.st instruction, the imm field corresponds to loading the weight: 1 - weight, 0 - inputs.
- We also have a fifo to keep track of the destination registers of the psum. This will be popped everytime psum is being sent to the WB buffer so that it knows which register to store the result in.

## Evidence of Progress
## 1. Vector Core Top Level (Credits to Joseph)
![Screenshot 2025-10-06 at 9 39 16 PM](https://github.com/user-attachments/assets/a52ff3bc-c92d-4d9a-9e79-fbca9ac78e2f)

Shifting will be its own unit instead of having to shift before every lanes. This is to save some cycles because not all operations needs shifting always.

## 2. Global Systolic Array Unit (GSAU) RTL
![Screenshot 2025-10-06 at 9 41 51 PM](https://github.com/user-attachments/assets/38a422b4-e87e-41dc-a995-82cce5e954e7)
The explanantion for 768 bits for the RD queue is explained in the diagram (we have 255 data vector registers)

## 3. Systolic Array Connections
Weight is a 1 bit indicator. If weights are being loaded its 1, else its 0. When its 1, enable signal in 1st column of MAC units go high so that weights are loaded in them and they are propagated towards the right.
This is how weights are loaded in the systolic array:  
![IMG_7505](https://github.com/user-attachments/assets/e3899577-80c0-4480-8777-99a9e823821d)

Weights are loaded one systolic array column at a time in 32 consecutive cycles. Load the first column and it shifts one column to the right in every cycle the weight_en signal is asserted. There's no fifo for weights, each mac unit has a register for weight which passes on to the mac unit to its right and we load into the weight registers of the first column of MAC units.

## 4. Sample instruction set
![Screenshot 2025-10-06 at 9 47 55 PM](https://github.com/user-attachments/assets/9d9c4aa7-bc94-4861-b00a-26609e3e84c6)
For full detail refer to: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?tab=t.1nzcifmpqvr6

NOTE: Both GEMM and CONV uses the same instruction because now conv is broken down into gemm.

## Next Steps
- Planning to get RTL verfied on Sunday meeting and start coding GSAU.
- Planning to finish coding before Fall Break.
