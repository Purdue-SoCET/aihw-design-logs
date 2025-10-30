## State
I am not stuck.

## Progress
- I couldn't attend the Sunday meeting (10/26) because my flight back got delayed.
- Nikhil updated me on things that were discussed on Sunday:
  - ```So for future reference instruction latency through systolic array is 64 MAC cycles = 64x3 clock cycles. Meaning if we are to support the maximum case we need 64x3 entries in the fifo which is 64x3x8 bits which probably needs to be ported to SRAM IP instead of FFs.```
  -   For the shifting unit, after we get the stripped down version from Haejune, we have to come up with a Python simulation to generate the control bits. The control bits are fixed.
  -   From Haejune:
  -   ```For Benes control bit generation, it’s just going to be a simple int [32] array. It’s a python code, so nothing hardware. If it’s fixed, then same 144bits are going to be used, so very simple copying and pasting result from the code I will send you tmr. And by feeding that into benes, it will return the output of [DATA_WIDTH] output [LENGTH] in the desired order. So destination array will look something like [7, 8, 3, 4, …] this means 7th input will end up in i=0, 8th will end up in i=1, etc```
  - The python code:
```import random
def permutation(c):
    m = 1
    while (2*m-1)<<(m-1) < len(c): m += 1
    assert (2*m-1)<<(m-1) == len(c)
    
    n = 1<<m
    pi = list(range(n))
    for i in range(2*m-1):
        gap = 1<<min(i,2*m-2-i)
        for j in range(n//2):
            if c[i*n//2+j]:
                pos = (j%gap)+2*gap*(j//gap)
                pi[pos],pi[pos+gap] = pi[pos+gap],pi[pos]
                # print(f"pi {i + 1}.{j}: ", pi)
    return pi

def composeinv(c,pi):
    return [y for x,y in sorted(zip(pi,c))]

def controlbits(pi):
    n = len(pi)
    m = 1

    while 1<<m < n: m += 1

    if m == 1: return [pi[0]]

    p = [pi[x^1] for x in range(n)]
    q = [pi[x]^1 for x in range(n)]
    piinv = composeinv(range(n),pi)

    p,q = composeinv(p,q),composeinv(q,p)
    c = [min(x,p[x]) for x in range(n)]
    p,q = composeinv(p,q),composeinv(q,p)

    for i in range(1,m-1):
        cp,p,q = composeinv(c,q),composeinv(p,q),composeinv(q,p)
        c = [min(c[x],cp[x]) for x in range(n)]

    f = [c[2*j]%2 for j in range(n//2)]
    F = [x^f[x//2] for x in range(n)]
    Fpi = composeinv(F,piinv)

    l = [Fpi[2*k]%2 for k in range(n//2)]
    L = [y^l[y//2] for y in range(n)]
    M = composeinv(Fpi,L)

    subM = [[M[2*j+e]//2 for j in range(n//2)] for e in range(2)]
    subz = map(controlbits,subM)

    z = [s for s0s1 in zip(*subz) for s in s0s1]

    return f+z+l


# Example
N = 32
# perm = list(range(N)); random.shuffle(perm)
perm = [27, 24, 2, 29, 4, 7, 20, 10, 1, 0, 8, 9, 3, 13, 16, 26, 12, 31, 17, 19, 28, 18, 23, 30, 5, 15, 6, 21, 11, 25, 22, 14]
ctrl = controlbits(perm)
ctrl_string = ''.join(str(b) for b in ctrl)
ctrl_module = ctrl_string[::-1]    # The final ctrol bit for benes_network module
print(ctrl_module)
result = permutation(ctrl)
print(result)
```
## Evidence of Progress
- On 10/29 Wednesday, we had a code verification presentation during the Vector Core meeting.
- Me and Nikhil presented the verification plan and waveforms for the GSAU control unit.
- Code: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/src/modules/gsau_control_unit.sv
- TB: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/src/testbench/gsau_control_unit_tb.sv
- Waves: https://github.com/Purdue-SoCET/atalla/blob/tensor_compute_accelerator_saandiya/src/waves/gsau_control_unit_tb.do
![Screenshot 2025-10-30 at 3 02 44 PM](https://github.com/user-attachments/assets/e363f462-9fc6-46a7-959c-2a846adb33f8)
![Screenshot 2025-10-30 at 3 03 31 PM](https://github.com/user-attachments/assets/d9f7f7d1-cb90-4a00-8c44-7a536e113027)
![Screenshot 2025-10-30 at 3 04 24 PM](https://github.com/user-attachments/assets/15955326-6818-4609-95cf-9fd99e886065)
- Synthesis report at 1666.666ps and a duty cycle of 800:
<img width="492" height="594" alt="image" src="https://github.com/user-attachments/assets/8e6bd6dd-a1ea-4711-8882-e88b179d81bf" />
 
- Feedback from Jing: ```gsau: 1. make sure case 3 has one cycle gap instead of 2 cycles. 2. get critical path.```

## Future plans
1. Convert fifos into sram in gsau control unit.
2. Come up with shifting unit bit generation python module.
3. Work on 2nd Design Review slides which is on 11/10 Monday.



