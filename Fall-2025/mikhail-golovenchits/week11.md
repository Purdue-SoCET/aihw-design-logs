Status: I am not stuck

## Progress

* We needed to implement bfloat16 datatypes for initializing weight matrices. Instead of creating a new float datatype in the frontend and backend, I modified the existing float definition in the IR and backend modules to consist of 16 bits. This way, I only had to change a few parameters for floats, instead of creating a whole new datatype, which is cumbersome as we have seen with creating vector datatypes. We are also not allowing the definition of 32 and 64 bit floats as our architecture does not have the ability to process those.
* Modified the "theta" POC instruction we have done in prior weeks to implement the GEMM instruction. This involved changing how the IRDAG processes the GEMM IR. 
* Merged Sahil's vector instruction branch into vector-frontend, allowing us to proceed with genereting the assembly for the gemm instructions. Fixed the token sizes and included the new instructions into the existing ISA object.
* All these changes can be found in the vector-frontend branch
https://github.com/Purdue-SoCET/aihw-ppci-compiler/tree/vector-frontend

* Fixed bugs in Ivor's packetization implementation, which led us to discover a new issue: packetization is being done based on the dependencies between IR instructions, which are not aware of actual register usage. This leads to packets being constructed where the same register is both written to and read from, which is not allowed. For example, a STRI instruction in IR gets put into a packet by itself to preserve the dependencies. The compiler then generates the assembly code for STRI, which is an li and a sw instruction on the same register. These 2 instructions are put back into the original packet with the STRI instruction, creating a hazard.

## Next steps

* Implement the ISA patterns for vector instructions and test.
* Find another way to packetize the generated assembly code, potentially consult with Prof. Wang of ECE 573 (compilers);