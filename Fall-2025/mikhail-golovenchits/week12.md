Status: I am not stuck

## Progress

* Consulted with Ivor about packetization script. Since we chose to packetize the assembly instead of the IR, he wrote a python script that does exactly that by tracking the register dependencies and prevents RAW, WAW, WAR hazards within packets, filling the empty space with NOPs. I verified the correctness of the script so we should be good to proceed with integrating it into the rest of the compiler.

* Presented the 2nd design review on Monday for which we received some feedback.
    * We need to make sure that the linked is aware of the nops added to the packets by the packetization script. Specifically, the relocations need to be done to the correct PC. This should be relatively straightforward to implement if we configure the packetization script to output the generated packets back to the assembly file it first came from.
    * We need to have a clear set of goals for this semester to present at the senior design presentation. I think our main goal this semester is to have the compiler fully able to generate all instructions specified in the ISA with the appropriate frontend intrinsic function calls. Ideally, we would also test the code the compiler outputs for accuracy using a simulator, but we are not sure when that will be provided.

* Mostly focused on the presentation and packetization this week so not much progress on the ISA patterns front.

## Next steps

* Create the presentation for the senior design event, as well as the research event.
* Continue work on matching ISA patterns.
