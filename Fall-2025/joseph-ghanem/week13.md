State: Not stuck on anything

# Progress
1) Presentations
- presented both in FURF and for my design review

2) Lane Sequencer RTL
- Finalized the rtl and began verifying the design with the sqrt module as it is the only finalized module. Below is the test plan I made and am passing each one:y

* **Scenario A (Happy Path):** Verifies the fundamental functionality of deserializing a vector slice into individual elements with correct data and control signals.
* **Scenario B (Downstream Backpressure):** Tests the DUT's ability to pause execution and hold data stable when the downstream module asserts a not-ready signal.
* **Scenario C (Upstream Starvation):** Ensures the module correctly returns to an idle state and clears valid signals when the input queue runs empty.
* **Scenario D (Back-to-Back Throughput):** Verifies the handling of consecutive vector instructions and checks for the expected latency bubbles between slices.
* **Scenario E (Asynchronous Reset):** Confirms that the module immediately halts operations and resets internal counters if a hard reset occurs during the busy state.
* **Scenario F (Mask Bit Toggling):** Validates that vector mask bits are correctly serialized and matched to their corresponding data elements using a specific bit pattern.

# Future Plans
- Top level integration plan
- lane unit integration plan