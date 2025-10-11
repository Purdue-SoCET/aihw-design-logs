State: Not stuck at the moment

# Progress 
1) Further refined vector top level RTL based on team feednback
<img width="1637" height="812" alt="Screenshot 2025-09-24 224303" src="https://github.com/user-attachments/assets/97732b0d-ba94-43eb-8677-4530ef82aca7" />

- VLS is now a global component since vector components are loaded and stored together at once. Not needed to be per lane, limited hardware area
- Cross bar added for shifting to interact with systollic array
- VBU unit for operations on mask being applied to an instruction instantly

2) Systollic array convolution offload
Met with Saandiya and Nikhil to discuss how we can change the Vector top level to Systollic Array. 5 bits will be added to the ISA and an additional functional unit will talk to Systollic array inside the lanes itself.

3) Prepared for Design Review
https://docs.google.com/presentation/d/1zGqpBYe6Qenp7KOvmsEcLhguIXTZgIaqBRJG4hOVtog/edit?slide=id.p#slide=id.p

4) Lane.SV Pseudocode
<img width="535" height="519" alt="image" src="https://github.com/user-attachments/assets/83bbf5b3-94b2-4a8b-a33e-cae245604a0c" />
Utilized FU pipeline latch to also be part of the counter. Do not have the FU's' to fully implement yet but setup the structs for in/out and general structure.

5) Verified Mask unit
<img width="431" height="1015" alt="Screenshot 2025-10-10 222227" src="https://github.com/user-attachments/assets/ce2cae43-d671-4099-99e4-9b4145605c6f" />
Passed basic unit test cases


# Future Plans
- Finalize bit spec
- Finish MASKU and verification
