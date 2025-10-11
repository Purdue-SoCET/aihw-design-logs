# Week 6

State: I am not stuck with anything, don't need help right now. 

## Progress
- **Front-end (Parsing and AST):**
    - Completed the C parser for scalar instructions.
    - Built out the full abstract syntax tree node library to translate scalar C constructs into PPCI’s AST framework.
    - Verified that simple scalar programs (arithmetic, branching, loops) parse correctly into the AST.

- **IR Generation:**
    - Constructed the code generator that maps AST nodes to the PPCI Intermediate Representation (IR).
    - Ensured that scalar constructs such as assignments, arithmetic, and control flow translate into a coherent IR stream.

- **Back-end (Attala ISA Integration):**
    - Implemented the architecture and instruction folder for Attala inside `arch/`.
    - Wrote the mapping logic that identifies scalar IR instructions and stores them in a compiler-managed instruction list.
    - Built the code generator to stream this instruction list into Attala assembly code, effectively completing the end-to-end scalar compilation flow.
    - This milestone means that I can now write a scalar C program and successfully compile it down into Attala assembly — a critical deliverable for our design review.

- **Vector Instruction Work:**
    - Created the skeleton file for Attala vector instructions, defining the token format and placeholders for operands.
    - Began designing vector opcodes that extend the scalar set, ensuring consistency in encoding with our ISA spec.

- **Research on Instruction Packetization:**
    - Started reading about packetization techniques in VLIW-like compilers, where independent instructions are grouped into “packets” that can execute in parallel.
    - Explored static (compile-time) vs. dynamic (runtime) approaches. Since PPCI and our ISA design lean toward static control, my focus is on **compile-time packetization**.
    - Initial notes suggest a packet could be formed at the IR level, grouping independent operations into a four-instruction bundle before lowering to Attala assembly.
    - Considering hazards: read-after-write (RAW) will need to be carefully checked in the IR stage before instructions are packed. This would let us expose parallelism to hardware while keeping scheduling complexity low.


*Test C code*
```C
int main() {
    int a1 = 4;
    int a2 = 3;
    int ar;
    theta(ar, a1, a2);
    return 0;
}
```
*Generated IR*
```
module main;

global function i32 main() {
  main_block0: {
    blob<4:4> alloca = alloc 4 bytes aligned at 4;
    ptr alloca_addr = &alloca;
    blob<4:4> alloca_6 = alloc 4 bytes aligned at 4;
    ptr alloca_addr_7 = &alloca_6;
    blob<4:4> alloca_8 = alloc 4 bytes aligned at 4;
    ptr alloca_addr_9 = &alloca_8;
    jmp main_block1;
  }

  main_block1: {
    i32 num = 4;
    store num, alloca_addr;
    ptr num_0 = 4;
    ptr tmp = alloca_addr + num_0;
    i32 num_1 = 3;
    store num_1, alloca_addr_7;
    ptr num_2 = 4;
    ptr tmp_3 = alloca_addr_7 + num_2;
    theta ptr alloca_addr_9 = &alloca_8, ptr alloca_addr = &alloca, ptr alloca_addr_7 = &alloca_6;
    i32 num_4 = 0;
    return num_4;
  }

}
```


## Design Choice
- **Scalar to Vector Extension:**
    I chose to mirror the scalar instruction framework in building the vector instruction file. This reduces implementation risk and ensures code reuse, since vector instructions often share encoding structures with their scalar counterparts.

- **Packetization Placement:**
    We are deciding whether we should implement packetization in the IR stage or the code generation stage
    - At the IR level, dependencies between instructions are explicit and easier to check (RAW, WAR, WAW).
    - If I wait until assembly, I risk missing opportunities for parallelization that were visible earlier.


## Next Week
1. **Implement vector instructions** beyond the skeleton:
 - Add basic arithmetic ops (`vadd`, `vsub`, `vmul`).
 - Define load/store semantics for vectors (alignment and stride issues need attention).
 - Write simple test programs in C and verify end-to-end compilation to Attala assembly.

2. **Advance packetization research:**
 - Prototype an IR-level pass that identifies independent instructions and groups them into bundles of up to 4.
 - Define the packet format in Attala assembly (likely curly-braced groups or prefixed packet markers).
 - Document hazards and how the compiler will resolve them (RAW, WAR, WAW).
