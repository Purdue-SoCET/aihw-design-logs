## State
I am not stuck

## Progress
1. During the Vector Meeting (12/3 Wednesday), I updated Jing with my updates and he asked me to do more analysis.
![IMG_9475](https://github.com/user-attachments/assets/c0b90c1e-7241-4fcb-a93e-cf9fa9b6b733)

In this picture there are 3 analysis to be wanted:
- Peak PE utilization
- Average PE utilization
- Ramp up/down, peak over time graph
- Heat map for PE utilization.

2. I also met with Akshath on (12/3 Wednesday), to go over the convolution programming model. He told me everything looks good.
3. I have also started working on the final report: https://docs.google.com/document/d/1pqSLC1YI7B6YlvKNO94d3csJGDTimtug0PLxJEcokzw/edit?usp=sharing
4. Rubric for the report: https://docs.google.com/document/d/1p9lezyefTYR5caKoAygwH0ZKMxU3SrSYBtS8NePAORg/edit?usp=sharing

## Evidence of Progress
1. PE Peak utilization, average utilization calculation
![Screenshot_2025-12-03_at_1 02 38_PM](https://github.com/user-attachments/assets/a51cf4b8-9624-4238-8510-b102c9127297)

2. Heat map
<img width="1000" height="800" alt="pe_heatmap" src="https://github.com/user-attachments/assets/d0a59b4a-990d-4f82-8983-43f17719ac61" />

3. Ramp up/down over time (zoomed in)
<img width="1500" height="600" alt="utilization_ramp" src="https://github.com/user-attachments/assets/cc82a2ce-7e39-46ff-8d29-2cf0a74689ee" />

## Analysis
- Although channel stacking successfully maximized the vertical efficiency of each active column (packing 27 weights into the 32-slot depth for ~84% utilization per PE), the overall array utilization remained low (~8%) because the workload was horizontally sparse. By configuring the test with only 3 Output Channels (Cout=3) on a hardware array designed with 32 physical columns, 29 columns (90% of the array's width) remained completely idle during computation. The total system efficiency is the product of these two factors—high vertical density (0.84) multiplied by low horizontal occupancy (3/32≈0.09)—resulting in a final utilization of approximately 7.8%, confirming that the architecture requires sufficient output channel parallelism (Cout≥32) to realize its full performance potential.
- If the utilization plotting is expanded well, it can be used to plot for different systolic array architecture. The slope is now a constant, but if we do adder tree instead of our current implementation, the slope can look steeper and less ramp up/down time
  
## Future Plans
1. Continue working and finishing the report by 12/9 for Malcolm to review.
2. Wrap up programming model.
