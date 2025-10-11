## NOTE: Content is a bit less because I was not aware of the Thursday alignment for design logs, after this one the schedule should be normalized to Thursday scheduling.

## State: I am not stuck with anything, don't need help right now.

## Progress
This week we have refined our ISA additions in the vector core meeting. We now will have one instruction for storing to systolic array (stsys.st) which can store either kernel or image (an immediate picks between the 2). As for shifting, we will not be using a Benes network due to the large latency, and due to it having more functionality then we need. We only need to shift right with a value of 0-31, meaning we will have a shift value of 5 bits as an immediate in the instruction (such as addi, addv). Current plan is to use a barrel shifter which uses a mux tree to achieve the shift amount. The critical path should be approximately a couple muxes. We then started work on the GSAU (global systolic array unit) RTL Diagram.

Diagram for GSAU: https://app.diagrams.net/#G1JW5Jguhs4vChq-sziK6ZME-tJgycms2J#%7B%22pageId%22%3A%22soUAP3OVNAC-PgTYQMAo%22%7D

ISA Additions (in the spreadsheet): https://docs.google.com/spreadsheets/d/1yDJ_oH0EXGIE4-4wVcwTeaw1Bg1vpoUSIkgTK3qDw_w/edit?gid=0#gid=0 

## Tasks
   We have a good draft for the GSAU at this point, we will get it checked by a GTA on Sunday and get started on coding. We have communicated with Vinay and made sure that out interface to the systolic array can work. We will also make the barrel shifter code. Our completion for both of the code for these units will likely be around 10/12, plus or minus a couple days (final deadline was 10/15). Lastly, we must also get a final check on our ISA additions by a GTA before we can certify they are complete.
   
## Notes
   We are using a couple valid/ready handshakes for data going between Scoreboard, GSAU, and Systolic Array. We chose this because of simplicity, our use case does not warrant the use of a larger area and more power hungry bus or standard protocol (i.e. APB, AHB, AXI, etc.). We have currently put in 24 bits of FF storage of our RD register. This is because Systolic Array can theoretically handle 3 operations at a time, however that may not be the common case.

## Future Plans 
   Once we are done with Diagramming and they have been checked off, we will move to code and verification of the two units we are assigned to as this point. After this we can help with other parts of the Vector Core or Systolic Array depending on the needs of both teams. 
