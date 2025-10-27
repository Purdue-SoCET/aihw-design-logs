# Week 9
## State: 
- I do not need help

## Progress: 
- Design review 1 finally completed
- Vector move instruction details flushed out
- Scalar to vector is not a common case, outside of already existing VS type instructions so we allow the move to be a pseudo instruction with add 0
- Vector team still unsure about movement details, need to meet to explain
- VLIW with no queue and 8 bits diagram completed: https://app.diagrams.net/#G1M_-irWdD2tf2M9vajaq4RTc4f5l0vSWu#%7B%22pageId%22%3A%22Il9e8COFQ9DecDX39woT%22%7D
- Reason for not having a queue is because it is unknown if that will be the common case so do not solve non-existent problems
- Certain moves allowed dictated in report
- BF16 to int and vice versa conversions

## Next Steps:
- Meet with Sooraj regarding changes
- Begin flushing out interfaces to and from other subteam/modules
- Review complete compiler document