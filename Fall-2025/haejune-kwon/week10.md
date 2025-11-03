# Week 10 Design Log

## State:
NOT STUCK! I FINISHED CBG!!

## Progress:
- Finished control bit generation (CBG) code.
- I converted the python code from "controlbits.pdf" into system verilog, so that it can be mapped to hardware.
- This CBG will generate control bits to be fed into Benes network code that I finished last week.
- As explained multiple times in the previous design logs, the control bits will control each of the 2x2 switch.

## Control Bit Generation
- The reference code includes self-update and recursion that cannot be done in hardware coding. Therefore, I had to flatten out these to logics. 
- The self-update refers to something like "p = composeinv(q, p)", meaning that p is being updated by using itself to update. This happens multiple times throughout the python code, so I had to introduce new variables to store the result, instead of pointing to itself. I updated it to "r = composeinv(q, p)". There is also a self-update in a for loop, and I resolved this issue by adding a dimension for the number of for loop iterations.
- In terms of recursion, the bit generation function is called once for N=32, then twice for N=16, and so on until N=2, which has its own logic. In each iteration, sub-arrays are generated for the next iteration. Since recursion is not possible in hardware, I flattened out this to happen one after the other, and each variable size is 5 x 32 to hold all 5 recursion values. One problem related to this was that the dimensions of the blocks continues to change as iteration goes on, as I just stated. this can get very tricky in hardware, as the size must be fixed, especially if the code is parameterized. However, I figured out that the total number of elements in each iteration is fixed to N (32 * 1, 16 * 2, ... for SIZE=32), so I decided to use the offsets and keep the length of all the variables constant. For N=16, the variable of length 32 will hold the sub arrays of 16 in each halves, and they will be accessed by using the offset from future iterations.
- In each iteration, first and last 16 bits of control bits are generated. For example, [15:0] and [143:128] for N=32, [31:16] and [127:112] for N=16 and so on, with last iteration generating the middle 16 bits.
- One big problem I faced was that the order of traversing the array is not linear. Instead, it was jumping between halves, because it was done in recursive manner. This is represented in CBG_order image. Therefore, I had to figure out the logic to solve this problem. While I was drawing these out, I realized that the input array is divided into halves, and left halves are stacked from left in original order, while the right halves are stacked from the starting index from next block. These happen in pairs, not as a whole 32 array.
- To solve this, I introduced an inner-most loop that iterates each of blocks in halves. This rearranged the blocks in desired order for the iterations to happen correctly.
- I also introduced composeinv and mind_min sub-functions to do the inverse permutation and output the minimum value of each index respectively.
- I integrated the CBG with benes, and it works perfectly fine.

## Next Steps:
- I will need to work on cleaning up the code, such as parameterization or turning always_comb logic into generate if possible. One issue I have is that one of the loops run for log2(SIZE) - 2 times, and I am not sure if this will cause a problem if the result is negative. The intension for this is to simply skip the for loop. I wil have to check with this.
- I saw that Duc has completed the test bench for benes and cbg, but I saw lots of compiling errors, so I may need to check and update it.

## Source code:
- scratchpad_main branch > atalla > rtl > modules > common > xbar > cbg_benes.sv, composeinv.sv, find_min.sv