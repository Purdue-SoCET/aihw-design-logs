# Weekly Report – Week 2

##  Barriers / Concerns
No major barriers or concerns this week.   

---

## Highlights This Week
1. Logged into **Brightspace** and explored the **design materials related to AI Hardware**. Also logged into **GitHub** and initiated **design logs** to document daily technical progress and design thoughts.
   
2. Completed a detailed **overview of the architecture of AI Hardware**. Focused on the interaction between scheduler core, vectore core and the systolic array.
   Went through the following materials:
   
   High level Design changes this semester:
   
   https://drive.google.com/file/d/1JW5Jguhs4vChq-sziK6ZME-tJgycms2J/view
   https://drive.google.com/file/d/1unNIZAcid6fzkeXMgdsKzFMuHUBHNdTr/view?usp=sharing
   
   ISA ideas:
   https://github.com/Purdue-SoCET/tensor-core/blob/tensor_compute_accelerator_akshath/tmp/idea.md

   Vector ISA green card:
   https://docs.google.com/document/d/1rC2aKzQkUmv_Xsk0O_zc7xOVgJlFa1jRvBw9cpV9Gxs/edit?usp=sharing    
   

4. Attended a **scheduler core overview session** conducted by *Rishi*, which detailed the functional flow and interface design of the scheduler module. Participated in an in-depth **discussion on ISA modifications**, specifically related to **vector and scratchpad instructions**.  
   
5. Conducted a **self-overview of the previous RTL implementation**, revisiting older design files to gain familiarity with current module structures and coding conventions.
   From the github master branch:
   https://github.com/Purdue-SoCET/tensor-core/tree/master

---

## Next Week’s Tasks
1. **Obtain the updated vector ISA** specifications from the vector core team to align scheduler and datapath interface logic accordingly.
2. **Begin designing the microarchitecture of the scheduler interface**, focusing on communication between the scheduler, vector datapath, vector register file, and scratchpad.  

---

**Status:** On Track ✅  
**Prepared**
