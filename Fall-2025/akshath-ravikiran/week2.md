> This week was spent brainstorming with the GTAs on timelines and group formations. I focused primarily on getting the team up-to-speed, and ideating with Systolic Array on our interactions. We also went through Crossbar designs, and why we prioritize MINs > Mesh/Naive crossbar. 

## State

[STALLED] I am stuck on the Systolic Array <=> TCA <=> Scratchpad interactions. Tags: Saandiya, Jing, Sooraj. 
- Context: 
    - We've not defined a clear TCA architecture. There are tons of uncertainties with this protocol as of now. 
    - The TCA Sim, as defined [here](https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_akshath/tmp/TCA_Sim.ipynb) is incomplete. It does not contain `routing` algorithms of the PSUM outputs into correct buffers, nor how do we handle timing of those transfers into the Scratchpad.
        PSUM Buffers have implicit timing in their structure, which assumes that every N+1th buffer takes in the *(M+1)th value in the T+1th cycle. 
        However, the sim does not guarantee that the *(M+1)th value comes in the T+1th cycle. There is an undefined gap, which changes with parameter values. 
    - We do not have a clear understanding of how the data will be loaded into TCA either. TCA will need to latch data, and then re-order somehow.
    - My suggestion? Have a crossbar sitting between the Scratchpad into TCA. Have the TCA maintain a wide buffer (~512b), and another crossbar into the Systolic Array FIFOs
        - How will this help? It allows her to load data on a row-or-col basis, and then route the required values into the correct Systolic Array FIFOs. 
        - How will this scale? REALLY BADLY! 
        - How will this logic look? Bad! We don't know the math for this.
- How does this effect Scratchpad? 
    - Scratchpad was initially meant to efficiently support the Systolic Array, and offer a split-transaction memory load. 
    - Currently, without such an intuition of the workload, we're stalling on the changes we'd need to make to support them. 
- Update: None this week. 
    > **This will be clarified by Week 4-5 in [Saandiya's](../saandiya-kpsmohan/) well-maintaining logs. Hint: We offload this scheduling onus into the SW, and make Systolic Array an offload of the Vector Core. Check [Joseph's](../joseph-ghanem/) logs for a Vector Core perspective.**
- What's pending: 
    - A concrete algorithm, confirming the way TCA loads data from Scratchpad into the Systolic Array, and coordinates it out through PSUM Buffers. 
    - A cycle-accurate simulator of the Systolic Array!
    - SW Routines for running these workloads on the Sim. 

## Arch Updates
#T0. Cleaned up last semester's [RTL](./assets/ConvController_TMA-Page-2.drawio.png). 
#C0. Crossbar will be a high latency, and large area module. We will not use the Mesh crossbar -- guarantees 1 cycle latency, but high area, power and a PD nightmare. We will be developing MIN - Multi Stage Interconnection Networks - based crossbars. 
#S0. We will not be performing paging in the Scratchpad at the SW level. 
- Context: 
    - Scratchpad is a SW Controlled Cache. This means that the SW needs to keep track of where data lives and how long it'll live in the Scratchpad. 
    - Initially, we moved towards allowing the Scratchpad to "Page" a section of the Scratchpad and then store many tiles within it. 
    - Since Paging was meant to not be exposed to the HW, and the core primitive we'd be working with was a Tile, we couldn't argue for keeping the Page abstraction. 
    - Moreover, we were considering making memory loads from DRAM page-based. We realized this would limit the amount of compute-memory overlap we could expose in HW through SW Scheduling optimizations. 
- Update: 
    - SW needs to simply tell HW how much data to load, and from where in the DRAM. 
    - No need of Page IDs and lookups near the Scratchpad. 
    - HW gets dumber, and SW gets more complex. This is a recurring theme in this project! 

## Progress
- Completed an onboarding presentation: https://drive.google.com/file/d/1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR/view?usp=sharing
- Prepared a detailed reading list for Scratchpad members. I've linked it [here](./assets/reading-list.md). Please take a look if you want to get an intuition of the "Why?" of this project. 
- Prepared a [overview](./assets/overview.md) of the Scratchpad.
- Ran students through [this](https://arxiv.org/abs/2110.03901) paper regarding implicit Convolution and the performance improvement it'd offer. Toe

## Future Plan
- Complete the Simulator for the TCA. 
- Complete the Scratchpad functional simulator. 
- Define the Interfaces + Modules in SV. 
- Discuss with Sooraj and Compiler team regarding the ISA. [#S0, #B1] are relevant Arch points.

