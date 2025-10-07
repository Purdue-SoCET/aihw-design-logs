# Week 4 Design Log

## State:
I am not specifically stuck, but I still have not figured out completely on how Benes network works. There is lack of information online. 

## Progress:

- Continued research on the concept of crossbar.
- it was very difficult to find the consistent algorithm that works for 2x2 crossbar, a module we are using as sub-logic.
- Checked the RTL diagram designed by Duc
- understood the logic for cross/keep-straight logic of 2x2 crossbar.
- Struggled to understand the logic to connect the output of a stage to the input of next stage.
- Found an python algorithm through research towards the end of the Sunday meeting.


### Crossbar and Benes network concept:
- our 32x32 crossbar will be designed to implement Benes network of 9 stages (2logN - 1). This is because the work load is too big for input length of N=32 for fp16 to be done in single cycle. Hence, pipelining is needed to divide up the work instead of muxing all the 32 bit inputs to all the 32 bit outputs.
- To do this, we will be using 16 of 2x2 crossbars in each stage, which is a hardware to either keep the order of an input pair the same or make them change order (cross). Each crossbar is controlled by a control bit, selecting whether the crossbar will keep striaght or cross.
- Therefore, there needs to be a logic to generate the control bits to control each of the 2x2 crossbar.

### Some crossbar logic assumption based on research:
- cross/keep-straight logic of 2x2 crossbar: if the destination index is in the same half(lower/upper), cross. If different, keep-straight
- One assumtion according to the research: if ith output is an upper value from 2x2 crossbar, the elemenent will connect to next stage input of index [i]. Lower ouptut will connect to index [i + 4].

## Next Steps:

- Test the validity of the python code with simple example of index of length 8
- If it works, write a logic for hardware.
- prepare for design review next Sunday.
- attend Friday meeting for pre-design review

## Reference:
- software code that generates and tests the bit generation and crossbar permutation.
https://github.com/Purdue-SoCET/tensor-core/blob/scratchpad_main/sim/memory/scratchpad/crossbar.py 