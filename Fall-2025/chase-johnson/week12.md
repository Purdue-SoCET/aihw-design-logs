## State: I am stuck with verifying my module, I can't seem to figure out why my modules are showing up as undefined whenver I run QuestaSim.

## Sub-Team - Vector Core
The Vector Core is a seperate piece of hardware from the rest of the tensor-core as it aims to focus on processing vector-based instructions. The purpose of the vector core is speed up AI model learning processes and work in conjunction with other pieces of hardware in the tensor core.

## Progress: 
This week I worked on implementing the VExp unit and found that the best way to control the flow of data within the module would be using a FSM, adder, multiplier, and fraction/int converter. I found that to support the switch between bf16 instructions and fp16 instructions I would need to use an IFDEF and make to seperate versions of the FSM. I would need an FSM dedicated to BF16 instructions and one for FP16 instructions.

The BF16 FSM would follow the same structure as shown in the comparison table where different computations would be performed from stage 1 to stage 11. I needed an fraction/int converter for the purpose of seperating the whole value from the fraction during the first part of the taylor series approximation process. Where I need to take the input and divide it by ln(2). Then seperate the integer from the fraction portion and compute the (fraction part - a) and then use that value for the rest of my taylor series approximation.

Also I only included the BF16 FSM because I have not completed the FP16 one but doing this is easy as I just need to add two more stages of computation and then change the hardcoded values.

I defined all the modules externally so that a switch between instruction types would be easy.

1. VExp Code
![](images/vexp_w12.png)

2. VExp BF16 FSM Code
![](images/vexp_fsm_w12.png)

3. VExp Fraction/Int Converter
![](images/vexp_fracint_w12.png)

4. VExp Comparison Table
![](images/vexp_comparison_table_w11.png)

## Future Plans:
- Figure Out Why Modules Are Not Defined
- Verify Exp Unit