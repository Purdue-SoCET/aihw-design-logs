State: Need to talk to team leads regarding RTL changes

# Progress
1) ISA finalized on Italla sheet with speudo code, instr types, and opcodes
<img width="881" height="475" alt="Screenshot 2025-10-10 215329" src="https://github.com/user-attachments/assets/93590d08-fc68-44e6-b299-f67825d8274b" />

2) Redesign of vector top level

Did research on other vector core implementations 

Ara: A 1 GHz+ Scalable and Energy-Efficient RISC-V Vector Processor: https://arxiv.org/abs/1906.00478 
New Ara for Vector Computing: An Open Source Highly Efficient RISC-V V 1.0 Vector Processor Design: https://arxiv.org/pdf/2210.08882 
Ara2: Exploring Single- and Multi-Core Vector Processing With an Efficient RVV 1.0: https://arxiv.org/pdf/2210.08882 
The Hwacha Vector-Fetch Architecture” / Hwacha Microarchitecture Manual: https://people.eecs.berkeley.edu/~krste/papers/EECS-2016-117.pdf 

Understanding how these papers implemented their vector architectures led to me thinking how to best utilize PPA tradeoffs into our vector design. Below are the design choices these papers made me seriously reconsider:
# Design Choices

## Lane Count
- **Decision:** Start with **8 lanes**; keep the lane count **parameterizable**.
- **Rationale:** The **systolic array** is the primary high-throughput unit; lanes provide general SIMD throughput.

## Vector Register File (VRF) Slicing
- **Approach:** **Per-lane slicing**, similar to **Ara**.

## Mask / Predication Model
- **Dedicated mask register:** `v0`
- **Width/Capacity:** 16 bits → up to **16 masks** addressable
- **Selection:** Immediate value indexes the active mask
- **Data path:** `v0` feeds the **MaskU**, which fans out a **1-bit VM enable** to each lane
- **No-mask behavior:** All lanes see `vm = 1`
- **Note:** Stride-based **shuffle/reshuffle** logic likely required for flexible masking patterns

## Element Width Flexibility
- **Now:** `fp16`
- **Future:** plan for `int8` (keep datapaths/VRF parameterizable)

## Mask Port Pressure
- **Special case:** `v0` has a direct, wide read path into **MaskU** to reduce R/W port contention.

## Reduction & Cross-Lane Operations
- **Plan:** Keep **separate** from per-lane VALU for simplicity (matches current implementation direction).

## Vector Load/Store (VLS)
- **Placement:** Outside the lane; **loads are fanned into lanes**.
- **Open question:** Can limited compute be performed directly on the load/store path?

## Variable Element Length (VL)
- **Controller:** A vector controller performs **strip-mining**—splitting long vectors into iterations that fit the physical lanes.
- **MaskU role:** Supplies zeros or performs merges as needed per iteration.

## Tail Policy (when `VL < VLMAX`)
**Options**
1. **Tail-agnostic:** Inactive elements are **don’t care**.
2. **Tail-undisturbed:** Preserve old values (requires **read → merge → writeback** to avoid overwriting elements the program may later read).

**Choice:** **Tail-agnostic**.
