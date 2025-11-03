## State: 
  I am not currently stuck on anything

## Progress:
  -Last friday we met as a groop to continue to work on the spec and final design
  -Wroked on the top level diagram to get it ready for the comign design review
    -We redid the design to feature no issue queue
    -we discussed the nuances of packet dependencies
      -this includes back to back packets dependent on the same register
        -if this happens then the second packet needs to clear its dependency as it will already have been stalled away by the first packet
        -this is to ensure we do not waste dependency bits, in a limited dependency bit system, the first depependent packet may want to set that bit again
      -this also included bit setting
        -anytime a packet comes in and sets a bit it first needs to check the bit it sets
        -if it does not it may over write a previouse instructions dependency and cause incorrect execution
      -this also included latency green zones
        -if we have a very long latency instruction like a GEMM instruction we know the latency green zone to be about 100 clk cycles
        -we do not need to set a dependency bit for this instruction if we know the dependent instruction is outside of this zone
        -this raises some questions and problems:
          -if the GEMM instruction for some reason is stalled, we cannot issue any other instructions even if they are independent
          -if we do, the dependent instruction may be shifted out of the green zone
          -this may cause a lot of issues and very slow ecexution
  -I redid the decode 1 block diagram to show the inner workings without the issue queue
    -The decrement logic may have a lot of area due to the functional units all needing a wire back to it to move the counter register tag around
    -I beleive this is the best way to do it
    -We discussed using more than 8 dependency bits, possible 16
      -this is becuase we may have more than 8 indepedent packets in the pipe at one time with how deeply everything is pipelined
      -especially with long latency instructinos, many of which will be indepenedent
    -We may not even set a dependency bit for long latency instructions as they would likley hog the dependecy registers
    -we would need to schedule all dependent instructions in the green zone then

  -I went to office hours for the first time on friday
    -confirmed that the diagram we built was in a good enough spot to have our deisgn review

  -met again on saturday to discuss more issues and continue working on diagrams and the spec sheet for the compilers
  -met sundday
    -redid the move commands in the ISA after talking to the vector team
    -redid the script to incoroprate all instructions as the ISA was updated
    -minimized the script to be based on functional unit and register accesses
      -about 20k unique combinations that are possible
      -did not include 3 NOPS and 1 instruction in this list
    -finshed the presentation for the design review
    -kept working on the spec sheet and got it in a good place for out design review

  -Did out design review presenetation on monday (finally)
  -helped the compiler people better understand out design
  -attended the weekly meeting and listened to Sooraj's presentation about simple solutions
  -this week was a little lighter due to 565 (did not go well)

  -all of our content has been shared in the discord for reference
  -the script will be in github soon for easy updatability
  -our presentation is in discord
  -all of our diagrams are also in discord
  -please refence them for progress proof

## Next Steps:
  -meet again with vector team to figure out exact latencys and how we will deal with the green zone issue mentioned above
  -keep updating all diagrams in accordance to the changes
  -begin working on the rtl
  -simualte and verify
  -solve any more issues that happen