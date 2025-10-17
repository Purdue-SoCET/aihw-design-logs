## State
I am not stuck with anything. Although I don't know how to generate coverage reports in Questa

## Progress (Week of Fall break)
* Continue the integration testing of the control unit from last week
* Add test cases to address mapper for coverage
* Further discussion on the non-blocking controller architecture

## Continue the integration testing of the control unit from last week
* Row conflict test case added

* Fixed row hit logic
    + row_hit was updated in the activate state, as soon as the activate command was sent
    + The desired update was when the row activation time is complete
    + Added condition to update the row_hit only when done activating the row i.e., tACT_done  = 1

* Added 3 tasks for looping 
    + do_row_miss
    + do_row_hit
    + do_row_conflict
    + The tasks go through all the state transitions for the command FSM for that operation and back to IDLE. The command FSM states and row status are checked at each transition
    + Only added looping for 1 row miss in each bank and passing

* ![](./images/week%208/wait_before_check.png)
    + Issue where the expected and actual value of row status looked same on the waveform but were different. The row status is combinational but probably still needed time to settle
    + Interestingly, happens only at the first check. Don't know the reason
    + Fixed by adding the small delay

* ![](./images/week%208/syntax_issue.png)
    + Issue where the expected and actual value of the row status were the same even when printed on the command line. However, the test showed fail
    + Spent 2 hours trying to fix, adding delays, check logic
    + Only to find out when I changed the checking logic to only print failed cases, I accidently added the failed error statement to the passed condition. LOL!

## Add test cases to address mapper for coverage
* For improved coverage, added looping with random addresses to check the correct output generated 
* Address is 32 bits. 2^32 simulation didn't make sense. Limited to 32'h00FF_FFFF
* Above test work only for x4 and x8. Cannot check x16 because BANK_GROUP_BITS is 1 (vs 2 in x4 and x8). It's parameter in the dram_pkg. Cannot change in the testbench. Plan is to have the controller working with 512 x8 config. So, skipping x16 for now
* I need to look at how to generate coverage report for questa

## Further discussion on the non-blocking controller architecture
* ![](./images/week%208/DDR4_controller-Non-Blocking-Bank-Queue.drawio.png)
* picture credits - Jason lyst, with updates by Tri Than
* Per bank queue has been finalized becuase easier to schdule request
* Bank queue before command fsm
    + Initially, command FSM was before bank_queue and bank queue would hold the commands from the command FSM
    + That meant we neede one more queue for storing commands before the command fsm becuase it needed to fully process the request (PRE -> ACT -> RD etc)
    + So, bank queue now moved before cfsm. It stores the actual request and per bank command state were anyways stored in the cfsm. No need for that additional queue
* Only need 1 CAM to search the head of each bank queue simultaneously for arbitration
* Possible sizes of the queues
    + Load/Store - 16 each because 4 masters each of size 4
    + Bank queue - worst case discussed was 32 if all the L/S are to the same bank. But we need average case not common case

## Future plan
* 565 exam next week so expect to focus more on that
1. Still complete the control unit integration to include timing control signals
2. This is a stretch goal. Figure out the coverage report generation for Questasim




