# Week 2

State: I am not stuck with anything, don't need help right now.

## Progress

- Meetings:
    - Attended the Computer Architecture Fundamentals focus group and went over performance laws (Iron Law, Amdahl’s Law) and how they are related to architecture/compiler.
    - Attended the Compiler group meeting and set up our project plan:
        1. prototype compiler supporting a dummy instruction theta.
        2. basic custom ISA integration.
        3. ISA refinement.
        4. begin developing a standard library.
    - Discussed backend implementation strategy and decided to use PPCI for simpler integration.

- Frontend:
    - Traced the compiler frontend from parser to AST construction then to IR generation.
    - Investigated how PPCI handles parsing rules and keyword registration.

- Custom Theta Instruction:
    - Added theta as a keyword in the parser by extending self.keywords.
    - Implemented parsing rule in parse_primary_expression() to handle theta syntax.
    - Added on_theta function to semantics module for IR generation.
    - Updated parsing to accept two arguments instead of one.
    - Switched from directly consuming arguments to using parse_expression.
    - Successfully generated IR for theta and confirmed that it prints correctly.

- Machine Code:
    - Verified that PPCI successfully prints IR and generates machine code for default functions.

- Evidence:
    - Example test program:

    ```c
    int main() {
        inline("
            theta x0, x1, x2
        ");
        return 0;
    }
    ```  

    - Output successfully includes `theta` IR node and lowered machine code placeholder.


## Meeting Notes

- ISA Discussion:
    - Initial draft ISA planned as 32-bit.
    - Vector loads/stores, arithmetic ops, reductions, masking, and shifts.
    - Register file structure (SP, PC, special registers).
    - Vector register width and type handling.
    - Whether compiler or ISA should enforce data-type rules.

- Software Model Discussion:
    - Need custom instructions to bridge C to Assembly.
    - Full ISA support targeted within 4 weeks.
    - Compiler will manage register allocation directly.


## Design Choices

- Used theta as a placeholder instruction to bootstrap compiler testing. This allows us to exercise parser, AST, and IR pipelines before the ISA is finalized.
- Chose to integrate theta by extending the existing expression parser rather than hardcoding it.
- Decided to begin with PPCI due to simplicity and the need for rapid deliverables.

## Next Week

1. IR Formatting:
    - Study PPCI IR node structure and formatting rules.
    - Add unit tests for theta parsing and IR generation.
    - Confirm parse C with theta to AST to IR to machine code then print.

2. Backend Preparation:  
    - Begin exploring backend hooks for custom tokens and encoders.
    - Sketch draft architecture file arch.py structure.

3. ISA Integration:  
    - Sync with ISA team once the green card draft is available.
    - Start mapping theta lowering into machine instructions.

4. Documentation:  
    - Write internal notes explaining parser modifications for theta.
    - Add diagrams of PPCI flow.