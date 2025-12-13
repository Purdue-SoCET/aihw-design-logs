## State: I am a little stuck with testing the top-level of the testbench

## Progress
 Brand new top level (again) feature the 2 cycle MAC made by Vinay! Changed the old MAC units to the new one, and kept most of the recent updates the same. With this I was able to create a  brand new testbench to try to verify the funcitionality. Now with the fact that we don't need to delay inputs, we stream in data with no delay!  

 ### New MAC Changes
 2 Cycle operation 

 Siginifcant improvement over old 2/3 cycle old MAC Unit.

 All of this allows us to actually send stimuli at the same time, instead of having dummy stages and creates a more clean overall dataflow for the systolic array. 


 ### Testbench changes 
  stall_sa initilization, so we can verify that my stall logic actually works. 

  New testing strategy so we can streaming with custom delays between rows. 


  ### Expected Results
  Faster result time incomparison to the old MAC units. Functionality and overall correctness should be the same with the adders and mul units already being verified, but you can compare the output against the Python golden reference.


  ### Link to Github commits
  https://github.com/Purdue-SoCET/atalla/blob/systolic_array_myles/rtl/modules/systolic_array/systolic_array_top.sv 

https://github.com/Purdue-SoCET/atalla/blob/systolic_array_myles/tb/unit/systolic_array/systolic_array_top_tb.sv


## Tasks
Work on testbenching and finalizing functionality. Work on the final report 

## Notes
N/A

## Future Plans 
Finish top level by Sunday and have finished report by 12/9/25