## State: 
  I am currently stuck. I am confused with how we are dispatching instructions in parallel, but I am talking ot Rishi about it tomorrow to clear it up

## Progress:
  -We have once again redone our entire deisgn.
  -This time we are getting rid of all functional unit status tabels and working to issue everyhting as soon as it comes into the issue stage.
  -Becuase everything is indipendent and the functional units are pipelined with fixed delays, we can essentially push every instruction into the functional unit as soon as it comes.
  -There is one exception to this: loads and stores do not have a fixed latency, but, to combat this we will create a queue for all the load store instructions
    -if mulitple come back to back, we dont have to stall them, and we can continue to issue other instructions while the memory accesses finish.
  -This week we met with the vector team to discuss how our scheduler needs to interact with their functional unit becuase they merged the systolic array into their vector core.
    -We talked about how we will retreive data from the VEGGIE or FP16 reg, including the mask if needed, and how we will send it to them, then write it back to either register file depending on the operation.
  -I also attended the weekly SoCET meeting and listened to the guy from cirrus logic talk about the importance of decoupling capacitors and how they are used. 
  -This week I recreated the entire top level diagram, hopefully for the final time.
  -I went in and changed it to have 2 decode stages
    -one checking just the dependency bits and figuring out what instruction to send
    -the next actually decoding the instruction and sending it
    -I did this so we can queue the instructins as we receive them
      -when the compiler to send us a new instruction that in dependent on earlier ones
      -it they will gather in the queue waiting until the pipe clears
      -it is possible to receive a completly independent instruction in the queue
      -while the pipe is clearing we will issue that instruction to hide some latency
  -I decided that each stage should have a small queue in case we cant issue it
    -for example if there is a branch and an ALU fighting over the register file we can only issue one
      -we need to queue it so we dont lose the stalled instruction
    -I think if we banked the register file we could do more accesses but I need to ask about that as I am unsure how much control we have over that 
  -Once it gets to the issues stage it will enter a queue (I think this will change once I clear things up with Rishi), where it waits to be selected by the issue policy.
    -we decided with a longest latency issue policy
      -this will select whatever instruction is the slowest
      -this is so we can issue faster instructions after to help hide the latencies of the slower instructions
  -Once it is selected it is sent into the functional unit and we wait for a writeback.
  -we still need a writeback buffer, same as last design due to the same reasoning
  -for the vector writeback we will need to somehow select between the vector reg file and the FP16 reg file so we will need the vector core team to send us a signal telling us what to write back to
  -the overall arch isnt that complicated, the most complicated part will either be writing back or the fetch stage due to the instruction queue logic and selecting which instructon to send
  -the number of queues we will need will come down to experimentation once everyhting works
    -hard to estimate what the intruction mix will look like and how independent things will be
  -the diagram will be located in the diagrams folder under queue_arch.png and out white board discussion will be there under queue_whiteboard.png

  Questions for Rishi:
    - do we need separate queues for systolic array and vector ops (parallel?)
    - scheduler core ISA
    - what to do when incorrect banking? (do we need to stall?)
    - fp operations in alu??
    - how many registers in everything

  
## Next Steps:
 -Meet with Rishi to clear up the problems in the top level
 -Start wroking on lower level diagrams to get a better understadning of how they work
 -present so everyone else knows what we are doing and how we are doing it
 -hopefully start coding in the next 2 weeks
