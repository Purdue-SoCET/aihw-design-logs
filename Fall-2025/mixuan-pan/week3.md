# Week 3 Design Log: Mixuan Pan 

## State

I'm not stuck with anything, don't need help right now. 

## Progress 

On the Sunday meeting, we decided to implement a wallace tree multipler for fp16 first instead of bf16. The main difference between the two is that fp16 has 10 mannissa, while bf16 has 7. But either way, the implementation is similar, just the matter of carry-on's and stages. We also realized that since we're only taking the output for the same size of the data type, half of the first stage partical products will only be useful with their adder carry-outs (the result of a wallace tree multiplier will be twice the size of the input data bit size). 

I'm currently working on implementing the wallace tree multiplier for fp16. This is pretty straightforward and should be done within a week. 


