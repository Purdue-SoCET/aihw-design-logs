## State: 
  I am not currently stuck on anything

## Progress:
  -This week we stated work on our emulator
  -instead of working on RTL for the rest of the semester we were tasked with creating an emulator
    -this will act as a golden model to compare the hardware too
    -it will also act as a checker for the compiler team
      -it will tell them if they are creating bad/invalid packets
    -basic flow we diecided on:
      -start with a mem file (.txt) that has our memory contents
      -load this file into the prgram by parsing it and storing it in a dictionary to be read and wrote too
      -fetch packet_size instructions at a time
      -decode all instructions in the packet
      -check to make sure they are a legal combination
      -check to make sure they are all independent
        -if either of these fail: stop the program and error it
      -check to see if there are any bank conflicts
        -this will be put in a report file
          -technically not an error, but they should be avoided
      -execute one instruction from the packet at a time
        -grab the data from the registers
        -put it through its function
        -write data back to registers
      -repeate for the rest of the instruction in the packet
      -once done repeate with the next packet
      -once end of program: write the contents of the active memory to a mem dump file
    -so far I complete the memory functions (most likley will change due based on what compiler team gives us)
    -there are functions that scan the input mem file and create a dictionary with the memory adresses and values
    -there is a read function
    -there is a write function
    -there is a top level script that demonstrates this all
    -(all located in the emulator branch)
  -We also tweaked the design slightly
  -A floating point unit was needed
  -we added intructions/hardware support for:
    -floating point add and subtract
    -floating point mult and div
    -floating point set less than and set less than unsigned
  -the sloating point values will be stored in the lower 16 bits of the scalar reg
  -there is already hardware to convert from scalar to BF16 and back
  -all of these changes are in the atalla isa doc and the drawio

## Next Steps:
  -Keep working on the emulator
  -get ready for design review 2
  -get ready for the poster review
  -keep updating the spec sheet so the compiler team can stay up to date with any more changes we make