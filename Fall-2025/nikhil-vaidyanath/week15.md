## State: I am not stuck with anything, don't need help right now.

## Progress
   This is a short week since it's just following Thanksgiving.

   My main goal this week is to complete my shifting unit's verification. I was not getting the results I expected out of Akshath's Benes module so I have messaged him with a couple questions on expected inputs and outputs.

   The xbar_if defines a "group_t" struct which has din and shift. This is odd because the shift is already given by the control bits. After much testing, I noticed if I simply set the struct equal to the actual input (which leaves the top 5 bits as do not care) then I get the output I expect. I'm not sure if he intended this function so I will follow up with Scratchpad. I also noticed that the enable signal within the xbar_if is not connected at all and will ask them to check that.

   I eventually trouble shooted my issues and got the shifting unit to show the results I expect. On 12/3 I attended the Vector Core meeting where I asked how I should synthesize the module, given it's completely combinational and my numbers weren't going to be representative from a timing perspective. I was told to synthesize with and without latches on input and output, because Vector Core has not decided the latch mechanism for unit to unit communication.

   Note: Code has not gotten pushed yet but will be once the check off is gotten (which 100% will get done before the semester ends)

## Tasks
    Next steps include:
     Finish verification of shifting unit (with Jing's checkoff)
     Work on final report, detailing GSAU and especially the logic for our decisions and transition away from the TCA
    Deadlines:
     Final Report - 12/19 @ 5 PM

## Future Plans
   Looking more towards the end of the semester, the report is going to be the most important thing. I will try to get my unit fully done and checked off whenever I have time, then dedicate the rest of my time towards putting all of my thinking and design decisions this semester into the report.