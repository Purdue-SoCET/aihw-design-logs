> This week was focused on completing the Systolic Array and Scratchpad units for the Cycle Accurate Simulator and getting onboarded for the compiler work. Parallely set up verilator and the testbench components. Not actually worked on it since.   

## State
[NONE]

## Arch Updates
[NONE]

## Progress
- While thinking of programming model, I went through [this paper](https://arxiv.org/pdf/2511.08083). Interesting exploration of how a bunch of researchers infrastructure-ized kernels for AMD. 
- Check out the [atalla-sim](https://github.com/Purdue-SoCET/atalla-sim/tree/master) code for a cleaned up repo structure, with a simulatable Scratchpad, Systolic Array, Crossbar and Veggie File.
- Setup the C++ Verilator stuff, and a [Verification.md](https://github.com/Purdue-SoCET/atalla/blob/main/docs/verification.md) guide. 
- Worked with the Scheduler team to finalize the ISA [Atalla Bit-Spec sheet](https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?usp=sharing). This should have been done 3 weeks ago, but it seems to a miscommunication from their end to Compilers. 
- Spoke with Heung about Compiler next steps and how to work with him on instruction scheduling, so that his packetization works next. 

## Future Plan
- Will focus on programming model during Thanksgiving + Report. 
- Plan to write a first pass for ppci. 