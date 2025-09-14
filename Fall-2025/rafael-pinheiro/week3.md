State: Not exactly stuck, but quite busy with 437's single cycle processor lab (due 09/16). Progress might be slower this week

Progress:
- Reverse engineering of the swizzling's algorithm:
NUM_BANKS = 32

```
def _row_lane(abs_row: int, cols: int):
    # Take the 5 lower bits of the row index
    low5 = abs_row & (NUM_BANKS - 1)  

    # Row-dependent phase: determines how the row maps into banks
    banks = [(lane ^ low5) & (NUM_BANKS - 1) for lane in range(NUM_BANKS)]
    # Each lane (thread, or column index) generates a bank index
    # (lane ^ low5) mixes the lane ID with the row bits
    # Swizzling -> row-dependent permutation
    # Effect (as explained in the different papers Akshath sent us):
    #   consecutive rows map differently across banks, breaking up systematic conflicts
    # How does it do that? Not fully clear yet, the formal mathematical proof is tricky
    # Might revisit this later for a deeper dive

    # Slots just repeat the row index
    slots = [abs_row] * NUM_BANKS
    # Each lane still points to the same logical row
    # The difference is where in memory (bank) that row’s piece resides

    # Validity mask
    valid = [(lane < cols) for lane in range(NUM_BANKS)]
    # Some rows may have fewer active columns (cols < NUM_BANKS)
    # This mask tells which lanes are actually used

    return banks, slots, valid

    map lane i $$\mapsto$$ bank i % NUM_BANKS $$\Longrightarrow$$ 

    All threads in a warp that touch column 0 across rows might hammer the same bank → bank conflict.

    This creates serialization, hurting bandwidth.

    By XOR-ing with low5, the bank assignment depends on both:

    - the lane ID,
    
    - and the row index’s low bits.
    
    So each row distributes its columns differently across banks. That means even if all warps access the same column pattern, their accesses land on different banks row-to-row, reducing conflicts and improving throughput.
```

- Assuming Scratchpad is:

    - Organized as NUM_BANKS separate RAMs

    - Each bank gets its own we and addr

    - Typically multi-ported or time-multiplexed to support R/W simultaneously

- Too early RTL signals I may need:

    - data_in [DW-1:0] – ~~data from SA~~ Julio

    - addr_in [AW-1:0] – ~~physical address (linear or bank,row,col)~~

    - we_in – ~~write enable~~

    - row_id

    - col_id

    - row_or_col

    - base

    - handshakes 

- Too early RTL signals I may be sending out from the frontend:

    - ~~addr_req [AW-1:0] – logical (row, col) request from systolic frontend~~

    - ~~addr_bank [log2(NUM_BANKS)-1:0] – bank index chosen by inverse swizzle~~ $$\rightarrow$$ SA already knows what it wants

    - ~~addr_slot – row/col inside the bank~~

    - data_out [LANES*DW-1:0] – wide vector, one word per systolic lane

    - ~~valid_out – asserts when data_out is correctly un-swizzled~~

    - ~~ready_out – SA can accept next word(s)~~

- Control signals:

    - start / done – tile-level handshakes.

    - config_stride, config_shape, config_swizzle – how to interpret logical $$\rightarrow$$ physical mapping.

    - stall_in – SA can back-pressure the frontend

    - busy – scratchpad actively serving requests

Reminder:

swizzled_bank = lane ^ (row & (NUM_BANKS-1))

$$\rightarrow$$

lane = swizzled_bank ^ (row & (NUM_BANKS-1))

Diagrams:

https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22Tro5ICBytG0uPzhBu2ZE%22%7D

- Not so early RTL input signals

    - For each vec_if and sys_if:

        - [14:0] start_addr,
        - [4:0] row_id,
        - [4:0] col_id,
        - [4:0] row_len,
        - [4:0] col_len,
        - isCol


- Not so early RTL output signals

    - slot_mask
    - shift_mask
    - stall_sys
    - done_sys
    - done_vec
    - [31:0] arr_sys
    - [31:0] arr_vec
      - Data might be padded if *_len $$\neq$$


Next Steps:

- RTL Diagram complete by Sunday
    - Data I'd need from the Systolic Array
- Start working on microarchitecture of front-ends