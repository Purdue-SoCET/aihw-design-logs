## State: 
  I am not currently stuck on anything

## Progress:
  -This week we worked on finishing the emulator
    -we have it working with basic test cases
    -need to test it against more advanced programs
    -modified the memory subsystem of the comiler to support 160 but instructions as well as 32 bit data
    -worked on the main instruction loop:
      -it grabs the 160 bit packet from the PC
      -decodes the packet into an array of dicts
        -the keys are the field like rs1, rd, imm, etc
      -these go into a massive if else statment
        -this checks for the instrucion type and sets up the function cooresponding to the instruction
        -it also handels branches and mem accesses
        -if there is a branch it calculates the PC and wether or not it was taken
        -actually sets the new pc at the end of the current packet iteration
      -this will loop through doing one instruction at a time
      -once it finishes a packet it will grab a new one
      -first thing it checks is if te packet includes a halt
        -if it does it breaks out of the loop and dumps the current working mem to a file
      -added vector reg file
        -needs testing
      -added scalar reg file
        -tested by writing to is and storing contents to mem
        -confirmed working
      -added mask reg file
        -needs testing
      -tested basic functionalities through a simple script
        -it performs an addi to a reg loading a value
        -it performs an and op on this new data
        -it writes the data back to the mem
        -halts
      -will probably make a vector add mult program with a loop to test branches vectors etc
    -Need to add vector load and stores
    -need to add sdma/spad support
    -need to write more advanced programs to test these funcitonalities
  -We redid our presentation for design review 2
  -presented design review 2
  -went to weekly meetings

## Next Steps:
  -finish the emulator
  -create slides for final presentation
  -create poster for poster presentation
  -update the spec sheets