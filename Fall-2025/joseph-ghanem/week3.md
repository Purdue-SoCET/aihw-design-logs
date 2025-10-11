State: Stuck on verificatoin as .wav is not working

# Progress
1) Veggie Microarch
<img width="1605" height="722" alt="Screenshot 2025-09-14 165431" src="https://github.com/user-attachments/assets/af986e51-1f1f-42df-ad8a-22be45d8bca3" />
This week I finalized the RTL of the veggie file. The specification involves the capability to read 2 vector data banks, 1 vector mask bank, and 1 read port. This design consits of control logic that determines which bank the read and write selects should go to in addition to an FSM that can ensure proper utilization of the banks buses during bank conflicts. Each bank consits of a read OR a write port. I decided to utilize a special "control bank" that ony contains the vector mask register (v0). This is to limit the bank conflicts in Bank0 since vector mask is the common case. The operand eater is used to store the intermediate operand in the case of a conflict. I decided to include this to hold onto the operands during the 2 cycle conflict process. I also plan to use an immediate value to index the vm register to hold 16 masks. So bit 0 in each element spot corresponds to mask 1, bit 1 in each elem spot corresponds to mask 2, etc. This way for only 4 more bits you get full utiliziation of all the 32*16 vector register

2) Veggie RTL Implementation
<img width="536" height="438" alt="Screenshot 2025-10-10 213835" src="https://github.com/user-attachments/assets/86b2881b-27fe-49f5-98d6-b250ada0d9e6" />
<img width="517" height="799" alt="Screenshot 2025-10-10 213828" src="https://github.com/user-attachments/assets/e98f1b4a-1dc6-4128-8bde-1baf6246c681" />
<img width="546" height="752" alt="Screenshot 2025-10-10 213819" src="https://github.com/user-attachments/assets/324d3f13-cf06-4234-8598-509d3971866d" />
<img width="570" height="888" alt="Screenshot 2025-10-10 213807" src="https://github.com/user-attachments/assets/62a1e98b-99a8-432d-96e8-174123f8594a" />
<img width="488" height="955" alt="Screenshot 2025-10-10 201353" src="https://github.com/user-attachments/assets/d8f5c320-a40b-4db4-bc6a-ec5a14617202" />

The RTL implementation includes multiple parts:
- Control logic (bank arbitration, conflict detection and conflict handling)
- Bank Gen
- Mini operand buffer

Some design choices were to interleave entire vector register utilizing the mod operator. The conflct variables track when any conflicts occur. 

# Future Plans
- Finalize ISA
- Vector SD Presentation
