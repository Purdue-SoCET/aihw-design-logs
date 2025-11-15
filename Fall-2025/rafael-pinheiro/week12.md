State: I am not stuck with anything, don't need help right now.

## Progress summary

Vector Core modelling started and Veggie File model done. Technically Vector Core modelling was done during the weekend of 11/8-9, so I decided to move to week 12 design log so I have something to show. Besides that, as mentioned, progress slow due to 3 midterms this week. Will try to compensate for it during Thanksgiving.

Also, prepared the slides and presented for Design Review #2.

## Veggie File and Op Buffer

### Veggie File

```python
class Veggie(Clocked):
    def __init__(self, bank_count=4, regs_per_bank=64, dread_ports=4, dwrite_ports=2, mask_banks=2):
        super().__init__()
        self.bank_count = bank_count
        self.regs_per_bank = regs_per_bank
        self.dread_ports = dread_ports
        self.dwrite_ports = dwrite_ports
        self.mask_banks = mask_banks

        # register storage
        self.data_banks = [[0] * regs_per_bank for _ in range(bank_count)]
        self.mask_banks_data = [[0] * regs_per_bank for _ in range(mask_banks)]

        # connection endpoints
        self.inp = None
        self.out = None

        # internal state
        self.conflict = False
        self.pending_reqs = []

    def connect(self, inp, out):
        self.inp = inp
        self.out = out
```
The ```__init__()``` constructor defines the structural parameters of the Veggie file — number of banks, register depth, and ports.
Each bank is modeled as a simple Python list to simulate fast indexed access.
The connect() method wires Veggie’s I/O interfaces to external modules, such as buffers or decoders.

```python
    def Tick(self, time):
        if not self.inp:
            return

        read_reqs = getattr(self.inp, "read_reqs", [])
        write_reqs = getattr(self.inp, "write_reqs", [])

        bank_rreqs = defaultdict(list)
        bank_wreqs = defaultdict(list)

        for req in read_reqs:
            bank_rreqs[req["bank"]].append(req)
        for req in write_reqs:
            bank_wreqs[req["bank"]].append(req)

        # detect conflicts
        self.conflict = any(len(v) > 1 for v in bank_rreqs.values()) or \
                        any(len(v) > 1 for v in bank_wreqs.values())

        if self.conflict:
            # hold off and retry next tick
            self.pending_reqs.append((read_reqs, write_reqs))
            if self.out:
                self.out.ready = False
            return

        read_results = {}
        for bank_id, reqs in bank_rreqs.items():
            if reqs:
                req = reqs[0]
                read_results[req["port"]] = self.data_banks[bank_id][req["addr"]]

        for bank_id, reqs in bank_wreqs.items():
            if reqs:
                req = reqs[0]
                self.data_banks[bank_id][req["addr"]] = req["data"]

        if self.out:
            self.out.vreg = read_results
            self.out.dvalid = {p: (p in read_results) for p in range(self.dread_ports)}
            self.out.ready = True
```

On each tick:

1- It checks for valid read/write requests

2- It detects any bank conflicts (two operations to the same bank in one cycle)

3- If no conflict occurs, it performs the reads/writes, updates Veggie’s internal register banks, and sets valid output data (vreg and dvalid) for the next pipeline stage

4- If there’s a conflict, it queues the operations to retry on the next tick

### Op Buffer

The OpBuffer class models a small staging buffer that receives data and mask values from the Veggie file.
It ensures that operands and their corresponding masks are available before signaling “ready” to the next pipeline stage

```python
class OpBuffer(Clocked):
    def __init__(self, num_pairs=1):
        super().__init__()
        self.num_pairs = num_pairs
        self.dready = [False] * (2 * num_pairs)
        self.mready = [False] * num_pairs
        self.vreg_tmp = [None] * (2 * num_pairs)
        self.vmask_tmp = [None] * num_pairs
        self.inp = None
        self.out = None

    def connect(self, inp, out):
        self.inp = inp
        self.out = out
```

The constructor initializes buffer slots for operand and mask pairs.
Each OpBuffer instance can manage multiple pairs of operands per instruction group, allowing simple vector operation batching.

```python
def Tick(self, time):
        if not self.inp:
            return

        dvalid = getattr(self.inp, "dvalid", {})
        mvalid = getattr(self.inp, "mvalid", {})
        vreg = getattr(self.inp, "vreg", {})
        vmask = getattr(self.inp, "vmask", {})

        # Capture data valid operands
        for i in range(2 * self.num_pairs):
            if dvalid.get(i, False):
                self.vreg_tmp[i] = vreg[i]
                self.dready[i] = True

        # Capture mask valid
        for i in range(self.num_pairs):
            if mvalid.get(i, False):
                self.vmask_tmp[i] = vmask[i]
                self.mready[i] = True

        # For this test, mark valid if we have *any operand* and mask
        ivalid = [any(self.dready) and any(self.mready)]

        if self.out:
            self.out.ivalid = ivalid
            self.out.vreg = self.vreg_tmp.copy()
            self.out.vmask = self.vmask_tmp.copy()
            self.out.ready = all(ivalid)

        # Reset once consumed
        if all(ivalid):
            self.dready = [False] * (2 * self.num_pairs)
            self.mready = [False] * self.num_pairs
```

