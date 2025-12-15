
State: Not stuck on anything

# Progress
1) FURF poster
Updated vector top level and VRF RTL diagrams so it is presentable to absract signal names. Included cacti sweep for sub banks, VRF and top level explanations of what each unit does. Also included my synthesis information

2) Vector Design Review Slides

- updated VRF and top level slides. Below is the link to the presentation
https://docs.google.com/presentation/d/1BMwlAepy0YwaviwnN0ugEozvFR4OoLl9l5gX-_TGe2c/edit?usp=sharing

3) lane sequencer 

Making generic module for lane unit as each FU will have their own pipeline. As I wait for all the FUs to be complete I am starting to make a geenric module I can plug into each of the FU pipelines within the lane to simplify integration. This needs to handle 1 and 2 operand modules and handle meta data.

# Future Plans
- FURF presentation
- Design review presentation 
- Lane sequencer
