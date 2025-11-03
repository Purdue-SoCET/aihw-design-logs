
State: I have a lot on my todo list

# Progress
1) MASKU wrapper file so I can do synthesis
   <img width="579" height="799" alt="Screenshot 2025-10-31 170413" src="https://github.com/user-attachments/assets/b48d7f5e-3731-4f16-9c88-c8857be0869d" />
   
 Had trouble synthesizing this so made a wrapper file with a flop since its easy. Clock port issues and whatnot with synthesis tool. Area for this was minimal as expected.

2) OP Buffer UPDATED RTL & Merging
   <img width="364" height="734" alt="Screenshot 2025-10-31 170706" src="https://github.com/user-attachments/assets/d905b6f2-20dc-494c-8d60-464bb823e58e" />

   Fixed A LOT of issues wrong with op buffer. Transparant when no conflict but when there is a conflict it outputs whatever is held in the temporary registers.  It clears the register state upon a read. Need to implement last part of the logic though

3) Added veggie tests
   Completed the veggie tb but on the integrated module to see how op buffer works with veggie. I was able to debug the issues with the op buffer which was that it was misidentifying when the logic was undergoing conflict. Ready gets set low as soon as conflict is detected so did not hold data long enough.

# Future Plans
- Finalize the op buffer
- Cacti still
- add the test to write to every bit of veggie
- Jings list from wednesday meeting

