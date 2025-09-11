## State: I am not stuck with anything, don't need help right now. 

## Progress
    On the Sunday meeting, I was assigned to work on the Python Simulator, to verify that the convolution would function correctly. I managed to add additional tracking measures (ended up being redundant), and finished a rough version of the routing test at the end of the script. 

    I also attended the Scratchpad meeting to get better understand on how we would interact with them. 

## Tasks
  My upcoming task would be working on the Python simulator, and change the tensor architecture, whilst simplifying it down.
  
  Python Simulator Work 
    - Strip everything down as much as possible
    - Change architecture to NCHW 
    - Ensure that HW is easy to work with (Keep Channel and Batch at 1)

  Documentation 
    - Nvidia GEMM Convolution 
        Paper for scratchpad 
    - Scratchpad RTL 
        How scratchpad interacts with rest of system 

## Notes
   Changing the tensor architecture should not be that bad, which leaves me with more time working on routing and finding out a way to see what values are actually useful. Getting the simulation done is incredibly important, as this will be able to prove that convolution should work. 

## Future Plans 
    Once I finish the simulator, we can hopefully start moving to working on RTL. I will try to get the simulation done by the Sunday team meeting. 