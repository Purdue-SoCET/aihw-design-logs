## State: 
  I am not currently stuck on anything

## Progress:
  -Once again we have taken on a new design
  -This time we are switching to a VLIW/EPIC based design
  -we will have packets of independent instructions
    -this will be 2, 3, or 4 instructions
      -we will need to see what works the best based on area and speed
    -the packets will include a dependency byte
      -we will check this byte agains out dependency tracker
        -if any bits are 1 and match then we need to stall the isntruction packet until they are cleared
      -we will probably add a queue to queue more instructions and check all of them in case and are independnet
        -if any are indeppendnet we will issue them in front of the dependent ones
    -once we issue them we will set the dependeny checker in accordancy to the other byte of meta data that comes with the packet
        -this will setup the dependency check for later packets which may be dependent on it
  -this allows easy and lightweight dependency checking
    -it is much cleaner than out first idea of incrementing a counter everytime an instruction is issued and decrementing it when it has a writeback or commit
    -the previouse idea would not allow us to issue other packets out of order, but this new idea will let us do that if we find an independent packet
  -the packet is setup so any instruction can be in any postion
    -there are certain setups we dont allow
      -packets with branches cant include anything after the branch in program order
      -we cant have a load and a store in the same packet to avoid load store advancing
      -we are limited by the number of functional units (only 1 alu can be in the packet at a time)
        -there are likley more limintations I have not thought of yet
    -becuase we can have any instruction in any postition we will need a full crossbar
      -despite the size and area of the crossbar, this greatly increases compiler flexability
  -all of this will happen in the decode 1 stage
  -we will issue it to out next decode stage after the crossbar where each functional unit will have a cooresponding decoder
  -we will increase the alu banks to avoid bank conflicts as we will need many access ports in case there are many scalar instructions
    -we will need up to 8 parallel accesses at once
      -2 ALU, 2 BR, 2 load or store, 2 vector load or store
    -one the occasion of a bank conflict we will have to stall and send forward what we can
      -this is unlikley so it wont hurt too bad
    -the vector register file will behave in a similar manner
  -we met with the vector core team again, we should be able to issue multiple instruction in parallel to the vector core
  -there are some limitaitons on this but that will be provided in out large documetn to the compiler team
  -branches are a speacial case
    -any instruction after a branch will nbot be allowed to make it out of decode 2 stage until the branch is resovled
      -on a miss we will squash the instructions
      -on a hit we will resume from the stall
  -we still need issue queues
    -we will need one for the scalar write back
    -one for the vector write back
    -we got rid of the FP16 reg file as it really didnt do much
      -vector can store their FP16 as a vector in the VEGGIE
  -I need to connect with SPAD team to understand what they need, I am unsure of how they operate currently
  -I did way to much VLSI research this week on predication, traces, load store advancment, load store speculation, and much much more
  -attended the SoCET meeting and listened to the AMD talk
  -attended a lot of other random meetings to figure out how this will work

  -all diagrams will be in the diagrams foldder, the top level arch diagram is VLIW_arch.png
  -the white boards I received from meetings will be under the diagrams folder as well labeled original_VLIW.png and new_VLIW.png

## Next Steps:
  -next we will need to communicate with everyone else and understand what they need from us and what we need from them
  -clean up top level diagram
  -start block diagrams
  -make the compiler team upset and give them out list of requirments (it will be long)
  -do design review