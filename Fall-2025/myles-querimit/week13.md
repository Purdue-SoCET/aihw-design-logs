## State: I am not stuck with anything, don't need help right now. 

## Progress
 Created the new toplevel for the systolic array to handle immediate computation start and simplifed input handling.

 ### Key Architecture Updates
Removed the input buffers (Vinay is going to replace that arch later), and replaced it with a direct connection to all of the MAC units. 


New immidiate computation, changed it so that each time sa_array_in comes from systolic array interface / vector unit, a value is taken in (from sa_array_in) and is sent through the array (computation starts immediately)


We no longer have to wait for the full matrix to be loaded into the buffers to start the computation. The values will flow through the systolic array immediately, and it is just directly connected currently. 

  ```systemverilog
  assign MAC_inputs[j][0] = memory.array_in[((N-j)*DW)-1 : ((N-j-1)*DW)];
  assign weight_enables[j][0] = memory.weight_en;
  ```


We currently use memory.array_in_partials as the psum buffer source. We use the bottom role so we wait for full column acculumation before adding the PSUMs.

### What Still is needed 
Buffer fixes 
Testing

### Testbench
Also made a new test bench to verify the new top level (will run later this week). Based heavily off of the old systolic array top level top bench. Stimuli and output loading is the exact same, with edits mainly with a new task waiting for the the systolic array being drained.


### Link to GitHub Commits
https://github.com/Purdue-SoCET/atalla/blob/systolic_array_myles/rtl/modules/systolic_array/systolic_array_top.sv 

https://github.com/Purdue-SoCET/atalla/blob/systolic_array_myles/tb/unit/systolic_array/systolic_array_top_tb.sv

## Tasks
Finishing verifying the top level, and help Vinay with input buffering.  

## Notes
Cannot make Sunday meeting due to going home for Thanksgiving break.


## Future Plans 
Finish top level, work on final report 