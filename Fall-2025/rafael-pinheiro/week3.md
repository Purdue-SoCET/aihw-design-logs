State: Not exactly stuck, but quite busy with 437's single cycle processor lab (due 09/16). Progress might be slower this week

Progress:
- Reverse engineering of the swizzling's algorithm:
'''
NUMBANKS = 32
    def _row_lane(abs_row: int, cols: int):
        low5 = abs_row & (NUM_BANKS - 1) # Take the 5 lower bits of the row index
        '''
        row-dependent phase : determines how the row maps into banks
        '''
        banks = [(lane ^ low5) & (NUM_BANKS - 1) for lane in range(NUM_BANKS)]
        '''
        Each lane (thread, or column index) generates a bank index
        (lane ^ low5) mixes the lane ID with the row bits
        swizzling -> row-dependent permutation
        Effect (as explained in the different papers and links Akshath sent us): consecutive rows map differently across banks, breaking up systematic conflicts
        How does it do that? No idea, still haven't fully understood the formal mathematical proof
        In the near future, if I have some time I'll take a look at that
        '''
        slots = [abs_row] * NUM_BANKS
        '''
        Slots just repeat the row index
        Each lane still points to the same logical row
        The difference is where in memory (bank) that row’s piece resides
        '''
        valid = [(lane < cols) for lane in range(NUM_BANKS)]
        '''
        Validity mask
        Some rows may have fewer active columns (cols < NUM_BANKS)
        This mask tells which lanes are actually used
        '''
        return banks, slots, valid
'''
    map lane i $$\mapsto$$ bank i % NUM_BANKS $$\rightarrow$$ 

    All threads in a warp that touch column 0 across rows might hammer the same bank → bank conflict.

    This creates serialization, hurting bandwidth.

    By XOR-ing with low5, the bank assignment depends on both:

    - the lane ID,
    
    - and the row index’s low bits.
    
    So each row distributes its columns differently across banks. That means even if all warps access the same column pattern, their accesses land on different banks row-to-row, reducing conflicts and improving throughput.

Next Steps:

- RTL Diagram complete by Sunday
    - Data I'd need from the Systolic Array