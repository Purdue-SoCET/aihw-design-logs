## State: 
  I am currently not stuck on anything

## Progress:
  This week we constructed and finished the top level architectural diagram found here: https://drive.google.com/file/d/1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu/view?usp=sharing (open in drawio hard to see details from jsut the picture)
  I explored deeply into the issue, execute, and writeback stage and thought about what the code will look like. I like how it is currently constructed using states to track the funtional unit status tables.
  There will be these states:
    EMPTY - empty and waiting for an instruction
    WAIT - instruction has been put into the fusts and something else needs to issue first
    RDY  - "hazard" cleared and waiting for functional unit to be clear - "hazard just means something else is being issued in this case as there will be no dependencies"
    EX - instr is in functional unit in execute stage
    instr can go straight from wait to ex if no dependencies or hazards
  Once the instruction reaches execute it will send its data into the pipe and wait until it gets the ready signal from the functional unit, and for the cases where there is a rightback, it will
  wait for the writeback signal from the writeback stage, at which point it will transition to wait, and wait for a new instruciton, or ready if an instruction is already waiting on it, or execute is there is nothing blocking it and an instruction is ready.
  For the execute stage, I plan on always sending all the data available in the interfaces and letting the functional unit decide what it needs based on opcode. I beleive this is similar to how it is already executed.
  We will only be able to send one fust at a time so there will never be any overlap on this bus if multiple functional units share a common port.
  For the writeback stage, we will need a buffer for the alu writeback in case a load finishes at the same time an alu op finishes, we cant lose one of those.
  When we writeback, we know what functional unit the data is coming from, so we will check that fust for the destination register and writeback there, this will all happen in the same cycle that
  the functional unit sets ready high, so there should be no delays from writing back, transitioning states in the FuST/clearing the FuST, and/or getting new data into the FuST
  
## Next Steps:
  Next steps are to start diagramming the FuST specifically and the issues stage specifically to see how things will be layed out and flow. I need to dive in deep into the current FuSTs and how
  they transport data, and what data they carry. Due to the lack of dependencies, i am sure there is a lot we can get rid of to lighten the hardware up. We have the design review sunday so
  hopefully I will learn more about how the other teams are working and that will help me better integrate the pipeline with their designs.
  I need to go in deeper in the issue stage to better understand that as well.
