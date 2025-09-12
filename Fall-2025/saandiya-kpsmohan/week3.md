## Routing Algorithm - Partial Sum

A. How to detect this deterministically  

You already have enough info to know which PSUMs are final:  
	1.	PE coordinates (i,j)  
	•	Tells you which output pixel the PE contributes to.  
	2.	Kernel size (R×S) and output channel K  
	•	Tells you how many multiplications are needed for a complete dot product.  
	3.	Input tile size (C_in)  
	•	Tells you how many channels need to be accumulated.  

So the condition is:  
  If PE(i,j) has seen the last input channel and last kernel row/column contribution for its assigned output,  
  then mark its PSUM as final → write back to scratchpad.    

B. Where to put the PSUMs until ready    

There are two options depending on architecture:   
	•	Option A (common in TPU-like arrays):  
Each PE forwards its PSUM down the array until it reaches the bottom row/right edge. The bottom outputs are always final and go directly to scratchpad.  
Simple, but requires careful scheduling.  
	•	Option B (with Accumulation FIFOs):  
Each PE outputs its PSUM to a per-output FIFO.  
The controller checks:     
	•	“Is this the last contribution for pixel (n,h,w,k)?”  
	•	If yes, write from FIFO → scratchpad.  
	•	If no, keep accumulating.  
More flexible, but requires extra control and a crossbar.  

C. When to write back to scratchpad  
	•	At the end of processing each tile (all channels of the input tile have passed through the systolic array).  
	•	You can deterministically compute this from loop indices in your controller:  
	•	if (input_channel == C_in-1) and (kernel_row == R-1) and (kernel_col == S-1)  
→ then write PSUM back.  

This is why many designs maintain a PSUM buffer (in scratchpad or register file):  
	•	In the middle of processing, you do:  
PSUM[next] = PSUM[prev] + contribution  
	•	At the very end, you flush it to output SRAM.  

Flow:  
	1.	Each PE accumulates local PSUMs.  
	2.	Controller decides mask + route (which PSUM goes to which FIFO).  
	3.	FIFO holds intermediate PSUMs until final contribution arrives.  
	4.	Once “last channel + last kernel row” condition is met →  
	•	Write back to scratchpad.  





## Routing Algorithm Flow for PSUM Handling

Step 0 – Setup  
	•	Inputs:  
    	•	Input tensor A(C,H,W)  
    	•	Kernel tensor K(M,C,R,S) (M = output channels)  
	•	Parameters:  
  	•	Stride, padding  
	•	Outputs:  
  	•	Output tensor O(M,P,Q) where  
  P = (H − R)/stride + 1 and Q = (W − S)/stride + 1  

⸻

Step 1 – Initialize Data Structures  
	•	Scratchpad Buffers: hold inputs, kernels, and partial sums  
	•	Accumulator FIFOs (per output pixel): acc_fifo[(m,p,q)]  
	•	Routing Table: maps (PE position, input index, kernel index) → (m,p,q)  

⸻

Step 2 – Feed Input and Kernel into Systolic Array  
	•	Inject input activations row by row (or column by column depending on array orientation).  
	•	Kernels are pre-loaded (stationary weight model).  
	•	Each PE(i,j) performs:  
 term = A[c, row_start+i, col_start+j] * K[m, c, i, j]  
 	•	Each term is tagged with its destination output pixel (m,p,q).  

⸻

Step 3 – Masking (Determine Useful PSUMs)  
	•	Each PE computes products, but not all terms belong to the same output.  
	•	Use deterministic index mapping:  
  output_row = (input_row - kernel_row_offset) // stride  
  output_col = (input_col - kernel_col_offset) // stride  
	•	If (output_row, output_col) is valid, keep the PSUM. Otherwise, discard.  

⸻

Step 4 – Routing  
	•	Once a term is computed:  
	•	Look up (m,p,q) in the routing table.  
	•	Push the term into acc_fifo[(m,p,q)].  

⸻

Step 5 – Accumulation Control  
	•	Each output pixel (m,p,q) requires R*S*C contributions.  
	•	Track FIFO depth:  
   if fifo_count[(m,p,q)] == R*S*C:  
      flush_to_scratchpad(m,p,q)  
  	•	Flushing writes the final accumulated PSUM back to scratchpad.  

⸻

Step 6 – Crossbar Usage  
	•	Needed if multiple FIFOs must be fed in the same cycle from different PEs.  
	•	Crossbar ensures each PE’s output goes to the correct acc_fifo without conflict.  

⸻

## Pseudocode Version
    for each cycle:
        for each PE(i,j):
            if input and weight valid:
                term = A[c, row_start+i, col_start+j] * K[m,c,i,j]
                (p,q) = compute_output_pixel(row_start+i, col_start+j, i, j, stride)
                
                if valid(p,q):
                    route(term, dest_fifo=acc_fifo[(m,p,q)])
                
      for each (m,p,q):
          if acc_fifo[(m,p,q)].count == R*S*C:
              scratchpad[m,p,q] = sum(acc_fifo[(m,p,q)])
              acc_fifo[(m,p,q)].clear()
