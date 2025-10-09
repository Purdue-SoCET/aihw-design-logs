**State**

Not exactly stuck, but quite busy with ECE 437's single-cycle processor lab (due 2025-09-16). Progress may be slower this week.

---

## Progress highlights

- Reverse-engineered the row-dependent swizzle mapping and validated reversibility.
- Confirmed the approach reduces systematic bank conflicts for typical tensor access patterns.
- Collected an early RTL I/O / control signal list and next-step microarchitecture tasks.
- Diagram (draw.io) reference: https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22Tro5ICBytG0uPzhBu2ZE%22%7D

---

## Swizzle / Un-swizzle — concept

Core idea: map each logical lane to a physical bank using a reversible, row-dependent permutation so that consecutive rows spread accesses across banks and avoid repeating bank conflicts.

Mathematically the mapping used is:

$$
	ext{swizzled\_bank} = \text{lane} \oplus \bigl(\text{row} \& (\mathrm{NUM\_BANKS}-1)\bigr)
$$

Inverse (to recover lane ordering when assembling a vector read):

$$
	ext{lane} = \text{swizzled\_bank} \oplus \bigl(\text{row} \& (\mathrm{NUM\_BANKS}-1)\bigr)
$$

### Example helper (Python)

```python
NUM_BANKS = 32

def _row_lane(abs_row: int, cols: int):
    """Return (banks, slots, valid) for a logical row.

    - banks: list of bank indices (per lane) after swizzle
    - slots: per-lane slot/address (here simply repeats abs_row)
    - valid: mask for active lanes when cols < NUM_BANKS
    """
    # Lower bits of the row index (mask depends on NUM_BANKS)
    low = abs_row & (NUM_BANKS - 1)

    # Row-dependent permutation: lane ^ low
    banks = [(lane ^ low) & (NUM_BANKS - 1) for lane in range(NUM_BANKS)]

    # Slots (address/row) — here we repeat the row index per lane
    slots = [abs_row] * NUM_BANKS

    # Valid lanes mask for short rows
    valid = [(lane < cols) for lane in range(NUM_BANKS)]

    return banks, slots, valid
```

Why this helps: if the mapping were static (e.g., bank = lane % NUM_BANKS), multiple warps or rows accessing the same column would repeatedly target the same bank(s). XORing with the low row bits spreads those accesses across banks as row changes, breaking up pathological conflict patterns.

---

## Architectural assumptions (early)

- `NUM_BANKS = 32` (parameterizable)
- Scratchpad composed of `NUM_BANKS` independent SRAM banks
- Each bank provides independent `addr` and `we`; read/write concurrency relies on multi-porting or time-multiplexing
- Scratchpad is software-managed (no hardware tags/valid like a DCache)
- Scratchpad is used by the Systolic Array (SA) and Vector units; the CPU and scheduler continue to use DCache

---

## Early RTL signal list (tentative)

Note: signals marked "early" may be refined as system integration decisions solidify

### Very early / likely inputs (from system / DMA / host)

- `data_in [DW-1:0]` — data to write into the scratchpad (from DMA / host)
- `addr_in [AW-1:0]` — physical address or encoded (bank, row, col)
- `we_in` — write enable
- `row_id [4:0]` — logical row index (used for swizzling)
- `col_id [4:0]` — logical column index
- `row_or_col` — selects row-wise vs column-wise transfer
- `base [AW-1:0]` — base pointer for the current tile
- handshake bits — start / ack / ready semantics

### Early outputs (toward SA / Vector cores)

- `data_out [LANES*DW-1:0]` — assembled vector read (one word per lane)
- `valid_out` — asserts when `data_out` is valid (un-swizzled, aligned)
- `ready_out` — SA can accept the next vector
- `busy` — scratchpad is servicing requests
- `stall_in` — back-pressure from SA
- `start`, `done` — tile-level handshake

### Control / config registers

- `config_stride` — stride between logical rows in physical memory
- `config_shape` — tile shape (rows × cols)
- `config_swizzle` — enable/disable swizzle or select swizzle mode
- `interrupt` / `error` — optional exception reporting

---

## Interface-stabilized RTL I/O (per `vec_if` and `sys_if`) — not-so-early

### Inputs (per interface)

- `start_addr [14:0]` — tile start address
- `row_id [4:0]`
- `col_id [4:0]`
- `row_len [4:0]` — tile row length
- `col_len [4:0]` — tile column length
- `isCol` — direction flag (1 = column-oriented, 0 = row-oriented)

### Outputs (per interface)

- `slot_mask [NUM_BANKS-1:0]` — which bank slots are active for this transfer
- `shift_mask [NUM_BANKS-1:0]` — used for lane/column shifts for alignment
- `stall_sys` — back-pressure to system interface
- `done_sys` / `done_vec` — transfer complete signals
- `arr_sys [31:0]` / `arr_vec [31:0]` — aggregated or per-lane data output (may be padded)

Note: data padding is required when `*_len` is not a multiple of `LANES` or `NUM_BANKS`.

---

## Datapath & control considerations

- Swizzle unit: converts `(row, lane) -> (bank, slot)` for physical addressing on writes/reads
- Inverse swizzle unit: converts `(bank, slot, row) -> lane` ordering when assembling `data_out`
- Slot-mask generation: creates per-beat masks for partial tiles (`col_len < NUM_BANKS`)
- Bank arbiter / scheduler: time-multiplexes accesses when ports are constrained
- Optional write buffer: decouples DMA/CPU writes from bank write latencies
- Replay / retry mechanism: handle structural hazards (busy banks or port conflicts) using replay semantics rather than speculative poisoning
- Handshakes: tile-level start/done plus per-beat valid/ready (AXI-Stream-like) between frontend and SA

---

## Example address flow

### Write (populate scratchpad tile)

1. Software/DMA issues a tile transfer with `start_addr`, `row_len`, `col_len`, `isCol`, and `config_*`
2. For each logical `(row, lane)` compute

$$\text{bank} = \text{lane} \oplus (\text{row} \& (\mathrm{NUM\_BANKS}-1))$$

   slot/address is derived from `row`/`col` plus the `base` pointer.
3. Drive `addr` and `we` into the selected bank and write `data_in`

### Read (SA fetch phase)

1. SA requests a logical `(row, lane)` vector
2. Frontend computes the inverse mapping and gathers `LANES` words from banks (via multi-port or time-multiplex)
3. Assemble `data_out` in logical lane order and assert `valid_out`. SA consumes when `ready_out` is asserted

---

## Next steps (short term)

- Complete the RTL block diagram (include swizzle/inverse-swizzle, bank interfaces, arbiter, config block, and handshakes) — target: Sunday
- Finalize the I/O contract (data widths, LANES, pipelining, handshake semantics) with SA owners
- Implement and validate swizzle / inverse-swizzle RTL and a small testbench
- Design bank arbiter and replay logic; model a tile load/store controller and slot-mask generator