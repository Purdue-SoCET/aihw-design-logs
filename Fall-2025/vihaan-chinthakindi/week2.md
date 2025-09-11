
State: I am not stuck with anything, don't need help right now. 

Progress:
 This week contained the first software subteam meeting. 
 In this meeting, we decided on some basic timelines:
    By This Sunday (9/6):
    - Be able to compile a custom instruction into binary
    - ```
        int main(){
            inline("
                theta x0, x1, x2
            ");
            cout << x0 << '\n';
        }
        ```
    In ~2 weeks
    - Support all custom instructions in our ISA
    In ~8 weeks, support implementations of stdlib.

Also discussed relevant memory accesses we can do (eg: to scratchpad).

Looked more deeply into PPCI, observing that to implement the custom ISA, we can simply create a member of the ISA class. Similar functionalities for custom architecture. For this immediate Sunday (9/7) meeting, Mikhail and Sahil are looking more into PPCI, while I will see the viability of using LLVM directly, which has a steep learning curve. 

Also attended session to get up to speed on 437 basics.
Discussed pipelining, Amdahl's Law, Cache basics, Out of order execution. 
