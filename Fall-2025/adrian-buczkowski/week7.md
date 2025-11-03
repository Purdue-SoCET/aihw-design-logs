# W7 Design Log - Adrian Buczkowski

## State: 
We have a high level diagram done for the memory controller. We are trying to hash out some smaller details after discussion with Sooraj, but we know the general shape of our design.

## Progress: 
This week the team came up with two different possible architectures for the controller. One with a load queue and store queue for all transactions. And one with a load-store queue for each bank of the DRAM. After our Thursday discussion, we realize we will have to combine these two approaches for the best results. I personally made the high level diagram for the first implementation discussed. It is linked here:

https://app.diagrams.net/#G18bqekF9I8oZJpSTm-BcsDvPkOPy_cdul#%7B%22pageId%22%3A%22kH9zeyrYaGyILM6MkzEw%22%7D

Our other initial idea should be accessible on a different page of the same link. After further thought, I realize that the per-bank queue system is a way better idea that the giant load store queue. Tracking transactions per bank will allow us to easily isolate independent transactions and pipeline them. Current coencerns about this implementation are as follows:

- How much CAM and how many CAM ports will we need for the queues? If the queues are strictly FIFO this isn't a big deal. Also, since the queues will not be very big we could turn it into a table implementation.
- We will need to replicate timers and FSMs for each command in flight.

