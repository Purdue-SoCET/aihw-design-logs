Status: I am not stuck with anything.

## Progress

- Sunday meeting
    - Debugged scalar architecture, some instructions were not generating correctly due to mismatches in token names
    - Used TextReportGenerator class to output the log and the generated assembly to a file
    - Discovered missing Bgt and Ble operations on the greencard, made Sooraj aware. These operations were added later that day
    - Further discussed packetization method tradeoffs.
        - Postprocessing script could have a hard time modifying the SchdImm bits that are needed to signify the start and end of a packet
        - Changing optimizer requires much research. Since it works on the IR, we would need to somehow flag each instruction in the IR, which the codegen would then use to set the schdImm bits in the ISA -- very work-intensive
    - Received clarification on packet size: currently a fixed size of 4 instrucions
        - If there are less than 4 instructions to be put in a packet, fill the rest with NOPs

- Individual work
    - Added the missing brach operations discovered in Sunday meeting
    - Validated sclar ISA implementation
    - BIG ACHIEVEMENT: scalar ISA is now fully implemented, pull request opened https://github.com/Purdue-SoCET/aihw-ppci-compiler/pull/2 

- Thursday meeting
    - Had teammates review pull request above, now merged
    - Laid out the work to be done for implementing vector datatype and instructions. The tasks are:
    - Add vector datatype to parser, along with any intrinsics necessary for vector operations
        - VEC32 datatype will consist of 32 float elements.
        - Initialized either using an initializer list like

            `vec v1 = {1.0, 2.0, 3.0}`;

        - or by giving it raw data, like

            `vec v1 = 0xABCDEFG;`

        - or another way using previously allocated memory address (syscall?)
        - all this has to be done without allowing scalar float operations 
    - Modify BinOp login in CodeGen to accept vector type objects and call the appropriate ISAs
    - Add custom logic to CodeGen for new operations
    - Created a project planning board on GitHub https://github.com/orgs/Purdue-SoCET/projects/1
    - Added tickets to the project board and assigned them to teammates

## Next steps

- Do the work outlined in the tickets above
