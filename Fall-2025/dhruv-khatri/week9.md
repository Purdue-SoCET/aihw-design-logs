## State
I am not stuck with anything. Only Prof Vijaykumar's exams

## Progress (565 exam + assessment for an internship)
* Added loops to tb from last week for testing row_hits and row_conflicts
* Changes can be found on my [github branch](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv). Commit name - "added loops for row hit and row conflicts"

## How the loops work
* Started with row miss. Opened row 0 of all banks of all BGs
* Accessed row 0 of all banks. Should now be a row hit
* For row conflicts, accessed all rows expect row 0 for all banks
* All test cases are passing

## Future plan
* Finish this integration tb without the Micron model. Tri is almost done with Micron tb
* Do the coverage report for modules