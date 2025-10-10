## State
I am not stuck with anything.

## Progress
Note - 538 exam and 565 PA1 due next week so spent less on the project this week.
Completed implementation and verification of the REFRESH timings from last week. Timing module verification is now complete. Further, discussed an integration plan.

## The integration plan (Calculus in digital design?)
1. Start with the control unit
 a. Integrate and test the init_fsm, command_fsm, and address mapper. Following interactions should be focused:
    i. Check that FSM goes from initialization to command.
    ii. Check that row policy updating happens correctly with the signals supplied by the address mapper.
 b. Add the timing control logic to (a). Control unit should be fully tested here.
2. Add the data transfer unit to (1). Check if the unit is sending and receiving at the correct edge and in correct bursts.
3. Add the signal generator to (2) and test with the micron model
4. The memory controller is now complete in simulation!!!

## Future plan
1. Work on Step 1 (b) of the integration plan. Tri started 1 (a).
2. Synthesize individual models. I'll start with the address mapper and timing control (modules I worked on).


