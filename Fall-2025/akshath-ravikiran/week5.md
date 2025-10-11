> Since SW completely abstracts away the GEMM and CONV logic, we can set a constaint that the new vector load instructions will be handling 2 "streams" of mem.load/store to 2 seperate SPADs. This means, we can avoid this complicated muxing of 4:2 requests from the Frontend=>Grant-Logic<=Backend. 

## State

I am stuck on the XBar design for the Scratchpad. Note: This is not the shifting-network. Tags: Haejune, Duc, Sooraj. 
- Context: Currently, the only uncertain part of the design pertains to the crossbar. The math for Benes "topology" is well-defined, but the control-bit-logic is not. The most efficient implementation we've found is explained in the [Bernstein paper]().
    ![alt text](./assets/bernsteinlogic.png) 
- Update: 
- What's pending: 


## Arch Updates
Updated the RTL for the Design Review. 
![design_review](./assets/design-image.png)

## Progress
- [Design Review Presentation](https://docs.google.com/presentation/d/1iEvYechSCiIgipsWWUsguGSQa5CKamQXyHnh3BL8s3I/edit?usp=sharing) finalized with the Frontend-Backend-XBar subteams. 
- Python implementation of the Benes Network CBG from the Bernstein Controlbits paper: 
    ![controlbits](./assets/controlbits.png)

## Future Plan
