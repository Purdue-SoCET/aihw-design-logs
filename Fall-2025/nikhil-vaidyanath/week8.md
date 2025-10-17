## State: I am a bit stuck with EDA tool access. Currently contacting relevant members to get cae group access.

## Progress
This week had Fall Break, and progress is much less due to that.

On Wednesday I met with Vector Core where we came to know of a couple errors in the ISA. For compiler team these instructions and the bitspec needed to be changed ASAP. Our earlier work wasn't completely correct and also had more of a "microarch definition" instead of a ISA level definition seen in RISC-V Green Card. We have since changed our instructions to match an ISA level definition and be more correct. While unintuitive, the gemm instruction carries out a vector matrix multiplication, and the result stored in "rd" or vdst in this case has been updated to show that. Note, we will still need to transpose (Sooraj click) the resultant matrix. Other changes were made to shift instructions to change the type and immediate usage (somewhat as outlined earlier, 1 bit for direction and multiple bits for shift amount)

Final instruction list with changes is in Sheet 5 of this Excel Sheet: https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?gid=739608826#gid=739608826

We also worked on the abstract and got it checked off by the GTAs. Our abstract explains that we worked on a methodology to allow vector core to complete convolution as a GEMM (and thusly GEMM by itself as well) acheiving levels of ILP while improving area compared to earlier implementations which would have either been impossible to implement or wasted large amounts of bandwidth and storage elements (SRAM, FFs, etc.).

Abstract: https://docs.google.com/document/d/1gBZ6_h6uZCL9Xjy55gx3o7PBXcEfP2HXks3DoknYAj0/edit?tab=t.0

## Tasks
   I have given the FIFO to Joseph and he is using it for the operand buffer, taking that off of my plate for now. I will be refocusing on GSAU development again. Our tasks are to generate a testplan as soon as possible and then get it checked off to be as exhaustive as possible with respect to edge cases and such. Due to scheduler delays, we have a one week extension for RTL freeze. We have a significant amount of RTL done, but have not completed testplan/verification.
   Deadlines:
     Exhaustive Testplan - due by 10/19 (will get checked off on 10/19 sunday work session)
     RTL Freeze (fully verified) - due by 10/26 (following sunday)
     Integration Done - previous deadline was 11/2, extended deadline is 11/9?

## Notes
   Saandiya and I came up with some latency figures:
   - Best case is 64 cycles, 32 right in SA and 32 down for last values to trickle out
   - Worst case is 160 cycles (64 + 96 cycles), 96 comes from wb buffer backpressure

   Likely not taken into account all systolic array factors. Need to contact GTAs, Vinay, and person in charge of WB buffer to confirm latencies 

## Future Plans 
   Some future notes are that we need to get a synthesis done on our workflow to get a number for clockspeed and area. This may not be representative of inter unit paths and such but is a good baseline for the chip as a whole because we need to know if our goals for clock speed and area can be hit for a possible tape out.