Scratchpad is the Cache and place where we get, store, and move matrices around for our main computing power-houses: Vector Core and Systolic Array. It allows us to parallely load data from DRAM while running compute on the already loaded data. 

The core memory primitive of "SPAD" operations are tiles. Tiles are maximum 32x32, and minimum 1x1. The average tile size is expected to be 32x32, with the uncommon case of 5x5 tiles. 
    We're optimizing for Batched Inference, where we hit the compute wall before the memory wall. 
    SW Tiling guarantees high re-use and optimal tile live-range. 
    ML Engineers would be writing code for running NCHW-dim tensors on Atalla, where [N, H, W] > (n*32) 
    The above three reasons summarize why we set the HW-SW handshake of 32x32 max-tile-size. 

The Scratchpad itself is logically 2D, with parameterizable columns and rows. Num_Cols = Num_SRAM_Macros = 32, for us. Rows is always calculated once the SPAD_Size and Num_Cols is provided. 

Our Tensor Core enables higher throughput and an optimized way of performing GEMMs. We want to also do an interesting method of performing Convolutions. 
We are aware that Convolutions are not used in Transformer Architectures. However, Convolutions are still heavily used in a plethora of workloads that do not employ Transformers. We'd like Atalla to be used for them too. 

Previous approaches convert CONVolutions into GEMMs using Toeplitz Matrices, a way of storing data in DRAM for easy streaming and compute. However, there is minimal re-use for each unique data address, and a lot of duplication. 

Nvidia Tensor Cores and Google TPUs perform Implicit Convolutions. They do not create Toeplitz matrices in the DRAM, but perhaps in the Scratchpad itself. We do not know for sure, since they are proprietery methods. We want to develop an approach which can achieve a similar goal -- optimize tensor storage and movement, while maintaining high throughput in the Systolic Array. 

Main keywords for you all to know: 
- Row-major, Column-major
- Implicit CONV
- Swizzling
- Coalescing 
- SRAM Banks
- Crossbar Interconnects