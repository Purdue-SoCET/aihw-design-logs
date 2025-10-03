Status: I am not stuck

## Progress

- Presented design review
- Fixed BR instructions & completed J type instructions https://github.com/Purdue-SoCET/aihw-ppci-compiler/commit/04d24b5e83341373a5e56310009a949d620303c7 
- Added all isntructions to ISA via @isa.pattern abstract method https://github.com/Purdue-SoCET/aihw-ppci-compiler/commit/1c29f9955b0edf72dcda9d952c50670f7a880261 
- Scalar instructions do not support floating points, so removed fp from parser to return a compiler error upon the user trying to instantiate a float or double type variable
- Continued to flesh out arch.py, most functions implemented https://github.com/Purdue-SoCET/aihw-ppci-compiler/commit/3be5df90326a52d319b27c3e9befa4ae1aa45f2f 
- Debugged architecture, successfully parsing most of the sample file but still a few errors upon jump due to mismatching ISA part names (i.e imm vs imm12 vs offset)

## Next steps
- Continue debugging scalar ISA to hopefully successfully compile by the end of sunday meeting
- Do the next steps from last week


