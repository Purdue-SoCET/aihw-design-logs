
State: 565 was COOKED so slower progress week
# Progress
1) Fixed mask unit to not have VM bit
   <img width="737" height="336" alt="Screenshot 2025-10-31 165734" src="https://github.com/user-attachments/assets/8c7cda8f-5781-43cb-ba6b-244c63391899" />

  Mask 0 register now all 1's, so no need to have vm bit anymore especially since it is not in the ISA. Therefore I changed the unit to reflect this and now only do splitting. 

2) OP Buffer base RTL
   
# Future Plans
- Fully verify veggie file
- finish lane implementation + verification
