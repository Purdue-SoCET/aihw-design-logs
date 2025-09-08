State: I am not stuck with anything, don't need help right now. 

## Progress

- Attended Computer Architecture Fundamentals focus group, and ISA Discussion meeting
 - Established design plan
    - By end of this week, implement a prototype compiler for a simple custom ISA consisting of 1 dummy instruction (theta)
    - By week 2 implement full custom ISA support
    - By week 4, refine custom ISA
    - By week 8, develop standard library
- Need to decide whether to use PPCI or LLVM to implement the compiler backend. Leaning towards PPCI for simplicity, but lack of community support and documentation is an issue
- Compiler needs to track datatypes like vectors, registers, etc

## Notes

ISA Meeting: 

- Team is implementing a new 32 bit ISA
- My compiler project should work to translate code into this new ISA
- Vector core ISA
    - Load_v, Store_v, Loadm_v, Storem_v
    - Mul, div
    - Add, sub
    - Reduce_add, reduce_min, reduce_max
    - Bit_and, bit_or, bit_xor, bit_not
    - Masking - gt, lt, eq, neq
    - Downshift, upshift
    - exp, sqrt, inv_sqrt
- Look into ppci, llvm for creating custom compiler

Focus Group:

- Iron Law: Processor Performance = Time/Program = Instructions/Program (Code Size) * Cycles/Intstruction (CPI) * Time/Cycle (Cycle Time)
- Architecture (Compiler Designer) --> Implementation (Processor Designer) --> Realization (Chip Designer)
- Amdahl's Law: Speedup = Performance after enhancements/Performance without enhancements
    - Speedup = $\frac{1}{(1-time_o) +\frac{time_o}{speedup_o}}$
- 5 stage pipelining of single cycle


Software Meeting:


- Need Custom Intructions for out ISA 
- C to Assembly
- gemm x0, x1, x2
- Have this done ASAP, then expand to full ISA within 2 weeks
- Need to track data types(vector, register etc)
- Decide how to implement programming model 
- Full ISA support within 4 weeks
- Full stdlib in 8 weeks
- Registers should not have synonyms
    - Compiler has complete control over allocation?
- By sunday be able to compile a custom instruction

```
int main(){
    inline("
        theta x0, x1, x2
    ");
    cout << x0 << '\n';
}
```



```
q = smalloc(128*64) # this goes to scratchpad

memset(q, ptr) # ptr = dram
q0 = q[0]
q7 = q[7]
y = q0 * q7 


```

