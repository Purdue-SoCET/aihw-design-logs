I am slightly stuck. I am having difficulites getting the reduction tree to build in the new file structure. This is making it hard to finish it up, however im carefully looking over what i did with sqrt and hopefully should be able to fix it.

Progress:
I somehow managed to break my flowkit, but after a few days i was able to get it to synthesise things again. 
BF16 sqrt unit completed and handed off to joseph.
Actually had a discussion with jing about limiting the reduction tree, and he thinks its a good trade off. However, another potential future optimization came up, if the workload study finds that reductions are not really used, then we could go to the non pipelined version that only requires elements/4 ALUs. again, this saves even more area, but at a cost of performance. As stated in the stuck statement, im having trouble building the reduction due to file structure. However, all it needs left is a basic counter to only assert the ready signal after so many cycles. I have every module brought in up to data, addedd parameters, and theortically implamented the rate limiting, but its not seeing files and i cannot test it.


Going Forward:
Fix the build system
Finish the reduction tree fully
Begin woking with joseph on a top level vector core testbench. I need to discuss with him, how complex we want to simulate it, if we want to do CPP, and what parts of the bench i should focus on.