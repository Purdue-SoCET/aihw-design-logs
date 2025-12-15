
State: Not stuck on anything

# Progress
1) Pcacti modeling
Sweept the Vector Register File architecture in pcacti (90nm–5nm, 1–16 banks) to nail down the optimal configuration for our 16KB, 512-bit design. The breakthrough happened when I caught that the tool defaults to generic bidirectional ports, which was blowing up our area estimates; switching to dedicated 1 Read / 1 Write ports slashed the periphery overhead by ~42%. The data now confirms that 4 Banks is our "sweet spot"—it delivers a ~12% speedup over a single bank without the diminishing returns and massive routing penalties of 8 or 16 banks. I also quantified the "Vector Tax," proving that our wide 512-bit interface is the primary area driver (costing ~4.7x more than a narrow baseline) rather than the bitcell count itself. Decision: Proceeding with the 4-Bank, 1R/1W configuration.

2) Updated top level architecture
- Coordinated with scheduler to abstract WB arbitration completely to the scheduler instead of a global arbiter. The result collector will replace the wba as a global module that concatanates the total vector and passes through once the entire vector is complete. This increases simplicity of logic in vector core and avoids duplicate arbitration logic. Although not approved yet so not in the top level diagram.  

# Future Plans
- FURF poster
- Design review slides
