StateL Currently having trouble with verification since once line of RTL causes a "fatal error" but has literally no reason why. Even though the same line works in different locations

# Progress
1) VEGGIE REDESIGN

<img width="762" height="863" alt="Screenshot 2025-10-10 224454" src="https://github.com/user-attachments/assets/d2e25afb-3c22-4116-9c8e-281041a32bc0" />
<img width="509" height="1024" alt="Screenshot 2025-10-10 224514" src="https://github.com/user-attachments/assets/f102756d-e55f-449a-8515-1a2881ebbb53" />
<img width="713" height="941" alt="Screenshot 2025-10-10 224527" src="https://github.com/user-attachments/assets/e201de2b-f11e-4691-82fe-aee099954678" />
<img width="762" height="449" alt="Screenshot 2025-10-10 224534" src="https://github.com/user-attachments/assets/e7a790bb-95b0-4370-9a21-28132b957711" />

Same structure as the previous veggie file. Lines 36 and 37 are the ones causing the "fatal error" but other than that the waveforms fully load. Currently working on a comprehensive tb that tests each of the sections of the sectors of the veggie file. Conflict logic is much more complicated than previously due to having to account for a varibale number of ports. New specifications include read AND write ports (4 writes and 4 reads) with only WW and RR conflicts. I at first tracked conflicts from the port perspective which made for very complicated arbitration logic. So I changed the logic to understand conflicts from the bank perspective which made the arbitratino logic WAYYYY simpler. I tried to make everything parameterizable in case we run into area constraints in the future.

