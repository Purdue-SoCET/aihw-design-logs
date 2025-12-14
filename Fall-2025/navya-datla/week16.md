State: I am not stuck or blocked on anything. 

Progress: 
- I finished the architecture, contributions, and conclusions section of the final report as well as redid a few of our diagrams to be more readable
- Finished PDH, IPE, Senior Design Proposal and Reflections which were submitted to Brightspace
- Fixed the way that the scalar data was being stored to memory, and were able to verify that an int could be loaded, do an add operation, and store back into memory
- Need to store vector data at 2 byte increments in memory (bf16)
- Still need to fix the scratchpad connection for VM operations
  - Received Scratchpad files from Akshath which we worked on beginning to integrate
  - Need to implement more functionality to work with the tile_id parameter required by the scratchpad. 
  - For this to work, we need to generate a tile_id for each new access to the scratchpad with a different base address
    - we need to have a dictionary that stores the previous pairs so we can either 
      - use the same tile_id on access to a previous base address
      - we can generate a new tile_id if we have not seen this base address before
    - we will increment a global counter which can update the next tile_id

Next Steps: 
- Update the emulator with the scpad and tile_id functionalities so we can test vector load/stores
- Create extensive tests so we can verify correct functionality