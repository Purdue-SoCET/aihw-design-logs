## State: I am not stuck with anything, don't need help right now. 

## Progress
  This week I finished the new stalling logic [STILL NEEDS TO BE TESTED] and started working on debugging the new FP16 adder. I recieved the testbench files and all of the modules needed, and I am currently working on it. 

  ### Stalling - Full Implementation 
  This implementation may cause critical path errors in the future due to how we have the stall singal propogate. 

  #### Data Flow (stall_sa signal):

  GSAU Sends A Stall Signal (stall_sa) > Control Unit Recieves Signal and Prevents Future Operations While Signal Is High > MAC Recieves Signal And Finishes Current Operation 
 
  #### Top Level Changes :
  - Add stall to MAC interface file and tie to to every PE 

  #### How we Register Values : 
  Hold the flip-flop when stall is high to register current value. 

  Psesudocode :
  ``` 
  if(stall == 1'b1) begin
  value <= value;
  end
  ``` 
 

 #### Architecture Explanation 
 This was decided a couple weeks ago as a team on the most effective way to implement stalling, the current rendition is a modified verision of Sooraj's idea. Critical path issues may be created from this implementation as we are sending the same singal to 1024 different processing elements at the same time. The reasoning behind this decision, instead of propagating the stall signal through the systolic array once every cycle, through the PE's, is that it would take 31 cycles to reach the top row if we started at the bottom and vise versa. This would mean we would have to register significantly more operation values instead of just the single one. Currently, we are only holding 1x32 in regards to the amount of data we are storing from the stall, and this value would be larger through singal propagation , as the other processing elements who are still uneffected would still be running. 


 #### Link to Branch
 https://github.com/Purdue-SoCET/atalla/tree/systolic_array_myles 
## Tasks
  ### Adder Changes (By Priority)

  - Subnormal Support 
  - NAN Support 
  - Accuracy/Edge Cases 

  ### Design Presentation
  - Start working on the design review slides for this Sunday 

## Notes
Missed Sunday meeting (told Malcolm in advance) 

## Future Plans 
  Finish verifying adder and work on booth encoding 