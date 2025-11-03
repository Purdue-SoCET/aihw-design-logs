# W2 Design Log - Adrian Buczkowski

## State: 
I am currently in the process of getting familiarized with the background information about the DRAM controller project. I have been informed about the basic state of the project and outstanding issues. I plan to make it through readings given to me by Dhruv and Tri. After the readings are complete, I will verify the timing constraints that Tri and Dhruv have calculated. I may also potentially help Tri debug the current issues with the controller.

## Progress: 
This week I read a lot of background material related to DRAM organization and control. While I am familiar with basic DRAM concepts, it is a deep subject with a lot of confusing terminology. I have become much more familiar with common terms and prtocols used in DRAM interfaces. This has helped me to understand the project state and the nature of the problems we are facing.

The primary resource I have read throught is the book Memory Systems: Cache, Dram, and Disk. Chapters 10-13 are related to DRAM operation and memory controllers. I read chapters 10 and 11 which cover DRAM memory system organization and basic DRAM access protocol.

The link to these chapters is here.
https://www.sciencedirect.com/science/article/pii/B9780123797513500126

This book along with the JEDEC standard is what I have been looking voer to get started with the project.

## Concepts Covered:
- Address decode and R/W transaction flow
- Difference between channel, rank, bank, row, column
- Physical constraints that cause variety in access delay
- Protocol and timings for DRAM access