# Week 1
statement: I am not stuck.

## progress
I have decided to join the vector core team on the weekly meeting.

Reading the first chapter of the textbook and grab the basic idea of the GPU.

## learning and key concept

1. The initial focus of the GPU is fro real-time rendering, which emphasized on graphic display like video games. Today's GPU is focusing more on graphic accleration which do better job on non-graphic application.

2. Optimization focus: According to Dennard Scaling, we are getting harder to reduce transistor size in hardware to improve clock speed and reduce power. Now we need to work on the optimization partin hardware architecture.

3. GPU cannot takeover all the work from CPU, they have their own personal jobs. The CPU starts to initiate the computation to GPU which is acted like a controller. CPU is good at latency while GPU is excel in throughput. It means that CPU is better at serial task while GPU can take more parallel tast.  

4. Interaction of CPU and GPU. The first one is system with discrete GPU. The reason why they have individual memory is that CPU needs low latency, so the system memory is optimzied on low latency, which needs fast and quik reaction on dealing data. As for GPU, it needs high throughput, so it is more focused on the entire effect.
<div align="center">
<img width="200" height="300" alt="屏幕截图 2025-08-30 221308" src="https://github.com/user-attachments/assets/3c715cec-646e-4e51-b79f-df9b78023284" />
</div>

5. Interaction of CPU and GPU. The second one is integrated CPU and GPU. Since the cache(memory) is shared, there will be low latency for data accessing. When CPU has some data, GPU can immediately access it and use for computation. Also, since the distance is shorter, there will be less power consumed which makes it more efficient. However, since they share the same memory, GPU has to wait until CPU is done its work. Also, there might be cache-coherence problem since data is not private.
<div align="center">
<img width="200" height="393" alt="屏幕截图 2025-08-30 221304" src="https://github.com/user-attachments/assets/d7a9474d-dea2-437f-b8ff-e975e2343436" />
</div>

7. Thinking on preference of the 2 interation way. In my opinion, as for the most daily use like a smartphone, integrated method is preferred since it is more power efficient which saves bettery. However, when comes to gaming on pc, discrete method will be used more often since it can generate peak performance.    

8. Initial thought on kernel. A kernel is a special function that will be executed thousands times through GPU threads. The CPU initiate a kernel to GPU, and the SIMT inside the core execute the kernel.

9. Generic modern GPU architecture. Inside the GPU, there are many SIMT(single instruction multiple thread). And L1 cache and scratechpad memory is sitting inside it. The sractchpad memory is for sharing data between multiple singl SIMT core and the barrier opperation is for synchronizing time. The interconection network is like a high speed bus which is acted like a temperory storage. And the memory partition contains L2 cache, where connects to the off-chip DRAM.
<div align="center">
<img width="400" height="484" alt="屏幕截图 2025-08-30 230830" src="https://github.com/user-attachments/assets/a5327058-846a-4118-a405-2c714cdefeca" />
</div>

10. Realtionship on multi threads and the performance. It is a trade off of multi core (CPU) and multi threads (GPU). In the multicore(MC)area, since we have a small number of threads, the space for fast cache is available. In the valley area, due to lack of cache space, the memory is crowded which requires more time for response, leading to ineffectiveness. When comes to the multi thread(MT)area, the efficient use of the threads eliminate the latency(waiting time) due to the lack of cache space memory, where parallelism is working.
<div align="center">
<img width="400" height="344" alt="屏幕截图 2025-08-30 232126" src="https://github.com/user-attachments/assets/776538ea-a4da-45f0-8627-4033d04982a4" />
</div>

11.Thinking on existence of L2. According to the graph, we find that the high cost for 32 bit DRAM. Instead of frequently accessing DRAM, we can have a state where L1 inside the core can be more communicated with the memory partition(L2 cache), which saves power.
<div align="center">
<img width="400" height="257" alt="屏幕截图 2025-08-30 232722" src="https://github.com/user-attachments/assets/5435418a-d5e6-4ffd-8384-2039a2555096" />
</div>

## Questions
How do we solve the cache-coherence problem when using the integrated architecture?

## Plan
1. Continue on reading the textbook and self studying the material.
2. Start getting the preliminary insight to core vector that are implemented in the project. 




