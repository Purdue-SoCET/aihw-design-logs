## State: I am not stuck with anything, don't need help right now. 

## Progress
  This week I created a section on the document regarding the usecase of the instruction "shift.vs"
  Link to document - https://docs.google.com/document/d/1cPfQhlDqv8aA0h1p-Eb_DB3sLzMEvE1i8g09MyHWf1w/edit?tab=t.pirxn99i0jm0

  Also started to work on simplify the adder given from the vector core team so that we can try to implement it in our processing elements. The new adder is a 2 (correct if i'm wrong) cycle adder, with our old one taking around 3 cycles, making it an improvement over the infrastructure that we had already. With it currently having a wide range of functionalities, I have been working of simplifying it, as we do not need all of the operations that it current has to be utilized in our PE.

  Link to new adder (Thank you vector core!!!) - https://github.com/Purdue-SoCET/tensor-core/blob/vector-core-valu-chase/src/modules/vaddsub.sv
  
  
  ### Planned adder Changes 

  Removing vaddif.sub

  Reasoning: In our processing element, we are always adding the incoming partial sum and the product, the operand already signs already encode subtraction when needed so we do not need an extra control. 

  Subnormal support (I think)
  Reasoning : Subnormal support is when we handle all of the tiny floating point numbers wher ethe exponent field is zero but the fraction is non zero. This is mainly made to give a gradual under flow. This is a bit expensive in hardware, and can lengthen the critical path. An alternative would just using flush to zero, where if we had a subnormal result, we should just output signed zero. is_sub, and eff_exp in the code are both utilized for the subnormal support. 
  
  ### shift.vs Summary Overview
  We should probably keep the "shift.vs" instruction with it making our lives easier in full convolutions in the future. Currently if we only use shift.vi, we would have to change the stride lengths in instruction even time we encounter a new layer with a different stride. With shift.vs, we only need that singular instruction to maintain functionallity across all potential stride lengths. Check document linked above for further documentation and explanation + little example ! 

## Tasks
  Continue working on simplifying the adder module (hopefully done by this sunday) and then help to make a MAC unit utilizing the new more efficient adder. 

## Notes
  N/A, enjoyed Sooraj's great presentation today 


## Future Plans 
 Continue to help out systolic array with us getting closer to tape out. We still need to save a significant amount of space, and actually pipeline the systolic array. 