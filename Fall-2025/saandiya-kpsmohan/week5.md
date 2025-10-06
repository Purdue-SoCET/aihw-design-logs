## State
I am not stuck.

## Progress
- On Sunday Meeting (9/21/25), Systolic Array team had a discussion with Timmy to go over how inputs, kernels and psums will flow in the systolic array and how the final output will look like.
![IMG_7455](https://github.com/user-attachments/assets/30315e99-410a-4e7f-abad-d01eb879ce29)
As we can see here, the output shape BEFORE transposing in systolic array occurs is HxWxK, and AFTER transposing occurs the shape is KxHxW. This output shape is not very useful for us meaning, we can't just use this result for the next operation such as max pooling or softmax. The shape needs to be redefined in the software before doing these operations.
- Next, I told Sooraj that I cant get the Python simulator to work with trying to implement the actual systolic array itself. So he gave a suggestion to use matmul instead and restrict the size to 32.
- I did that, and the output matches the expected output.
- Final version of simulator: https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_saandiya/tmp/TCA_tiled_sim.ipynb
![Screenshot 2025-10-06 at 7 07 59 PM](https://github.com/user-attachments/assets/3fafcb53-c590-4c24-9434-45f4c13c994a)

- On 9/23/25, during the Systolic Array and Scratchpad meeting, we went over the new TCA RTL design: https://app.diagrams.net/?src=about#G1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR#%7B%22pageId%22%3A%22Q9zmwPF7jkmAEOsmvTRS%22%7D
- During this meeting as well, we were discussing how to map values into an external buffer/fifo from the toeplitz matrix before sending it into the systolic array in which there wasn't a clear solution other than requesting values from scratchpad consecutively which is a lot of cycles and not utilizing the values we already have in the TCA. This led to SoorajGPT wanting to find a solution from a different angle, for example: input stationary systolic array.
![IMG_7457](https://github.com/user-attachments/assets/1158b311-d0fd-4572-948c-3ad14f83530d)

- And then on midnight 9/23/25 Sooraj proposed to move the convolution/gemm operations to vector core itself which I will explain why below. This sparked some discussions in discord to see what is the best way to move.
- During Vector core meeting (9/24/25) Sooraj, Jing, and others decided to move the convolution operation, and all other operations of Systolic Array through the Vector Core itself. This means all GEMM, Conv, weight loading (all systolic array operations) goes through vector core. The scratchpad DOES NOT interact with the systolic array anymore.
- BUT the design flow for these operations still REMAINS THE SAME. Its just that there is no TCA anymore. Instead of TCA, we use the Vector Core.
- The reason behind this is that, desiging a separate TCA unit will take area on the chip, while the vector already has a vector register file that has 4 512 bits banks space that can be used to carry out convolution and gemms.
- This means now systolic array have to be interfaced with the vector core.

## Evidence of Progress
## Vector Core meeting (9/24/25)
- Went over how things will flow now. I understood that this method is much much simpler than creating a TCA unit because we are reusing the vector core registers which is now WAY easier instead of buffering the buffer in the TCA unit. We just neeed to add a systolic array interface from vector core.
![IMG_7460](https://github.com/user-attachments/assets/2179e083-0f10-4c01-ab4f-69262e41e360)
![IMG_7459](https://github.com/user-attachments/assets/699ffce3-7dd3-4eb5-85fb-1417d628870b)

## Design Review
- Made slides for Design Review: https://docs.google.com/presentation/d/1NUsgPNHckD6SQqHwr7apMZsKGGzt-dGIDLM42nVq9yI/edit?usp=sharing
- Vector Core Block Diagram: https://app.diagrams.net/#G1JW5Jguhs4vChq-sziK6ZME-tJgycms2J#%7B%22pageId%22%3A%227TNEaft9gA3lZacV84dw%22%7D
- Me, Nikhil and maybe Myles have moved under Vector for now.

## Meeting with Joseph, Jing, Nikhil (9/25/25)
We had a meeting to see what new instructions will be needed and how the vector core is modified.
During this meeting we also discussed the best case and worst case latencies in vector core.
![IMG_7468_2](https://github.com/user-attachments/assets/3f235fa1-960b-40f0-860e-fc7b2232004e)

Best and worst case latencies:
![IMG_7467_2](https://github.com/user-attachments/assets/1ece7d37-6972-4eaa-b61a-aed6f09b82e2)

How Toeplitz is formed and instructions for that:
![IMG_7466_2](https://github.com/user-attachments/assets/9de9846b-04fa-4e6e-ab4d-57aa0782e138)

- We also came up with 2 new instructions to carry out shift operations to contruct the Toeplitz added to Atalla ISA sheet: https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?usp=sharing
  
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

## Week Plan:
![Screenshot 2025-10-06 at 7 09 01 PM](https://github.com/user-attachments/assets/1baa6827-cb8f-44d5-a9c0-35dad01c7e42)

- Had a pre design review on Friday (9/26) with all team leads which went well.
- Timmy raised a question if we can construct im2col by channels instead of kernels - which the answer is that if there are different strides then the FSM for this becomes really complicated.

## Future Plans
- Will work on the systolic array interface
- Check staggering inputs created in the vector core itself - would that be better
- Buffer before/after the sys arr
