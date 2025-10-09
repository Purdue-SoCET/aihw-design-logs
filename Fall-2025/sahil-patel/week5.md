I’m not stuck with anything.

# WEEK 5 — DESIGN LOG

## PROGRESS
- Implemented tokens and a simple architecture skeleton.
- Focused on scalar operations first (`add`, `sub`).
- Created custom **scalar** instructions for our new architecture.

## DETAILS ON PROGRESS
### Tokens + simple architecture
- Added 64-bit token layouts with consistent fields: **opcode**, **rd**, **rs1**, **rs2**, **imm/imm12**.
- Set up core files: `tokens.py`, `registers.py`, `instructions.py`, `arch.py`, `asm_printer.py`.
- Registered GPR class (x0…xN, 64-bit) with common aliases (`sp`, `ra`, `gp`) to keep assembly readable.

### Scalar instruction bring-up
- Implemented base ALU ops: `add`, `sub` (scalar-scalar).
- Verified encoding maps: rd/rs1/rs2 fields land in the expected bit ranges.
- Added immediate form for ALU where needed (e.g., `addi` style) with range checks (reject out-of-range immediates).
- Round-trip tests:
  - parse → AST → encode → disassemble/print → compare text
  - negative tests: bad register names, wrong operand count, immediate overflow

### Asm printer + errors
- Asm printer shows mnemonic + operands in stable order (`add x3, x1, x2`).
- Clear, short error messages:
  - “immediate out of range”
  - “unknown register”
  - “wrong operand count for opcode”

## NOTES
- Keep to ISA-approved forms only (no extra forms).
- Default integer type: **64-bit** through parser and backend.
- Consistent field naming across files avoids confusion later (opcode/rd/rs1/rs2/imm/imm12).
- Endianness/alignment for memory will be confirmed with the ISA team before finalizing load/store encodings.

## NEXT STEPS
- Implement **load/store** support (requires basic memory model):
  - Decide address form: `rs1` as base + optional **imm12** offset.
  - Define element sizes: byte / half / word / doubleword. Specify sign/zero-extend on loads.
  - Alignment rules and required traps/handling for misalignment (confirm with ISA).
  - Common mnemonics to start: `ld`, `lw`, `lh`, `lb`, `sd`, `sw`, `sh`, `sb`.
- Update tokens/instructions:
  - Add memory opcodes and verify bit positions for base, dest/src, and offset.
- Expand tests:
  - Positive: base+offset loads/stores; boundary immediates; back-to-back memory ops.
  - Negative: misaligned (if disallowed), offset overflow, writing x0 (if x0 is read-only).
- Asm printer:
  - Print memory as `ld x3, 16(x1)` style (or the ISA’s chosen syntax).
- Small end-to-end demo:
  - Two ALU ops to compute an address, one `sd`, one `ld`, verify round-trip and encoded bits.
