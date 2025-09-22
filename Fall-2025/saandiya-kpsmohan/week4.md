## State: I may or may not be stuck.

## Progress, Tasks, Next Steps, Future Plans
- On Monday, me, Sooraj, Nikhil, Jing and Malcolm sat together and discussed the whole flow of convolution from tiling into the Scratchpad until the end of the convolution.   
- On Tuesday, I met up with Jing and Malcolm again to further understand this new design and I started implementing this in a Python simulator.  
- The new design, idea, requirements are documented in this google docs: https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?usp=sharing
- As of now, my simulator works with different kernel number, kernel size and input size with stride = 1 with the tiling, and kernel loading and using matmul to represent the Systolic Array.
- The simulator doesnt work with my implementation of an actual Systolic array, so we narrowed down the error to the implementation of the Systolic Array itself.
- So, I am going to try and use the SA simulator students made last semester and hopefully that works, and this is where I might get stuck.
- Planning to finish this by Sunday meeting, so that we can implement the RTL during the team meeting.
- The current simulator is updated in my github.
