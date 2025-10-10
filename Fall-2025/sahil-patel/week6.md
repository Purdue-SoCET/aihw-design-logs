I’m not stuck with anything.

# WEEK 6 — DESIGN LOG

## PROGRESS
- Finished implementing **scalar** instructions (ALU + immediates).
- Started implementing **vector** instructions.
- Set up checks for vector types and widths in the parser/backend.

## DETAILS ON PROGRESS
### Scalar track (wrap-up)
- Verified encodings for add, sub, and immediate forms.
- Round-trip works: parse > encode > print/disassemble > match text.
- Negative tests pass: wrong operand counts, bad registers, immediate overflow.

### Vector instruction bring-up
- Forms to support first: VV (vec, vec), VS (vec, scalar), VI (vec, imm), VM (vec + mask), SA.
- Register classes:
  - VR: v0…vN (vector registers)
  - GPR: x0…xN (scalars) — reused for VS/VI/SA operands
- Type/width rules:
  - Element types (e.g., i8/i16/i32/i64) vs vector width (lanes) are enforced.
  - Parser rejects mixed widths in one instruction.
  - Clear errors for width/type mismatch and bad lane counts.
- Encoders:
  - Reused 64-bit token shape: opcode, vd, vs1, vs2 (or rs1), imm/imm12, optional mask/pred bits.
  - Added helpers for each form to keep operand order consistent.
- Early ops (for testing):
  - add.vv, add.vs, addi.vi
  - Simple moves/broadcasts if needed: mov.vs, splat.vi (names will follow final ISA mnemonics)
- Asm printer:
  - Stable operand order (e.g., add.vv v3, v1, v2; addi.vi v4, v4, 8)
  - Prints memory-free vector ops first; memory vector ops will come later.

### Testing
- Positive tests:
  - Correct lane widths, valid immediate ranges, expected encodings for VV/VS/VI.
- Negative tests:
  - Width mismatch (e.g., v128 with v64), invalid immediate sizes, wrong register class in operand.
- Round-trip text tests for each new mnemonic.

## NOTES
- Instruction packets (hardware bundling to reduce dependencies):
  - We discussed grouping multiple instructions into a packet issued together (VLIW-style).
  - Goal: help hardware schedule independent ops in the same cycle and avoid read-after-write stalls.
  - Compiler impact:
    - Add a simple packetizer step after instruction selection (or a greedy scheduler) to cluster independent ops.
    - Respect obvious hazards: don’t place a consumer in the same packet as its producer.
    - Leave room for a mask/predicate bit if packet format needs it.
  - Short term: keep encodings packet-agnostic; packets can be a metadata layer for now, then mapped to final bits after the ISA team freezes the packet format.

- Keep using only ISA-approved forms: VM/VV/VS/VI/SA (no extra forms).
- Default integer type stays 64-bit across parser and backend.
- PPCI remains our fast path for encode/print; LLVM remains a future option.

## NEXT STEPS
- Finish core vector ALU op set (add/sub/and/or/xor).
- Add mask/predication plumbing (parser flags + encoder bits) once ISA finalizes mask rules.
- Introduce basic vector memory ops next (if scheduled for Week 7): vld, vst with base+offset and alignment checks.
- Expand unit tests:
  - Mixed VV/VS/VI sequences.
  - Error cases for mask width/type, packet hazards when enabled.

