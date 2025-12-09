# Week 14 Design Log

## State:
Currently not stuck with anything.

## Progress:
- Completed Clos network
- Started on the final report: Every member on scratchpad was assigned to each part of the final report. I will be focusing on the crossbar, including the introduction and design choices of different networks. If the team needs more input, I will handle some part of results section, where all the synthesis numbers will be added.

## Clos network:
- I built the RTL for clos network as explained in the previous week's design log.
- There are 8 IMs, 4 CMs, and 8 OMs for default design. These numbers are parameterized along with size and data width, so different versions can be tested to find the optimal combination of the parameters used for clos network: C(n,k,m).
- As placements to CM needs to be done one after another to allow keeping track of previous placements, it had to be placed in always_comb block instead of generate.
- Extra variable was used to keep track of the next CM to be used based on the current placement.
- Another sub-module was used to do the OM-output sorting, using naive 4x4 crossbar that entirely uses muxes.
- Synthesis result was much better compared to Batcher for all versions.
- Clos compared to Benes fully pipelined has double of clock speed with less power, but it has double area. Compared to singlecycle, area and power is much worse while having about 4.7 times the speed.
- However, these comparison is done with the numbers without cabbage, so Sooraj agreed on using clos network as the optimal solution until Benes + ROM turns out to be much more efficient.

## Next Steps:
- Work on the scratchpad report, focusing on the crossbar section.
- Discuss with Akshath on the specific outline and structure of the report. Until then, I will start writing about the different networks used, so that it can be added to whichever part needed.