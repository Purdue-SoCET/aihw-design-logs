## State: 
  I am not currently stuck on anything

## Progress:
  -Last friday we met with Sooraj to tweak the design
    -instead of continuing to have the compiler send us the packet dependency bits
    -we will now track all of the dependency bits per register
    -this includes:
      -1 bit cooresponding the every register
        -256 for the scalar regs
        -256 for the vector regs
        -2 for the vector mask regs
      -we wil set this bit high when an instruction writing back to that register is issued
      -all subsequent instructions will check this bit for the read and write (WAW) registers and will not be able to issue if it is high
      -we willo continue to have all instructions in lock step until they have been sent to execution together
      -they will still be able to write back independently
      -this was changed to help the compiler team have a more obtainable project
      -they will still guarentee that we have independent instructins within a packet
      -but now we will need to check dependencies between packets vs the compiler telling us about those dependencies
    -Also met with the vector team to clarify the move instructins and how they work
    -We fixed up the top level diagram to reflect this change
    -I created a lower level diagram of the new dependency checker and how it works (located in the same drawio as always)
    -Began working on the interfaces for the top level
      -current idea with the interfaces is to continue the way they currently are
        -this means 1 interface for every architectural pipeline stage:
          -Fetch->decode1
          -decode1->decode2
          -decode2->execute
          -the execute will be lots of interfaces, each functional unit has their own we need to accomidate
          -execute->wb
        -we plan to complete all of the interfaces by sunday
    -we worked on the bit spec sheet as well, cleaning it up and adjusting it for the new changes
    -this was another lighter week but it will pick back up once we start implementation (should be next week)
    -as always all of the reference diagrams we worked on are located in the drawio
    -spec sheet and other files should be shared in the discord

## Next Steps:
  -finish interfaces
  -start implementation
  -get ready for design review 2
  -poster thing