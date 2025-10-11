## State: 
  I am currently not stuck on anything

## Progress:
  -This week we constructed and finished the top level architectural diagram found in the diagrams folder labeled old_arch.png (I dont know how to insert pics into the file)
  -I explored deeply into the issue, execute, and writeback stage and thought about what the code will look like.
  -I like how it is currently constructed using states to track the funtional unit status tables.
  -There will be these states:
    -EMPTY - empty and waiting for an instruction
    -WAIT - instruction has been put into the fusts and something else needs to issue first
    -RDY  - "hazard" cleared and waiting for functional unit to be clear - "hazard just means something else is being issued in this case as there will be no dependencies"
    -EX - instr is in functional unit in execute stage
    -instr can go straight from wait to ex if no dependencies or hazards
  -This already exists so it will make it easy to reuse
  -this is a very simple way of keeping track of which structural hazards exist in the functional units
  -this is simple and will not take much area
  -Once the instruction reaches execute it will send its data into the pipe and wait until it gets the ready signal from the functional unit
  -for the cases where there is a writeback, it will wait for the writeback signal from the writeback stage, at which point it will transition to wait, and wait for a new instruciton, or ready if an instruction
      is already waiting on it, or execute is there is nothing blocking it and an instruction is ready.
  -For the execute stage, I plan on always sending all the data available in the interfaces and letting the functional unit decide what it needs based on opcode. I beleive this is similar to how it is already
      executed, this will also make the interfaces very easy. I will need to check with the specific teams to see what they need/want from me
  -We will only be able to send one fust at a time so there will never be any overlap on this bus if multiple functional units share a common port.
    -we will use either age logic or longest delay logic to decide what gets sent
  -For the writeback stage, we will need a buffer for the alu writeback in case a load finishes at the same time an alu op finishes, we cant lose one of those.
  -When we writeback, we know what functional unit the data is coming from, so we will check that fust for the destination register and writeback there
    -this will all happen in the same cycle that the functional unit sets ready high, so there should be no delays from writing back, transitioning states in the FuST/clearing the FuST, and/or getting new data
        into the FuST
  -Becase of banking issues in the vector register file, if we are trying to access 2 regs in the same bank we will either have to stall or try to issue another command
    -I am worried if we try to issue another instruction it will cause a huge critical path as it will check reg file, go back to issue policy, then send another instruction which may have a differnt register
        accsess
  
## Next Steps:
  -Next steps are to start diagramming the FuST specifically and the issues stage specifically to see how things will be layed out and flow.
    -I need to dive in deep into the current FuSTs and how they transport data, and what data they carry.
    -Due to the lack of dependencies, i am sure there is a lot we can get rid of to lighten the hardware up.
  -We have the design review sunday so hopefully I will learn more about how the other teams are working and that will help me better integrate the pipeline with their designs.
  -I need to go in deeper in the issue stage to better understand that as well.
