## Overview

Hi. I'm Akshath. I'm a 696 student this Fall '25, and I'm leading the Scratchpad team. My focus this semester is on the following topics: 
- Scratchpad Architecture
- DCache, ICache Finalization
- Scratchpad + DCache + ICache Verification (UVM + Functional)
- Crossbar RTL Design + IC Design + Layout
- AMP-Sim (for fun)

## Design Log Structure 

I've broken down my Design Logs into 3 major sections. Feel free to use my `template.md` file for your own logs. 

1. `State` mentions if I'm stalling on a true dependency from some other team's writeback. 
2. `Arch Updates` mentions all the arch changes we've made to the design. I've included changes to any interactions other team's might also have, for intuition sake. 
3. `Progress` highlights the links + references to committed work. 
4. `Future Plan` mentions the next steps I took the following week. 

## Resources

The following links mention repo-branches, drawio files and slides that I'd like others to refer to for questions. 

- Scratchpad
    - https://github.com/Purdue-SoCET/tensor-core/blob/scratchpad_main/
    - https://docs.google.com/presentation/d/1iEvYechSCiIgipsWWUsguGSQa5CKamQXyHnh3BL8s3I/edit?slide=id.g3840f9a64e0_0_1#slide=id.g3840f9a64e0_0_1 (Design Review #1)
    - https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#{%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22} 
- Split Transaction Caches
    - https://github.com/Purdue-SoCET/tensor-core/tree/memory_subsystem_lockupfreecache
    - https://drive.google.com/file/d/1em8aO1mWeDkecu1IMuqn2Jjr1YTbZ7w3/view?usp=sharing
    - https://docs.google.com/presentation/d/1AfC92lPhgahhlwJFHfiTvBNI8fM5cjCR75PEP1H8KZ4/edit?usp=sharing