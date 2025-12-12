## State: 
  I am not currently stuck on anything

## Progress:
  -This week we finished out final report
  -we redid all of out diagrams to be clean and readable
  -polished the transitions
  -added a history section describing the changes throughout the semester
  -added a contributions section
  -added a conclusion
  -added the emulator section describing the emulator
  
  -Found a way to finish the emulator using the SCPAD script that already exists
  -any time we write to or read from the scpad we need to use a tile id corresponding to the address
  -this tile id will be saved in a dictionary with the address beign the key and the tile id being the data
  -there will be a global tileID counter to ensure we dont reuse tileIDs on accident.
    -this will have to be a long int
  -when we want to use an address inthe scpad we will:
    -first check the dictionary to see if there is a tileID corresponding to the address
      -if there is then we will use that tile id with the address
    -if there is not we will use the global counter as a new tile id
    -we will store the pair to the dictionary
    -we will use increment the global counter
    -then we will use that pair to access memory
  -this sequence ensures there will not be any reuse of tileIDs when ther shouldnt be
  -it alsoensures we can access the same address in the scpad multiple times

  -all evidence for this week has been turned into brightspace and is on the share point
  -the emulator progress is in the github under the emulator branch


## Next Steps:
  -finish the emulator
  -test the emulator