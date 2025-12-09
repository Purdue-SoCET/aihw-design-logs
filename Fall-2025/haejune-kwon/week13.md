# Week 13 Design Log

## State:
Currently not stuck with anything.

## Progress:
- Did VIP poster presenetation review presenation on Tuesday.
- Did Design review on Wednesday.
- Did further research on clos network and understood it deeply enough to start RTL coding.

## VIP poster presentation:
- Rafael, Julio, and I did the VIP poster presentation on Tuesday 10:30am with the topic of scratchpad.
- We made sure the poster included more diagram than words, and the words were in bullet points to minimize text.
- We explained frontend, backend, and crossbar of the scratchpad, with main focus on the need of scratchpad, swizzling, and crossbar.
- One difficulty faced during the presentation was that we were not sure of how much knowledge the judge/audience had. Therefore, we had some trouble choosing the right level of technical terms to use.
- We got a feedback that using the example of library and table situation to explain DRAM, SRAM, and swizzling was very helpful in understanding the funcionality and purpose of scratchpad.

## Design review 2:
- The main difference from the first design review is addition of numbers. This design review included synthesis numbers of frequency, area, and power for Benes, cabbage, and batcher network.
- This time, the presentation was much better, as the content was the same from last week, and I had the discussion with Akshath on multiple concepts: 
- Synthesis tool used was MITLL with Cadence Genus
- The optimal cycles were singlecycle for Benes and 3-5 cycles for Batcher
- The new possible solution discussed last week was Benes + ROM instead of cabbage. This means that all the combinations of control bits associated with each shift mask will be stored in a separate memory (ROM), and instead of running the heavy cabbage code, it will simply do a lookup. With this, one solution is simply using the entire 5x32 bits of shift mask to do the searching of ROM, and a better option is to use indexing method so that each combination of shift mask gets mapped to each index, which allows for smaller bits used to do searching on ROM.
- On top of Benes+ROM, I added clos network as the new possible design choice.
- I did not have much time to talk about the crossbar, because we were running out of time.

## Clos network:
- On top of last week's research on clos network, there are specific rules on how the IM-CM-OM connection is made.
- First, the input data-shift pair enters the IM in the same order without any rearranging.
- Then, IMs are connected to the CM depending on the destination OM. For example, if the destination for certain input is OM[0], then it should be placed in any CM with index 0. This happens by checking the IM[0][0] to the last index of final IM in order. If the input needs to go into index 0 but index 0 of CM[0] is filled already, then it is redirected to CM[1] index 0 and so on. Therefore, it needs to keep track of the data placements in CM to complete the CM wiring.
- Then, CM is connected to OM with pre-defined wiring, where all index 0 gets wired to OM[0], index 1 gets wired to OM[1], and so on.
- Lastly, smaller sorting happens within OMs and is connected to the output.

## Next Steps:
- Since I have understood the logic of Clos network, I will start building RTL next week, so that we can get synthesis numbers and possibly replace Benes or Batcher as a solution to the crossbar.

## Image:
- VIP_poster.jpeg