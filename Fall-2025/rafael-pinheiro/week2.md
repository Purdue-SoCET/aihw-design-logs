```markdown

**State:**  
I am not stuck with anything, don't need help right now.  

---

## Progress

- **Attended Jing’s Focus Group**
  - Reviewed what Sooraj told us to read about: pipelining and caching

- **Attended Scratchpad Onboarding Meeting**
  - I’ll be working on the **Scratchpad frontend** to the **Systolic Array**.  
    - This involves getting data from the Scratchpad memory and sending it to the Systolic Arrays
    - The Systolic Arrays will perform **GEMMs (General Matrix Multiplications)** and **convolutions** using Scratchpad data

---

## Topics from the Onboarding Meeting

### CPU and Memory Interaction
- The CPU modifies data, but on-chip **SRAM** is temporary - it’s not persistent
- Data must eventually be **written back to DRAM**
- This introduces several complications:
  - Many-core systems
  - Out-of-order execution
  - Memory-mapped I/O (MMIO)
- For simplicity, assume a **single-core**, **in-order** system

---

### Cache Concepts Review

When writing new data to memory:
1. **Write-Through Policy**
   - Every cache edit immediately updates main memory (asynchronous)
   - **Low performance**
2. **Write-Back Policy**
   - Main memory updated only when the cache line is replaced
   - **Higher performance**

**Write Buffers** are used to alleviate backpressure from these operations.

> **Key Point:**  
> Data caches (**DCache**) are hardware managed, not software controlled.  
> Cache decisions occur **every cycle**, automatically in hardware.  
> Many bits in the SRAM are lost to *tags* and *metadata* for coherence tracking.

---

### Why Scratchpads Are Different

Scratchpads are **not like DCaches**.

- DCaches are designed for **general-purpose CPU workloads**, where:
  - Data is accessed at **word-level granularity**
  - Often, only a subset of data bits are used per instruction
  - These caches fit into the **CPU pipeline** model

However, our work is **not CPU-style** compute

---

### Domain-Specific Memory: Scratchpads in Accelerators

Scratchpads are used in **Tensor Cores (NVIDIA GPUs)** and **TPUs (Google)**
They serve as **high-bandwidth, software-controlled caches** optimized for domain-specific workloads

- **Programmers work with Tensors**, but systems frameworks abstract them into **matrices** and **vectors**
- **Why abstraction?**
  - Tensors are massive (e.g., \( N \times M \times K \))
  - Chips have limited SRAM and extremely fast cycle times (sub-nanosecond)
  - We need multi-layer abstractions to manage compute and memory efficiently

---

### Divide and Conquer Strategy

- Break large **tensors** into smaller **2D matrices**
- Break matrices into **tiles** (e.g., 32×32)
- Perform compute on each tile and combine results later

This approach simplifies work while maximizing throughput for our specialized architecture. 
We are **not** building a general-purpose throughput machine — our design is **domain-specific** and **compute-focused**

---

### Architectural Insights

- The **Scratchpad** acts as the **data cache** for the **Systolic Array** and **Vector Core Units**
- There will still be a **DCache**, but it’s reserved for the **Scheduler** and CPU-type work
- **Scratchpad Characteristics:**
  - **Software-controlled**
  - No tag bits, valid bits, or automatic indexing
  - SW handles memory management (similar to OS paging)
  - Allows transparency and programmability

**Why this matters:**  
- Tag bits waste valuable SRAM space.
- We want **software-defined control** for flexibility in specialized workloads
- The hardware architecture must always consider **software programmability**

---

## Next Steps

- Read the links Akshath shared about **Swizzling**, **GEMMs**, and **Convolutions**
- Experiment with the **Convolution Simulator**
- Reverse engineer the **Swizzling algorithm**

---

## Reference Links

- [Matrix Transpose in CUTLASS (Colfax Research)](https://research.colfax-intl.com/tutorial-matrix-transpose-in-cutlass/)  
- [Why GEMM is at the Heart of Deep Learning (Part 1)](https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/)  
- [Why GEMM is at the Heart of Deep Learning (Part 2)](https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/)

---

*Keep in mind:*  
We’ll be presented with the **ISA for Scratchpad control** soon
For now, focus on understanding the **hardware decisions** behind it


Next steps:
    - Read links Akshath sent us about Swizzling (crucial!), GEMMs, convolutions
    - Play around with the convolution simulator
    - Reverse engineer the algorithm for swizzling

```markdown