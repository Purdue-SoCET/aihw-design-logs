Design Log Week 5:

I am not stuck at this point of time.

-----------------------------------------------------------------
Progress:

Discussed with GTA about the issues with the LUT if change to base e^x, LUT will be too large, e^x can only go up to e^11 as fp16 has a max value and e^12 will go above said value, and we are already trying to conserve area by swapping to a Lane based approach for the vector core, meaning that this e^x approach may not be as viable as we once thought. To top it off we also have an issue with the Taylor approx as the continual subtraction will add more cycles as the base point of approximation will need to be included.

New thought approach is to swap back to our base 2 approach, however, we can decrease LUT size and make the negative inputs stable by calculating the positive value instead and then dividing by it. Obviously this means that at least 50% of the time you are adding a divider into the mix meaning more cycles to output however we beleive that the tradeoff is worth it as we save LUT space as well.

Link to catastrophic cancellation paper (taylor expansion on exponential):
[text](https://courses.grainger.illinois.edu/cs357/su2013/lectures/lecture02.pdf)

Read up on for various approaches and ULP precision of the different approaches:
[text](https://arxiv.org/pdf/2112.02263)

(Issues detected, LUT's are extremely large and precise and there are 2 LUT's being introduced for the methods. We cannot consider this feasible if we directly implement the approaches in this article but its still good to know the precision)

My current plan is to simply implement the smaller LUT and then have a flag to check if the MSB is 0 or 1 for sign. Then calculate via the same approach described as above based off that conditional. So far have tested it on 5000 random cases and getting little to no error. Need to check incrementally across minimum fp16 incremented all the way through maximum fp16 value and then plot as x-axis then plot % error along y-axis to observe and determine if the approach is stable and viable. 

Quick thing to note: Finally got the ball rolling along for the asicfab along with the BRS, emailed councilor for the BRS and got a responseand Boyuan is working with IT to get me access to asicfab. Should be able to start and hopefully finish .sv testbench for exp() or division by the end of this month.

Future Plans:

Finish the design presentation and finalize approach after simulation is working.
Start working towards the .sv testbenches as the functional unit need to be able to run and compile by the end of September. 