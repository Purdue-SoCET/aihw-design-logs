# Week 4
## State: 
I dont't need help with anything

## Progress: 
- Project was overhauled to simplify scheduler architecture to match scheduling for GPU team
- Most out of order execution pushed to compiler team 
- Project still needs ISA changes to be implemented, register changes to variable size matrix operations, branch and jump handling for new packetized instructions
- Scoreboarding is no longer necessary, still have issue queue but will no longer have any register/data dependencies
- Simplifies project since existing register status tables (RST's) are now obsolete since compiler guarantees non dependent instructions
- Functional unit status tables still necessary and can still be executed out of order to increase functional unit utilization
- Issue queue will remain along with age logic, and hazard detection
- This week we presented our hastily revised project pitch to the team leads and professor Johnson
- Tentatively responsible for branch and jump handlinjg but subject to change due to recency of project change
- Will continue understanding new ISA with given ISA card

## Next Steps:
- Redo diagramming accounting for new changes to the ISA via packetized instructions