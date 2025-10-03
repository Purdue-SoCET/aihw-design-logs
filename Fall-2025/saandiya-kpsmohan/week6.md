## State
I am not stuck.

## Progress, Design Choices
- Design Review went Well on Sunday.
- Attended vector core meetings to give updates and start working on Global Systolic Array Unit (GSAU) which interfaces between Vector Core and Systolic Array.
- Me and Nikhil worked on GSAU RTL: https://app.diagrams.net/#G1JW5Jguhs4vChq-sziK6ZME-tJgycms2J#%7B%22pageId%22%3A%22soUAP3OVNAC-PgTYQMAo%22%7D
- Finalized ISA: https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?gid=0#gid=0
- We added a new instruction : stsys.st	Store Image/Kernel to Systolic Array Imm	1000111	for (i=0; i<VL; i++) if (mask[i]) systolic_input_fifo.push(vs1[i[);.vdst[offset+j] = systolic_output_fifo.pop(j); load_weights = imm; PC = PC + 4	VI	71
- For shift, we added 5 bits to existing instructions. Shifts are always to the right.
    - add.vv	Add	0101001	for (i=0; i<VL; i++) if (mask[i]) vd[i] = (vs1[i] + vs2[i]) >> shift[4:0] ; PC = PC + 4	VV	41
    - addi.vi	Add Immediate	0111000	for (i=0; i<VL; i++) if (mask[i]) vd[i] = (vs1[i] + imm) >> shift[4:0]; PC = PC + 4	VI	56
- I made an instruction set for convolution for compiler team to refer: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?tab=t.1nzcifmpqvr6
- Me and Nikhil met with Vinay to go over the design and confirmed its compatible with the current systolic array.
- We planned to use valid-ready handshake protocol for our design because it is what used in industry.
- Upon discussing with Vinay, systolic array needs to be modified to add a valid/ready signal for psum outputs.

## Next Steps
- Planning to get RTL verfied on Sunday meeting and start coding GSAU.
- Planning to finish coding before Fall Break.
