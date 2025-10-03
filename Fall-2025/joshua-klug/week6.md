## State: 
  I am currently stuck. I am confused with how we are dispatching instructions in parallel, but I am talking ot Rishi about it tomorrow to clear it up

## Progress:
  We have once again redone our entire deisgn. This time we are getting rid of all functional unit status tabels and working to issue everyhting as soon as it comes into the issue stage.
  Becuase everything is indipendent and the functional units are pipelined with fixed delays, we can essentially push every instruction into the functional unit as soon as it comes.
  There is one exception to this: loads and stores do not have a fixed latency, but, to combat this we will create a queue for all the load store instructions so if mulitple come
  back to back, we dont have to stall them, and we can continue to issue other instructions while the memory accesses finish. This week we met with the vector team to discuss how
  our scheduler needs to interact with their functional unit becuase they merged the systolic array into their vector core. We talked about how we will retreive data from the VEGGIE or FP16 reg, 
  including the mask if needed, and how we will send it to them, then write it back to either register file depending on the operation. I also attended the weekly SoCET meeting and listened
  to the guy from cirrus logic talk about the importance of decoupling capacitors and how they are used. This week I recreated the entire top level diagram, hopefully for the final time.
  I went in and changed it to have 2 decode stages, one checking just the dependency bits and figuring out what instruction to send, the next actually decoding the instruction and sending it
  throught the pipeline. Once it gets to the issues stage it will enter a queue (I think this will change once I clear things up with Rishi), where it waits to be selected by the issue policy.
  Once it is selected it is sent into the functional unit and we wait for a writeback.
  Here is the link for the drawio: https://drive.google.com/file/d/1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu/view?usp=sharing (open in drawio hard to see details from jsut the picture)
  
## Next Steps:
 -Meet with Rishi to clear up the problems in the top level
 -Start wroking on lower level diagrams to get a better understadning of how they work
 -present so everyone else knows what we are doing and how we are doing it
 -hopefully start coding in the next 2 weeks
