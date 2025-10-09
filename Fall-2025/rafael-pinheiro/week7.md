```markdown
State

I am not blocked on any tasks at the moment.

## Progress

This week my primary work was on the read Service FSM (`r_fsm`) for the scratchpad frontend (single-VC version). I implemented the FSM and a corresponding testbench to exercise basic request/response flows and to validate the handshakes with the scratchpad interface

I included the current `r_fsm` module and the `r_fsm_tb` testbench below (verbatim). These are the exact sources I used while developing and debugging the FSM

### r_fsm.sv

```systemverilog
/*
  Rafael Monteiro Martins Pinheiro
  rmontei@purdue.edu

  Service FSM for Scratchpad Frontend read requests (single VC version)
*/

`include "memory/scratchpad/scpad_types_pkg.vh"
`include "memory/scratchpad/scratchpad_if.vh"

module r_fsm #(
	parameter VC_ID = 0   // parameterize which VC this FSM serves
)(
	input  logic clk, n_rst,
	scpad_if.vc_frontend sif   // new modport for one VC
);
	import scpad_types_pkg::*;

	typedef enum logic [2:0] {
		R_IDLE,
		R_MAKE_XBAR_DESC,
		R_REQ_XBAR,
		R_ISSUE_SRAM,
		R_RESP_DONE
	} state_t;

	state_t state, nextstate;

	frontend_req_t cur_req;
	xbar_desc_t cur_xbar_desc;

	sram_r_req_t sram_read_req_reg;
	logic frontend_read_busy;

	always_comb begin : next_state_logic
		nextstate = state;

		case (state)
			R_IDLE: begin
				if (sif.frontend_req.valid)
					nextstate = R_MAKE_XBAR_DESC;
			end

			R_MAKE_XBAR_DESC: begin
				nextstate = R_REQ_XBAR;
			end

			R_REQ_XBAR: begin
				if (!sif.sram_busy)
					nextstate = R_ISSUE_SRAM;
			end

			R_ISSUE_SRAM: begin
				if (sif.frontend_sram_read_res.valid)
					nextstate = R_RESP_DONE;
			end

			R_RESP_DONE: begin
				if (sif.read_complete) begin
					if (sif.frontend_req.valid)
						nextstate = R_MAKE_XBAR_DESC;
					else
						nextstate = R_IDLE;
				end
			end
		endcase
	end

	always_ff @(posedge clk, negedge n_rst) begin : state_regs
		if (!n_rst) begin
			state              <= R_IDLE;
			cur_req            <= '0;
			cur_xbar_desc      <= '0;
			frontend_read_busy <= 1'b0;
			sram_read_req_reg  <= '0;
		end else begin
			state              <= nextstate;
			frontend_read_busy <= (nextstate != R_IDLE);

			if (nextstate == R_REQ_XBAR && state == R_MAKE_XBAR_DESC) begin
				// Temporary masks
				// Will change this after I figure how to do the comunication with the handler (if there will be one)
				cur_xbar_desc.slot_mask  <= '{default: '0};
				cur_xbar_desc.shift_mask <= '{default: '0};
				cur_xbar_desc.valid_mask <= '{default: 1'b1};
			end

			if (state == R_REQ_XBAR && nextstate == R_ISSUE_SRAM) begin
				sram_read_req_reg.int_id    <= (VC_ID == 0) ? FRONTEND_VC1_REQ : FRONTEND_VC2_REQ;
				sram_read_req_reg.valid     <= 1'b1;
				sram_read_req_reg.xbar_desc <= cur_xbar_desc;
				sram_read_req_reg.scpad_id  <= cur_req.scpad_id;
			end
		end
	end

	always_comb begin : output_logic
		sif.frontend_res.valid    = 1'b0;
		sif.frontend_res.complete = 1'b0;
		sif.frontend_res.rdata    = '0;

		sif.frontend_sram_read_req = '0;
		sif.frontend_ready         = !frontend_read_busy;

		case (state)
			R_ISSUE_SRAM: begin
				if (sram_read_req_reg.valid) begin
					sif.frontend_sram_read_req = sram_read_req_reg;
				end else begin
					// On-the-fly issue
					sif.frontend_sram_read_req.int_id    = (VC_ID == 0) ? FRONTEND_VC1_REQ : FRONTEND_VC2_REQ;
					sif.frontend_sram_read_req.valid     = 1'b1;
					sif.frontend_sram_read_req.xbar_desc = cur_xbar_desc;
					sif.frontend_sram_read_req.scpad_id  = cur_req.scpad_id;
				end
			end

			R_RESP_DONE: begin
				sif.frontend_res.valid    = 1'b1;
				sif.frontend_res.complete = 1'b0; // wait until read_complete external
				sif.frontend_res.rdata    = sif.frontend_sram_read_res.rdata;
			end
		endcase
	end
