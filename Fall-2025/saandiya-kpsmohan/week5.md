## State
I am not stuck.

## Progress, Design Choices
- This week Sooraj, Jing, and others decided to move the convolution operation, and all other operations of Systolic Array through the Vector Core itself. 
- The reason behind this is that, desiging a separate TCA unit will take area on the chip, while the vector already has a vector register file that has 4 512 bits banks space that can be used to carry out convolution and gemms.
- This means now systolic array have to be interfaced with the vector core.
- Made slides for Design Review: https://docs.google.com/presentation/d/1NUsgPNHckD6SQqHwr7apMZsKGGzt-dGIDLM42nVq9yI/edit?usp=sharing
- Vector Core Block Diagram: https://app.diagrams.net/#G1JW5Jguhs4vChq-sziK6ZME-tJgycms2J#%7B%22pageId%22%3A%227TNEaft9gA3lZacV84dw%22%7D
- Me, Nikhil and maybe Myles have moved under Vector for now.
- We also came up with 2 new instructions to carry out shift operations to contruct the Toeplitz.
1. New Crossbar ISA (6 bits)
Shift left/right
Addition of left_right bit and 5 bits for shift amount - total 6 bits added
Can be specified by immediate fields on instructions like addv
0 - left, 1 - right
Order of operations is mask -> shift -> execute
Idea: conv becomes a pseudoinstruction, compiler unrolls loop into many Atalla RISC like instructions (i.e. addv, addi, mset.vi)
2. Send to Systolic Array (New Instruction) 
SEND.SYS vdst, vsrc, offset[4:0]
Stream vector register → systolic array input FIFO.
Get output in vdst at a certain offset.

- How things will flow?
1. Load kernels into SA columns (weight-stationary) - > 1 kernel per column using weight loading controller.
2. Tile input feature map in SPM.
3. Stream tile rows into Veggie File.
4. Construct Toeplitz columns using vector mask, vector add, vector shifts.
5. Feed activation vectors into SA column by column.
6. SA multiplies and accumulates, produces PSUMs.
7. PSUM is returned back into the veggie file and accumulated in vector core using sum reduction.
8. Sent back to scratchpad.
9. Repeat for all kernels / tiles.


## Future Plans
- Will work on the systolic array interface
- Check staggering inputs created in the vector core itself - would that be better
- Buffer before/after the sys arr
