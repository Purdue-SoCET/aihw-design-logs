## State: I am not stuck with anything, don't need help right now. 

## Progress
  Most of this week was under fall break, so I did not have a substantial amount of time to work on the project. In the time I did have, I managed to finish all of the stalling capabilities needed for the systolic array. With me following Sooraj's idea to implement the draining system, I talked to Vinay and Saandiya to properly integrate this feature in. 

  ### Architecture Overview 
  When a stall signal is sent, instead of stopping the operation of every single PE in the systolic array, it would be better for us to let all of the outputs drain out, unless there is backpressure. In the case in which there is backpressure, the PE's will actually stall. After discussing with Vinay, the best way to implement this idea would be to set the ```start``` signal low when the stall signal is set to high. 


  The name of the stall signal that we will recieve from the GSAU will be called ```stall_sa``` 

  The file that these changes would be implemented in would be ```src/modules/sysarr_control_unit.sv```

  Here is the link to my commit - https://github.com/Purdue-SoCET/tensor-core/commit/f2a3e92a7d77892dd50d8565d86404a21671e56c

## Tasks
  Moving forward, me and Vinay will test if the stalling solution will work in a variety of test cases. Once this change is verified, we will start working on pipelining the entirity of the systolic array. The current task of implementing stalling is finished, and just needs to be verified. 

## Notes
  Week of fall break.

## Future Plans 
  Figure out the architecture changes that is needed to start pipelining the systolic array. We also need to be very weary of the overall size of our changes, as we have to start to acknowledge the actual tapeout of the chip.