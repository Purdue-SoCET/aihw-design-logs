## State
I'm not stuck with anything.

## Progress
* Checked Mode Register (MR) loading during initialization
* Made report outline

## MR loading
* My thought was that incorrect MR loading during initialization was causing the not being able to change the Micron model speed error
* That's not the case. Micron throws an error on loading non spec compliant values into the MR 
* Changing Micron model speed remains to be done for next semester students

## Report Outline
* Discussed report outline with Tri for the blocking version
    - Introduction
        + Background of why we need controller
        + Industry standard practices (use of HBM/GDDR) for higher bandwidth in AI accelerators
        + Cycle accurate simulators (like ramulator) also used but that is limited to architecture concepts
        + HBM cannot be possible in tape-out. Some older version of DDR is an achievable option
        + Hence, this lays the groundwork for DRAM controller tape-out
    - Implementation
        + Top level overview
        + Detailed design decision
            * Address mapper - why Ra-R-B-BG-C policy and open row policy used. Explain with DDR4 structure
            * How refresh is handled. Why refresh is not handled on every state
            * Write masking feature when not writing all locations
    - Verfication plan
        + A small cache reference model added by Tri for verification
        + Best, worst, and average cases
    - Results
    - Analysis of results
        + Less than 10% bandwidth even for all row hits
    - Drawbacks and Future work
        + Obviously need a non blocking controller for performance

* Blocking/Non blocking/AXI report all in one
    + Will have a common background for why DDR controller
    + Each project will then have it's own chapter

## Future plan
* Complete report
* Complete other VIP requirements

