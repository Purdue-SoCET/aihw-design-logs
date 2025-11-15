## Project Update

### State: I am not currently stuck or blocked.

### Progress
1. Testbenching has been mostly completed. Since it is using my simulated dram/sram tasks, it is possible that when backend is dropped into the system some function may be off. The simulated world and my thoughts of how scheduler and dram/sram work could be slightly off from the final versions. However, the way things currently are the backend has survived testing. 

2. With testbenching done it was time to clean up the code. To begin the interfaces were moved into scpad_if and some new packages/parameters were added to scpad_pck/scpad_parameters. Additionally, long determenistic if statements were shorterned. For example, to calculate the num_request we can use the top 3 bits of num_cols instead of using a bunch of less thans and manually setting the number. In a similar manner the long if statements for dram_wdata and sram_wdata, the data used to build our potentially 512 bit request, was shorterned.

3. Synthesizing the backend has also begun. Currently most of the files were set up. Once the script is fully complete synthesizing will be made available. 

4. Work on the poster for the upcoming Fall Undergraduate Research Expo has begun. Currently the skeleton is set up and the main sections are defined.

5. Updated the Backend diagrams to match the current synthesizable version.

6. Presented the updated backend during the Tuesday design review presentations.

### Next Steps
1. The most important next step is to finish the poster. During the Sunday meeting the team will come together and finalize/get it printed.

2. Finish the synthesizing script for backend then get the area and clk numbers to add to the excel sheet.

3. The backend can be optimized/cleaned up further, one obvious optimization is to get rid of multiplication as explained in week10, however this task will have to wait for after the poster session. 