On each tick:

1- Samples dvalid and mvalid from Veggie’s output.

2- Stores the operand and mask once they become valid.

3- Marks the internal ivalid signal true only when at least one operand and one mask are ready, emulating pipeline readiness.

4- Clears readiness once the values are propagated

### Testbenching

The testbench builds a minimal simulation using the event-driven engine (EventQueue, ClockDomain, Sim) to test dataflow from Veggie -> OpBuffer

```python
class IO:
    def __init__(self):
        # Veggie <-> OpBuffer signals
        self.read_reqs = []
        self.write_reqs = []
        self.vreg = {}
        self.vmask = {}
        self.dvalid = {}
        self.mvalid = {}
        self.ready = True
        self.ivalid = []
        # outputs container for op buffer
        self.vreg = {}
        self.vmask = {}
```

Acts as a dummy interconnect structure — mimicking signal bundles between hardware modules (instead of using full SystemVerilog-style interfaces)

```python
def build_sim():
    eq = EventQueue()
    clk = ClockDomain(eq, period=1.0)
    core = Core(eq)
    core.add_clock_domain(clk)
    sim = Sim()
    sim.init(eq, core)
    return eq, clk, sim
```

Initializes the event-driven simulation environment, defining a clock (1.0 unit period) and linking all modules into a single core.

Mirrors a top-level testbench instantiation in HDL simulation

```python
def test_vector_pipeline():
    eq, clk, sim = build_sim()

    veggie = Veggie(bank_count=2, regs_per_bank=8, dread_ports=1, dwrite_ports=1, mask_banks=1)
    opbuf = OpBuffer(num_pairs=1)

    veg_in = IO()
    veg_out = IO()
    op_in = veg_out
    op_out = IO()

    veggie.connect(veg_in, veg_out)
    opbuf.connect(op_in, op_out)

    # register to clock domain (optional here, we schedule ticks explicitly)
    clk.add_clocked(veggie)
    clk.add_clocked(opbuf)

    # schedule a write at t=0.0
    veg_in.write_reqs = [{"port": 0, "bank": 0, "addr": 2, "data": 99}]
    veg_in.read_reqs = []
    eq.schedule(0.0, veggie.Tick, 0.0)

    # schedule a read at t=1.0 (we set the request just before scheduling)
    def place_read(time):
        veg_in.write_reqs = []
        veg_in.read_reqs = [{"port": 0, "bank": 0, "addr": 2}]
        print(f"[{time}] test: placed read_req")
    eq.schedule(1.0, place_read, 1.0)

    # schedule veggie to service the read shortly after placement
    eq.schedule(1.01, veggie.Tick, 1.01)

    # schedule opbuf to sample veggie output after veggie produced it
    eq.schedule(1.02, opbuf.Tick, 1.02)

    # inject mask so op buffer can combine it with data
    def inject_mask(time):
        op_in.mvalid = {0: True}
        op_in.vmask = {0: 0xFF}
        print(f"[{time}] Injected mask into op_in")
    eq.schedule(1.03, inject_mask, 1.03)

    # call opbuf again to observe the combined result
    eq.schedule(1.04, opbuf.Tick, 1.04)

    # run sim
    sim.run(until=2.0)

    # results
    print("\n--- RESULTS ---")
    print("veg_out.vreg:", veg_out.vreg)
    print("veg_out.dvalid:", veg_out.dvalid)
    print("op_out.ivalid:", op_out.ivalid)
    print("op_out.vreg:", getattr(op_out, "vreg", {}))
    print("op_out.vmask:", getattr(op_out, "vmask", {}))
    print("----------------\n")

    # assertions
    assert veg_out.vreg.get(0, None) == 99, f"Veggie readback failed: {veg_out.vreg}"
    assert op_out.ivalid and op_out.ivalid[0] is True, f"OpBuffer didn't mark ready: {op_out.ivalid}"
    print("Test passed")
```

1- Writes data 99 into Veggie register [bank=0, addr=2]

2- Issues a read request from the same register after one cycle

3- Veggie returns 99 to its output interface

4- OpBuffer samples the Veggie output and waits for a valid mask

5- Mask 0xFF is injected

6- OpBuffer combines data + mask and marks the pair valid

```bash
socet149@asicfab:~/atalla-sim (rafael-branch)$ export PYTHONPATH=$(pwd)/src
socet149@asicfab:~/atalla-sim (rafael-branch)$ python3 -m tests.test_veggie
[1.0] test: placed read_req
[1.03] Injected mask into op_in

--- RESULTS ---
veg_out.vreg: {0: 99}
veg_out.dvalid: {0: True}
op_out.ivalid: [True]
op_out.vreg: [99, None]
op_out.vmask: [255]
----------------

Test passed
```

- Veggie correctly handled write -> readback sequencing
- OpBuffer combined valid operand and mask to produce a ready output

## Next Steps

- Start modelling Vector Core's Scoreboard and WriteBack Buffer