# Progress:

- Continued research on the concept of crossbar: 2x2 crossbar is a hardware to either keep the order of an input pair the same or make them change order (cross). Each crossbar is controlled by a control bit, selecting whether the crossbar will keep striaght or cross.
- Benes theorm utilizes this 2x2 crossbar to perform the desired array transposing. Although it will take log N amount of clock cycle (N for length of array), it minimizes hardware component (compared to muxing all the 32 bit inputs to all the 32 bit outputs, which is done in 1 cycle).
- it was very difficult to find the consistent algorithm that works for 2x2 crossbar, which is what we are using as sub-logic.
- Checked the RTL diagram designed by Duc
- understood the logic for cross/keep-straight logic of 2x2 crossbar: if the destination index is in the same half(lower/upper), cross. If different, keep-straight
- Struggled to understand the logic to connect the output of a stage to the input of next stage.
- Found an python algorithm through research towards the end of the Sunday meeting.
- One assumtion according to the research, if ith output is an upper value from 2x2 crossbar, the elemenent will connect to index [i]. Lower ouptut will connect to index [i + 4].

# Next Steps:

- Test the validity of the python code with simple example of index of length 8
- If it works, write a logic for hardware.
- prepare for design review next Sunday.
- attend Friday meeting for pre-design review
