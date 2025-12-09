# Week 12 Design Log

## State:
Still not able to understand clos fully. Will dig deeper into it

## Progress:
- Did a presenation on Tuesday.
- Professor Anand found crossbar very interesting.
- Sooraj suggested using something related to SRAM as a possible solution, but I did not understand this fully. I will have to talk to Akshath about this, because he seemed to like the idea very much.
- Since clos can also be a good solution, I will do more research before talking to Akshath during the Sunday meeting, where I will discuss the better solution betweeen the two.
- I think there was a lack of communication between Akshath and myself on the result and process of synthesis, because I could not answer questions related to synthesis tool and mistakenly answered as wrong number of cycles for solution to Benes. This may have been because after finishing and verifying Benes for 9 cycles, I moved on the CBG, while Akshath went on with synthesis and altering the pipeline cycles. We did this, as we wanted to generate the CBG code as soon as possible, which ended up us splitting the work between the two of us.
- Understood that we are single cycle is the optimal for Benes.
- Discussed with the other VIP students to decide on the poster template and started adding materials to the poster

## CLOS network
- Clos is a generalized Benes network
- Clos works in 3 cycle, and this is fixed.
- Clos does not need a separate control bit generation code nor uses 2x2 switches. The controls are done internally, which will decrease latency and the number of cycles.
- The pdf example uses permutation with N=32 and includes hardware diagram, so it is assumed that this can be done in hardware.
- Three stages are called Input, Center, and Output.
- Each stage has desired number of schedulers (in powers of 2), which is consisted of rearrange module and dispatcher, which does the actual rearrangement of input to output and communicates with the adjacent stage to control the rearrangement module respectively.
- The parameters for clos network is C(n,k,m), meaning n input/output ports, k input/output modules, and m central modules.
- Optimal design of clos for N=32 is C(4,8,4).
- Clos allows for both Strictly non-blocking (SNB) and rearrangably non-blocking (RNB) depending on the restrictions
- The requirements are: (m > 2n−1) for SNB and m = n for RNB.
- RNB is more beneficial because it has the minimal area. Optimal case for N=32 is n = m = 4, so RNB is possible.

## Next Steps:
- I will have to look more into the actual implementation of clos so that I can transfer the idea into code
- prepare for a design review presentation that will happen on the 19th.
- Work on VIP presentation poster and actually do the presentation on Tuesday.
- I will talk to Akshath about our design selection and the synthesis step, so that I get a better understanding of our work as a whole.

## Image:
- clos_network.png