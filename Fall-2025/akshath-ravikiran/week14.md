> This week was focused on completing the Scratchpad Final Report. 

## State
[NONE]

## Arch Updates
[NONE]

## Progress
- Showed everyone how to use toggle and code covergae on QuestaSim. 
    > VLOG_FLAGS - ` -sv -compile_uselibs -cover bst -sv -pedanticerrors -lint -mfcu`
    > VSIM_FLAGS - ` -coverage -c -voptargs="+acc"`
- Please find our final report [here](https://docs.google.com/document/d/186o7OMmD8pstcT0LBeVNRixO5y7Undeff-K4Qaho2tY/edit?usp=sharing).
- I tried to synthesize the ROM on Flowkit, but I kept getting an `inferred memory unit` error during the optimization pas in `flow.yaml`. I intend to flush this out.
    > Note, this is technically useless, because the synthesis just gives FF numbers. 

## Future Plan
- Finish verification over winter!