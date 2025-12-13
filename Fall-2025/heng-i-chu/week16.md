# Week 16

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Final Report:**
  - Finished writing the final report and had our mentor review it.
  - Made some changes according to the feedback from our mentor, especially fixing the highlight on compiler research instead of simple Implementation.

- **Frontend Parser:**
  - Wrapped up the frontend parser and reorganized it into C code and Atalla modules.
  - This way it is easier to verify the frontend and introduced separation in modules from normal C code with Atalla extensions.

- **Compiler Pipeline:**
  - Fixed remaining the entire compiler pipeline and verified it successfully produce assembly code.
  - Checked each step of the compiler parses C code with Atalla intrinsics, lower it through IR, packetize, and generate Atalla assembly.
  - Tried some simple program to test end-to-end and made sure every stage is working.


## Design Choices
- **Frontend Modularization:**
  Separating the frontend parser into different modules for original C code and Atalla-specific instructions.

- **Pipeline Validation:**
  We made sure that each stage in the entire pipeline works correctly from input C code to final assembly.

- **Final Report:**
  The final report follows the compiler flow starting from frontend parsing to IR, codegen, then to packetization.


## END OF THE SEMESTER!!!

