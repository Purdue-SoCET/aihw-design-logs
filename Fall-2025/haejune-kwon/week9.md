# Week 9 Design Log

## State:
Not stuck anymore. I finished Benes network code

## Progress:
- Finished Benes network with 9 stages after some debugging process.
- No new concept was learned due to focusing on debugging.

## Debugging process
- The permutation value kept giving wrong values even after I reverted my code to the original code without parameterization, so I tried to check where the problem is. The debugging process was difficult, because I did not have access to the waves. The make command simply ran the test bench and produced the output text. Therefore, I could only knew the final result and nothing in between. This was very different from python, because I could not use print statements or check intermediary variable values without the waves. 
- One way I found was assigning my output directly to the permutation values to each stage, instead of the final output. Then I figured out that even the output for first stage was wrong. This meant that either the 2x2 switch was not functioning or the control bits are wrong.
- I double checked the crossover_switch sub-module and the control bits by using the original python code, but they were both definitely correct.
- Therefore, I checked the first 16 LSB of control bits ([15:0]) that my module received, and it reading the 16 MSBs. After this, I flipped the input control bits, and it produced the right permutation output.
- I then replaced the original code with then parameterized one with generate, and it was working as well. This means that my code was correct the whole time, but the endianness was reversed.
- I decided that this shouldn't be a problem, as I can always decide the order of control bit generation. I can simply produce it in reverse order.
- UPDATE: our repository was renamed to atalla, so I pulled the repository again. Then, the endianness fixed itself, so there is no need for worrying about it anymore.
- It was very very difficult to do debugging without waves, which is why I spent so long to only debug this module.

## Next Steps:
- Since the benes is fully pipelined and parameterized, I will work on control bit generation code.
- To do so, I will need to convert the python code to hardware code, flattening recursion and pipelining the module to divide the load equally.

## Source code:
- scratchpad_main branch > atalla > rtl > modules > common > xbar > benes_xbar.sv