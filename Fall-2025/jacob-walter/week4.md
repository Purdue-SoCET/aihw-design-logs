I am currently not stuck on anything

Main Socet Meetin Notes:
Presentation on MRAM was very interesting, but a lot of it went over my head. Presentation makes a good template for how to make really good slides for a presentation.

Time Spent: 6 hours + whatever i work today

Progress:
Continued work on reduction FU, hopefully ready for testing right after i am done writing this. Need to abstract it a little more a make the ALU block seperate of the main unit. Was a terrible idea attempting this and i wasted a lot of time with that. To talk on square root, newton-rapson is way to slow, looking at like 50 cycles. Two new methods have been found, quakes fast invers square root and linear piecewise approximation. After research on their accuracy, I have decided to do linear approximation. A python simulation needs to be written to verify that firstly the method works, and secondly it actually produces values with a worst case of 8-9 bits of accuracy.