State: I am not stuck.

## Progress

Sunday meeting:
- Laid out structure of packetization:
1. Break code into Basic Blocks
    - Basic blocks are blocks of code without any branching instructions. These can be easily packetized due to determinism of executios
2. Construct DAGs
    - Directed Acyclic Graph can be used to track dependencies between basic blocks
3. Packetize s.t. 
    - global ld/st order is maintained
        - loads and stores are anchors that signify that all code before and after them must remain in that order to maintain intended functionality
    - adjust for FU latency
        - functional unit latency will be provided later, need to account for that as well
4. Minimize total latency
    - minimization problem
5. Rerder packets

Steps 1&2 should already be done by PPCI in the IR optimization stage, need to find this and add steps 3-5. We will first focus on basic packetization in step 3 and once that is tested and working properly, we will add the other features.

Another achievement of the sunday meeting was fully uploading the generated scalar ASM to a .S file, without extraneous logging output. What remains now is to fix linking bugs and we will be able to generate an executable file.

Scheduler team design review takeaways:

* Number of instructions in packet is still variable -- do NOT hardcode 4 anywhere
* Currenly 16 check and 16 set bits (also still variable)
* Register allocation should keep track of banks and bank conflicts
* Need to look into register allocation techniques and find research on banking stuff
* 256 registers split into 4 banks -- same as our registers we create in registers.py?
* FU delays will be provided later
* Vector and mask registers are  separate register types

Individual work on vector frontend:

Added a 'vec' type variable to parser, so far only able to parse something like 

``` vec v1; ```

Which is optimized out of the IR by the compiler since it has no value. The next major step is to figure out how to load the vector values into the vector registers.

We are not able to simply say
```vec v1 = {1,2,3,4,5};``` since we do not have a vector alternative to a LI instruction. We will need to explore several options of how to implement this data. One way would be to somehow allocate a memory space somewhere outside of the C program and simply reference it by address. This would look like

```vec v1 = 0xDEADBEEF;```

This would get translated into

vreg.ld r1, 0(0xDEADBEEF)

Our next step is to figure out how to load the vector data into memory, among next steps from past weeks.