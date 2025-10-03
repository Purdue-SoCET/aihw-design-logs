State: I am not stuck with anything

## Progress

- Determined that in order to lower the IR to assembly (codegen), we need to fully flesh out the custom backend architecture. This backend architecture will be loosely based off riscv, with modifications based on the custom architecture of the chip.

- Added all scalar instructions templates to amp_arch branch of aihw_ppci_compiler based on the green card, using token layout specified in the bitspec
    - Based instruction functions off of how they are done for riscv in ppci

- During the sunday meeting, we were briefed on the packeting requirement for sending instructions to the processor. This will have to wait until we are able to fully implement at least scalar instructions. We will need to decide whether this will be done during codegen optimization or using a postprocessing script.

## Next steps

- Create slides and present our progress up to this point on 9/28 design review
- Hold a team work session to finish the architecture and be able to translate scalar instructions to out custom ISA. This shouldn't require modifying codegen as scalar instruction parsing should be the same as for RISC-V, just with different operation mnemonics.
- Once that is done, we can split work between packetizing and implementing vector instructions.
