## State
I am not stuck with anything.

## Progress
Started integration of init_fsm, command_fsm, address mapper, and row policy modules.
Researched about PHY and FPGA testing.

## The Integration (Calculus in digital design?)
1. Integrated the init_fsm, command_fsm, address mapper, and row policy modules
2. Initialization sequency is handled correctly on reset, signalling command FSM once complete
3. There are a few discrepencies in the way Tri and I handle interfaces. So, integration took a little while. 
   However, a consistent way is prefered.
(Evidence is on [github](https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_dhruv))

## PHY and hardware testing
1. I incorrectly assumed PHY is a separate chip. It is always on the same die of the SoC. So, PHY logic will be needed for tape-out.
2. Prof Swabey mentioned working with a single memory chip will be easier for signalling. May have to use chips soldered on a PCB instead of DIMMs. Have a meeting scheduled 
   with Prof Swabey to talk more.
3. For FPGA testing, we need an FPGA with soft memory controller. Found [DE25-Nano](https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=123&No=1384&PartNo=2) which has LPDDR4 memory. [Datasheet](https://www.intel.com/content/www/us/en/docs/programmable/762191/current/external-memory-interface-in-fpgas-and-socs.html) says it has a soft controller. However, Will need to check if any MC logic difference with DDR4.

## Future plan
1. Have the init_fsm, command_fsm, address mapper, and row policy module integration done by next week.
2. Start to synthesize individual models. I'll start with the address mapper and timing control (modules I worked on).