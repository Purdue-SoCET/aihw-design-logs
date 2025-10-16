State

I am not stuck on any tasks right now and do not need immediate help.

## Progress summary

Fall break — Emmi started writing the code for `frontend.sv`. I produced new frontend diagrams based on the Week 7 spec and updated the interface assumptions

Diagrams: https://app.diagrams.net/#G1ElCZMM-KjPGufnR3GiQcNenLo1k3HUEb#%7B%22pageId%22%3A%22z5i2-UzuZiJJCSVkOzf7%22%7D

### Frontend implementation (notes)

The frontend is implemented as a small pipeline that latches Vector Core requests, forwards them to the frontend VC logic, and then to the SRAM controller / crossbar. It mirrors the handshake signals from the scratchpad interface and gates progress with `fe_stall`

Key points from the current `frontend.sv` draft:

- The module imports `scpad_types_pkg` and `scratchpad_if` and instantiates a `frontend_vc` submodule
- A two-stage latch pipeline is used to synchronize requests/responses between the Vector Core and SRAM/Xbar interfaces
- `pipe_EN = !fsif.fe_stall[IDX]` is used to gate all pipeline latches so the frontend respects backpressure

The code below is the current draft that Emmi started:

```systemverilog
`include "scpad_types_pkg.vh"
`include "scratchpad_if.vh"

module frontend #(
    parameter logic [SCPAD_ID_WIDTH-1:0] IDX = '0
) (
    input logic clk, n_rst,
    scpad_if.frontend_vec fvif, 
    scpad_if.frontend_body fsif
); 
    import scpad_types_pkg::*;
    logic vec_rd_req_valid_syn;
    logic vec_wr_req_valid_syn;
    logic fe_rd_res_valid_syn;
    logic fe_wr_res_valid_syn;

    scpad_if.frontend_vc vcif;

    //pipeline enable
    logic pipe_EN; 
    assign pipe_EN = !fsif.fe_stall[IDX];
    
    // stall vec request bit
    assign fvif.fe_vec_stall[IDX] = fsif.fe_stall[IDX];

    //fe_vc module

    frontend_vc #(.IDX(IDX)) u_frontend_vc (
        .vcif(vcif) // will see about this
    ); 

    ///////////pipeline////////////

    //latch incoming requests from vector core and send to units
    latch #(.T(rd_req_t)) l1a (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN && fvif.vec_rd_req_valid[IDX]), .in(fvif.vec_rd_req[IDX]), .out(vcif.vc_read_req[IDX])
    ); 

    latch #(.T(wr_req_t)) l1b (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN && fvif.vec_wr_req_valid[IDX]), .in(fvif.vec_wr_req[IDX]), .out(vcif.vc_write_req[IDX])
    ); 

    //latch valid bits from vc

    latch #(.T(logic)) l1c (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fvif.vec_rd_req_valid[IDX]), .out(vec_rd_req_valid_syn)
    ); 

    latch #(.T(logic)) l1d (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fvif.vec_wr_req_valid[IDX]), .out(vec_wr_req_valid_syn)
    ); 

    //latch units' output requests to sram controller/xbar

    latch #(.T(rd_req_t)) l2a (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vcif.sram_read_req[IDX]), .out(fsif.fe_rd_req[IDX])
    ); 

    latch #(.T(wr_req_t)) l2b (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vcif.sram_write_req[IDX]), .out(fsif.fe_wr_req[IDX])
    ); 

    //latch valid bits to send to sram/xbar

    latch #(.T(logic)) l2c (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vec_rd_req_valid_syn), .out(fsif.fe_rd_req_valid[IDX])
    ); 

    latch #(.T(logic)) l2d (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vec_wr_req_valid_syn), .out(fsif.fe_wr_req_valid[IDX])
    ); 


    ///////////// to sram/xbar /////////////
    ///////////// back from sram/xbar ////////////////

    //latch incoming responses

    latch #(.T(rd_res_t)) l3a (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN && fsif.fe_rd_res_valid[IDX]), .in(fsif.fe_rd_res[IDX]), .out(vcif.sram_read_res[IDX])
    ); 

    latch #(.T(wr_res_t)) l3b (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN && fsif.fe_wr_res_valid[IDX]), .in(fsif.fe_wr_res[IDX]), .out(vcif.sram_write_res[IDX])
    ); 

    // latch valid bits from sram/xbar

    latch #(.T(logic)) l3c (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fsif.fe_rd_res_valid[IDX]), .out(fe_rd_res_valid_syn)
    ); 

    latch #(.T(logic)) l3d (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fsif.fe_wr_res_valid[IDX]), .out(fe_wr_res_valid_syn)
    ); 

    // latch edited responses 

    latch #(.T(rd_res_t)) l4a (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vcif.sram_read_res[IDX]), .out(fvif.vec_rd_res[IDX])
    ); 

    latch #(.T(wr_res_t)) l4b (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(vcif.sram_write_res[IDX]), .out(fvif.vec_wr_res[IDX])
    ); 

    // latch valid bits to send to vc

    latch #(.T(logic)) l4c (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fe_rd_res_valid_syn), .out(fvif.vec_rd_res_valid[IDX]) 
    ); 

    latch #(.T(logic)) l4d (.clk(clk), .n_rst(n_rst), 
        .en(pipe_EN), .in(fe_wr_res_valid_syn), .out(fvif.vec_wr_res_valid[IDX])
    ); 


endmodule
```

## Akshath: Changes and impact

Akshath asked us to simplify the Vector Core <-> Frontend contract: the Vector Core will not use both read and write channels for the same unit simultaneously. This reduces duplicated signals and simplifies the frontend pipeline

Concrete implications:

- Safely remove the duplicate latch paths that assume simultaneous rd+wr for a single IDX; keep the latches that service the active channel per instruction. Practically this means dropping about half of the per‑IDX latch pairs (either the rd or wr path) in `frontend.sv` and `frontend_vc` if the instruction set guarantees mutually exclusive r/w usage for each request
- Update `scpad_if.vh` / `scpad_types_pkg.vh` to document that a single channel is active at a time (or add a 1‑bit selector field) so the frontend and vector core share a clear contract
- Verify `fe_vec_stall` and `fe_stall` interactions still meet timing after latches are removed (the pipe gating remains required)

Suggested immediate actions:

1. Review `scpad_if.vh` for an explicit channel selector/flag and add comments documenting mutual exclusion.
2. Remove redundant latches in `frontend.sv` (candidate: drop either l1a/l1c or l1b/l1d per IDX depending on instruction type) and update `frontend` accordingly
3. Run the frontend unit testbench and smoke-test basic rd/wr flows with single-channel active

## Abstract for Purdue Fall Undergraduate Research Expo 

## Next steps

1. Finish the `frontend.sv` implementation before Friday's RTL freeze
2. Remove redundant rd/wr latches per Akshath's guidance and update `frontend`
3. Update `scpad_if.vh` with a channel-selection comment/field and add test vectors that exercise the mutually‑exclusive path
4. Start verification: write a minimal TB that toggles rd/wr channels (one at a time) and validates handshake and data paths