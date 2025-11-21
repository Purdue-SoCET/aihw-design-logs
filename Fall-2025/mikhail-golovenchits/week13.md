State: I am not stuck with anything

## Progress

- Created the research poster during the sunday meeting.
- Attended both the research poster presentation and the senior design presentation.
- During the poster presentation explained all aspects of the compiler project to judges with different backgrounds. It was interesing to explore how people with little to no exposure to this technology, much less compilers, gain information about it. The questions people with little technical background ask were sometimes out of the box and made us rethink some design/documentation choices we made thanks to this outside perspective.
- Feedback from senior design review:
    - We were asked why can we not just use RISC-V to instruct the Atalla processor. This was due mostly to the need for instructions like gemm, as well as a custom bitsize of each instruction.
    - We were made aware of the tradeoffs of using Python for this compiler as opposed to more efficient languages like C. We mainly highlighted that we chose Python due to its simplicity and extendability.

- Clarified programming model to be used for instructing the processor.
    - Confirmed that GEMM and SDMA work on vector registers.
    - A vector datatype is the same as a bf16 array, since both are stored in vector registers.

## Next steps
- Finish vector ISA patterns and frontend for GEMM, SDMA, etc.
- Extend BinOp processing to output vector operations.
- Begin work on the final report.