## Overview

Hi. I'm Akshath. I'm a 696 student this Fall '25, and I'm leading the Scratchpad team. My focus this semester is on the following topics: 
- Scratchpad Architecture
- DCache, ICache Finalization
- Scratchpad + DCache + ICache Verification
- Crossbar Micro-Arch
- AMP-Sim (for fun)

## Design Log Structure 

I've broken down my Design Logs into 4 major sections. Feel free to use my [`template.md`](./template.md) file for your own logs. 

1. `State` mentions if I'm stalling on a dependency from some other team. 
```verilog
typedef enum string { "NONE", "STALLED", "STALLING" } state; 
```
2. `Arch Updates` mentions all the arch changes we've made to the design.
3. `Progress` highlights the links + references to committed work. 
4. `Future Plan` mentions the next steps I took the following week. 

Each `Arch Update` point gets mapped to a specific ID. This helps us track how many iterations we've gone through, and which one we're on right now. 
```python
#T -> Top-Level Interfaces | Latest: T3
#F -> Frontend | Latest: F2
#B -> Backend | Latest: B3
#C -> Crossbar | Latest: C3
#S -> SW/ISA | Latest: S2
```

## Resources

The following links mention repo-branches, drawio files and slides that I'd like others to refer to for questions. 

- General Onboarding Presentation: https://drive.google.com/file/d/1yjtGIwYba1tQ_oEZ2nP-iKsl-h5MZtOR/view?usp=sharing
- [Overview.MD](./overview.md) lists a good summary of the Scratchpad.
- Scratchpad
    - https://github.com/Purdue-SoCET/tensor-core/blob/scratchpad_main/
    - https://docs.google.com/presentation/d/1iEvYechSCiIgipsWWUsguGSQa5CKamQXyHnh3BL8s3I/edit?slide=id.g3840f9a64e0_0_1#slide=id.g3840f9a64e0_0_1 (Design Review #1)
    - https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#{%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22} (Diagrams)
    - https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?gid=0#gid=0 (ISA)
- Split Transaction Caches
    - https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_lockupfreecache
    - https://drive.google.com/file/d/1em8aO1mWeDkecu1IMuqn2Jjr1YTbZ7w3/view?usp=sharing 
    - https://docs.google.com/presentation/d/1AfC92lPhgahhlwJFHfiTvBNI8fM5cjCR75PEP1H8KZ4/edit?usp=sharing (Design Review)
- Reading Lists - I've compiled some sources/papers that the team has gone through. I believe they will be good starting points for context about this project. 
    - [General Reading List](./assets/reading-list.md) 
    - [Crossbar Reading List](./assets/crossbar-reading-list.md) 
    - ["Async"-Memory Reading List](./assets/async-mem-access-reading-list.md) 