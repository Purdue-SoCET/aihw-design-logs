State: I am not stuck with anything, don't need help right now. 

## Progress

- Attended Computer Architecture Fundamentals focus group
- Attended compiler group meeting
- Code traced frontend from parser to abstract syntax tree
- Created a custom "theta" function in the frontend and successfully generated the IR
- Successfully printed out the IR and machine code for pre-installed functions
- I will be working on the backend and possibly contribute to creating the ISA for the tensor core

# Meeting Notes
- Added support for parsing “theta” by adding “theta” to self.keywords in the parser. Then added parser for theta to parse_primary_expression().
- Added an on_theta function into semantics
- Changed how theta is parsed to take 2 arguments instead of 1
- Used parse_expression instead of directly consuming arguments 
- Understand self.consume (currently erroring when consuming comma, presumably because it does not see a comma there, so need some while loop structure)
- Understand how AST is being traversed
- Ask expert about adding meaning to theta and traversing AST
