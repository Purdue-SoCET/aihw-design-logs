## State: 
  I am not currently stuck on anything

## Progress:
  -We continued to make progress on the new VLIW based design
    -cleaned up the top level diagram
    
    -created a lower level block diagram for the decode 1 stage
      -packet queue
        -this will be a partial CAM and a partial table
        -8 bits per packet for checking the dependecny bits in parallel will be a CAM
          -total of 64 bits
        -1 bit per packet for a valid bit also a CAM
          -total 8 bits
        -3 bits per packet for the index also a CAM
          -total 24 bits
        -total of 96 bits for the CAM
        -the reason for each will be explained later
      -Dependency checker
        -this will check if there are any 1s in the packet's check bits that match any 1s in the current check bits
        -it will do all valid packets in parallel (why we need the CAM)
        -it will seelct all packets that have no matches
          -based on the selected packets it will select the one with the oldest age (the smallest index)
        -this will also include the most recent packet, the one that was just fetched
        -if all of the packets have a match then it will send nothing
          -if all of the packets have a match and the queue is full then it will have to stall the fetch stage
          -it wont be able to write the new packet into the queue, it will leave it in the latch
        -the index is then routed back to the queue where it is matched with all the other indexes to find the actual index of the table entry
        -if the instruction is the newest instruction (the one just sent) then that will be sent through
          -it will not be written back to the queue and nothing in the queue changes
        -if the newest instructino is not sent then it will be written to the queue (assuming there is space)
          -it will take the value of 1 more than the max current index
      -age updater
        -this will take in all of the ages and update them based on which was removed
        -the dependency checker will send the index that was selected
        -the age updater will remove this index (set valid to 0)
        -then it will decrement 1 from every index that is after (larger) this index
        -it will leave any idexes that are lower
        -it will then write back all of the valid bits and indexes at the same time
      -opcode decoder is simple
        -it just looks at all of the opcodes and send the instruction to the crossbar
        -cross bar send them to their respective decode bsed on the opcode
      -current dependency check
        -this hold all of the current dependency bits
        -it is just 8 flip flops
        -the second part to it is the counters
          -each bit will have a coresponding counter
          -the counter will be set to 4 when the bit is set
          -each instruction will carry the bit that it set with it through the pipeline
          -when the instructin is commited/retired/written back it will decremenet the counter
          -when the counter reaches 0 it will clear the bit
        -when an instruction is sent it will set its bit (the one found in the set bits part of the table) to the current check bits
      -Table
        -the rest of the table will hold the 4 instructions and the set bits
    -We also started work on the paper for the compiler team
    -we brainstored ideas of the layoutand contents
    -we finished the abstract for the professional developemnt assignement
    -I created a script to find all possible packet combinations
      -there are a lot (probably 50k+)
      -out original idea was to make a table with all possible combinations for the compiler team to reference
      -with how many there are that might not fit very well in out document
      -the script will continue to be update as we change the instruction set and as we figure out what instructions can and can not go together
      -the script works through brute force
        -it calls a function that makes a combination of all instructions
        -it then checks if any of the 4 instructions dont work together based on another list that lists what all instruction cant go togehter
        -finally it checks how many of a certain type of instruction can be in the packet together
          -example: we can only have 1 scalar ALU operatino at a time
        -it will only allow a certain number of instructions of a set type based on how many of the type are supported
        -it then writes this final list to an output file and lists the total number of combinations that work
    

UPDATE!!!!
  -lots of changes have been made
  -there will no longer be an instruction queue before decode
    -that is way to complicated and if we dont need it then why have it
  -latencys will no longer be exposed to the compiler
    -we are now dealing with latencys through wires coming from each functional unit to each decode
    -if any decode matches a not ready signal then the entire packet stalls
    -this prevents us from having to have a gurenteed worst case latency (green zone) for the compiler
    -this make writebacks and back pressure much easier
  -took time to understand scratch pad and its nuances
    -there is an invisible desitnation register that is trechnically not listed in the ISA that the compiler team needs too look out for
  -updated the script to not include every single combination, just funtional unit combinations
  -discussed load store advancment and figured out that it is not a problem for vector
  -merging scalar loads and stores to prevent it from becoming a problem with scalars

  -the old diagrams (ones before the update) can be found in diagrams labeled decode1.png and VLIW_pipeline_updated.png
  -the old python script can be found under scripts/packet_depend.py
    -not going to upload the txt file it is pretty large
    -whoever reads this can run it if they wish

## Next Steps:
  -uppdate the pipeline diagram
  -create and finish a top level diagram before sunday
  -update the python script
  -finish the document for the compiler team
  -keep fleshing out lower level diagrams
  -finish presentation so we can actually do a design review