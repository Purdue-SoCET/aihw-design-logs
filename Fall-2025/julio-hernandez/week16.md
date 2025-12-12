## Project Update

### State: I am not currently stuck or blocked.

### Progress
1. There was significant progress made in the verification of the backend and scratchpad as a whole. 

2. For the backend spirit of the test remained largely the same. The major advancement was the creation of the an automatic checker and additional test cases. The checker checks how many writes/reads occured and matches the data received with the "data" sent. The additional test cases were for testing the bounds of the base address and to finally test stalling. Every test passed the automatic check and particularly troublesome test cases were look over manually as well. 

3. Work for verifying the entire scratchpad also began. For now only quick smoke test of the individual scratchpad units were created. All of the units compiled individually and passed basic functionality test. There were some small bug fixes and typos that had to be fixed throughout this process. Finally, after quickly verifying basic functionality a test bench for the entire scratchpad was created. For now the scratchpad as whole compiles and passes basic functionality tests.

4. After all that a coverage report for the backend unit was created. The coverage report was for branches and statements. The major backend components returned with 100% coverage and only the swizzle unit was left out. This is because the backend only creates row major request so the column major portion of the swizzle unit is unused. Future could entail creating a special swizzle unit for the backend to help reduce area.

### Next Steps
1. Finish verifying the entire scratchpad thouroughly.

