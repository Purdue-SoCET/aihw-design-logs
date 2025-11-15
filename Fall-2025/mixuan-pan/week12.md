# Week 12 Design Log: Mixuan Pan 

## State

I'm not stuck with anything, don't need help right now. 

## Progress 
This week, we presented during the second design review on Monday. It went pretty well, and we received good feedbacks. 

I also modified the bf16 adder on wednesday for Joacob from Vector core. I realized I didn't mention about the custom left shift moduel on Monday when he asked for the adder module. 

In addition, I also rebuilt the entire Wallace Tree Multipllier module with modified rounding logics used in the adder. This shrinked down the area to 5062.174.

proof of work: 
https://github.com/Purdue-SoCET/atalla/blob/systolic_array_mixuan/systolic_array_utils/add_bf16.sv
https://github.com/Purdue-SoCET/atalla/blob/systolic_array_mixuan/systolic_array_utils/left_shift.sv
https://github.com/Purdue-SoCET/atalla/blob/systolic_array_mixuan/systolic_array_utils/wtm/source/mul_bf16.sv
## Next Step
Sooraj said we need the subtraction logic for the adder urgently, so I might finish it up quickly, since it shouldn't be that bad. After that, I will work on the poster that will be presented on Tuesday. 

