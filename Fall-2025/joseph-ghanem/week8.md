
State: 565 was COOKED so slower progress week
# Progress
1) Fixed mask unit to not have VM bit
   <img width="737" height="336" alt="Screenshot 2025-10-31 165734" src="https://github.com/user-attachments/assets/8c7cda8f-5781-43cb-ba6b-244c63391899" />

  Mask 0 register now all 1's, so no need to have vm bit anymore especially since it is not in the ISA. Therefore I changed the unit to reflect this and now only do splitting. 

2) OP Buffer base RTL
   Created draft for op_buffer RTL and added dvalid and mvalid signals to the veggie to help op buffer. Decided to make it a seperate module but plan on making 1 module that integrates both.

3) Veggie synthesis
   Synthesized veggie with 1, 32, and 64 registers per bank. Area is kind of huge, results found in area excel sheet
   
# Future Plans
- Cacti for area planning
- integration + added veggie tests