endmodule
```

### r_fsm_tb.sv

```systemverilog
`timescale 1ns/1ps
`include "memory/scratchpad/scpad_types_pkg.vh"
`include "memory/scratchpad/scratchpad_if.vh"

module r_fsm_tb;

logic clk;
logic n_rst;

// Instantiate the interface
scpad_if sif();

// DUT hooked up to generic vc_frontend modport
r_fsm #(.VC_ID(0)) dut (
	.clk(clk),
	.n_rst(n_rst),
	.sif(sif.vc_frontend)
);

// Clock generation
initial clk = 0;
always #5 clk = ~clk; // 100 MHz

// Reset task
task reset_dut();
begin
	n_rst = 0;
	sif.frontend_req        = '0;
	sif.sram_busy           = 0;
	sif.frontend_sram_read_res = '0;
	sif.frontend_sram_write_res = '0;
	sif.read_complete       = 0;
	#20;
	n_rst = 1;
end
endtask

initial begin
	$display("[%0t] Starting r_fsm_tb...", $time);
	reset_dut();

	// === Test 1: issue one request ===
	@(posedge clk);
	sif.frontend_req.valid    <= 1;
	sif.frontend_req.scpad_id <= 4'h1;
	@(posedge clk);
	sif.frontend_req.valid    <= 0;


	wait(sif.frontend_sram_read_req.valid);
	$display("[%0t] Req issued: scpad_id=%0d", $time, sif.frontend_sram_read_req.scpad_id);

	repeat (3) @(posedge clk);
	sif.frontend_sram_read_res.valid <= 1;
	sif.frontend_sram_read_res.rdata <= 32'hDEADBEEF;
	@(posedge clk);
	sif.frontend_sram_read_res.valid <= 0;

	repeat (2) @(posedge clk);
	sif.read_complete <= 1;
	@(posedge clk);
	sif.read_complete <= 0;

	wait(sif.frontend_res.valid);
	$display("[%0t] FSM responded with rdata=%h", $time, sif.frontend_res.rdata);

	// === Test 2: back-to-back requests ===
	repeat (2) begin
		@(posedge clk);
		sif.frontend_req.valid    <= 1;
		sif.frontend_req.scpad_id <= $urandom_range(0,15);
		@(posedge clk);
		sif.frontend_req.valid    <= 0;

		wait(sif.frontend_sram_read_req.valid);

		repeat (2) @(posedge clk);
		sif.frontend_sram_read_res.valid <= 1;
		sif.frontend_sram_read_res.rdata <= $random;
		@(posedge clk);
		sif.frontend_sram_read_res.valid <= 0;

		repeat (2) @(posedge clk);
		sif.read_complete <= 1;
		@(posedge clk);
		sif.read_complete <= 0;

		wait(sif.frontend_res.valid);
		$display("[%0t] FSM response: rdata=%h", $time, sif.frontend_res.rdata);
	end

	$display("[%0t] All tests completed!", $time);
	$finish;
end
endmodule
```

## Design-review notes (summary)

During the design review the team decided to offload the Systolic Array as a functional unit inside the Vector Core. This changes the data-movement model: data now moves from the scratchpad into the Vector Core (via the veggie file) and then into the Systolic Array for computation. The motivation is increased programmability and simpler mapping for convolution-style operations.

Key points from the discussion and instructions from Akshath:

- Vector Core throughput requirement: the Vector Core should be able to issue a request into the scratchpad every cycle and expect the data back in N+2 cycles (N = crossbar latency, +2 = per-unit latency).

- Architectural implication: the request/response datapath should be pipelined rather than strictly sequenced by an FSM. The team argued this simplifies logic: implement two data-path "channels", each with a request and response lane. Each frontend servicing unit holds one horizontal pipeline for issuing requests to the SRAM and another for receiving responses back into the Vector Core.

- With two channels, the Vector Core can send two requests per cycle. The software/compiler guarantees that the two requests target alternate scratchpads, which simplifies hardware arbitration.

- Because the datapath is pipelined and latency is fixed (N+2), the request sequencing FSM can be removed. Instead, the design relies on latches (or tail latches) that act as small buffers; a single-cycle stall signal can be used to stop the pipeline if SRAM stalls. No split-transaction queue is required on the frontend because responses are in-order and the tail latches are dedicated for that stream.

- Practical rules and caveats discussed:
  - The frontend and backend each maintain two sets of units, each capable of issuing one request per cycle.
  - If the backend (SRAM) takes longer, the pipeline stalls — the frontend must assert a stall signal to the Vector Core so request latches are not cleared. No ACK is required for requests; only a stall signal is used to prevent data loss.
  - Julio's path to DRAM is split-transaction and cannot be stalled in the same way; Julio needs a buffer/queue to absorb backpressure from DRAM while keeping SRAM/DRAM controllers decoupled.

Diagram reference used in the discussion:

https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22%7D

## Next steps

- Continue adapting the `r_fsm` logic toward a pipelined, multi-channel datapath as discussed; in practice this means refactoring the FSM into a steady-state request/response pipeline with small per-channel latches and a stall signal for back-pressure
- After the datapath refactor, create top-level functional testbenches and integrate with the veggie file and the Vector Core's flow

```markdown