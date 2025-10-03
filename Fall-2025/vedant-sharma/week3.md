Design Log Week 3:

I am not stuck at this point of time.

-----------------------------------------------------------------
Progress:

I've learned that I will be working to help with implementation and simulation of the exponential functional unit. This week was essentially my week wwhere I figure out what units I'm helping with and getting ready to start writing testbenches for. So far what Jing has recommended is I work on the exp() unit and then shift to either the reduction or smth. My goal is to verify through python simulation that our design approach works, then implement a simple testbench to see if it can run and compile once its done, then work on testing edge cases or simply move on to creating tb's for the reduction unit to see if that can run and compile once its done.

In order to correctly simulate and verify that the approach for the design we are taking works I've been working on a python simulation with the method of the functional unit, the golden model based off pytorch's exp() function, and then randomly generated 16 bit binary inputs. Our approach for the method as I understand it is to split the e^x term via a LUT for the closest integer value and then have the remainder of the exponent 'r', be calculated through a taylor approximation. Based off the RTL diagram we are using a cubic taylor approximation and a LUT with values for 2^-15 to 2^16. 

equation as I understand it:    e^x = 2^(x/ln2)
                                y = (x/ln2)
                                y = q + r (q is integer, r is small fractional portion)
                                e^x = 2^q * 2^r
                                2^q is in LUT, 2^r is calculated through Taylor approx.

Quick thing to note: I still have not been able to get access into BRS even though I talked to Boyuan and resolved the issue on UniTime. Will have to message again perhaps in order to get access to asicfab for verification.

Future Plans: 
Now that I know what functional unit I'm working on along with the approach being taken with the design my future plan is to actually implement the python simulation. Basically write a python file and created a csv with 10,000 generated cases, then create a column for the relative error between the two models, golden and functional_unit. If the error is minimal then I simply can reflect that and proceed with the testbench if not then we may have to change the design approach we are currently using. I need working python results by Wednesday.