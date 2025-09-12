State: Not Currently Stuck

Progress:
    # Current focus away from LLVM, implement backend/frontend support using PPCI
       - For any potential LLVM work, did create a fork in amp-llvm in the SoCET github.
    # Work on lowering a custom theta instrunction to assembly code
        - For this, we had to observe the lexer/parser/AST code and modify. Currently being worked to take from AST to IR.
        - Code in fork 'dummy-isa-testing' under 'aihw-ppci-compiler' github.

Next Steps:
    # Work on backend (IR to custom instructions)
        - Extend ISA and Arch classes in PPCI with our own custom implementations (keeping in mind AMP specific things like scalar/vector reg files)
        - For now, focus on doing Scalar instructions
        - If time permits, follow up / research on Thursday meetings point of handling inline asm support.
