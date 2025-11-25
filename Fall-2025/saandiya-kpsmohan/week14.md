## State
I am not stuck.

## Notes
1. These are some useful papers from Jing to be referenced in the final report:
- Saw this im2col hardware unit (figure 1). Potential reference for the future. https://arxiv.org/pdf/2107.13386
- Future utilization graph we want to pursue (figure 2). Will be a different graph since we're kinda fixed with weight stationary https://arxiv.org/pdf/1809.04070
- Some common CNN models are MobilenetV2, Alexnet, Yolo, Resnet50.

2. Column major vs row major
- We are doing row major order (loading rows from scpad) because it requires 1 shift and 1 add for a normal instruction where as column major requires 3 shifts and 3 adds. Refer to the figure below:
![IMG_9300](https://github.com/user-attachments/assets/0a6479e0-f303-42f3-91b8-bd98cde614b6)

3. Output shape of systolic array
- The output shape of the systolic array would be NHWC and AFTER transposing (which is loading an output column as the first output row) the shape becomes NCHW which is what we want.


## Progress
I have done the golden model + CPU runnable code. Everything is verified.
It currently works with variable input size (nxn), variable input channels, variable kernel size, variable stride, variable padding and no dilation.  
I have run the code over with Jing on 11/23 (Sunday) and everything looks good.
I have also written the Atalla code that is equivalent to the C code.
- The folder everything is in: https://github.com/Purdue-SoCET/atalla/tree/tensor_compute_accelerator_saandiya/conv_prog_model
- main file: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/main.c
- conv_lib.c: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/conv_lib.c
- atalla_conv.c: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/conv_prog_model/atalla_conv.c

## Future Plans
1. Kernel optimization in C
<img width="1798" height="890" alt="image" src="https://github.com/user-attachments/assets/c83084ad-c769-48d5-bed2-b052f5cb6ac9" />

2. Calculate PE utilization % - simple addition
3. Optimize C code for dilation
