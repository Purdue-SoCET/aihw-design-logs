State: I am not stuck with anything, don't need help right now.

## Progress summary

Simulating Lockup-Free Cache in a Cycle-Accurate Simulator

### What's the Lockup-Free Cache?

The Lockup-Free Cache is a parametrizable C-byte-sized, W-way Cache with N banks.

It works not much differently than the 437 DCache, with the twist that is Lookup-Free, i.e. services subsequent hit accesses to memory even if a previous access was a miss and is waiting on the requested data to be fetched.

On a miss, the cache allocates a Miss State Holding Register (MSHR) entry that tracks outstanding requests, forward the miss to the next memory level and later merges or forwards the returning line to all requestors that waited for that line. Subsequent requests can still be served if hit, or coalesced into existing MSHRs if tergeting the same block.

### Why using a Lockup-Free Cache?

Improves throughput and IPC for memory‑intensive workloads by keeping the pipeline and other cache operations progressing during long latency misses.
Essential for out‑of‑order and wide superscalar designs or any design with many in‑flight memory operations.
Minimal contract (inputs/outputs and observable behavior).

#### Hit/Miss Behavior
On a hit: respond immediately with data and do not allocate an MSHR.

On a miss:
- Allocate an MSHR entry that records the requestor, request type, and any merging candidates.
- Send a miss request to the next level (or memory).
- Allow other accesses to progress; coalesce requests to same block into the MSHR (avoid duplicate memory requests).
- When refill arrives, complete all outstanding requestors for that block and free the MSHR.

#### Key components
- Tag RAM and data RAM (standard).
- MSHR table: entries track outstanding miss address (block address), source requestors, pending write/read types, merge list, and state.
- Miss request queue: sends requests to next‑level/memory.
- Refill path: accepts returning cache lines and updates data RAM/tags and completes MSHR entries.
- Optional write buffers / writeback logic and eviction handling.
- Replacement policy, dirty tracking and eviction mechanism.

#### Important edge cases
- MSHR saturation: fixed number of MSHRs limits outstanding misses. On saturation you must stall/queue upstream requests. Choose MSHR depth based on target concurrency.
- Multiple requestors for same block: must coalesce to one outstanding miss; ordering of returns and write merging matters for correctness.
- In-flight stores (atomicity): store buffering vs write‑through decisions change semantics. For a write miss, decide allocate on write and whether to forward to memory or allocate MSHR + refill.
- Eviction of a block that has outstanding requestors (writeback): must prevent evicting an in‑flight line or handle writeback safely.
- Memory ordering and coherence: if you have a coherence protocol, MSHRs and merging must respect ordering and coherence messages (e.g., snoops arriving while a miss is outstanding).
- Refill partial lines or bursts: handle sub-block fills and alignment cleanly.
- Interrupts / resets while misses outstanding: specify recovery behavior (flush, commit, or hold).

#### Pros and cons
##### Pros:
- Higher throughput and better utilization of CPU and memory bus.
- Avoids pipeline stalls caused by single long latency miss.
##### Cons:
- More complex to implement and verify.
- Requires extra storage (MSHRs) and logic (coalescing, refill completion).
- Requires careful handling with coherence or ordering semantics.


### CHANGE OF PLANS

All of this was useless, since we now moved from modelling the Lock-Up Free Cache to the Vector Core.

Vector Core is the piece of Atalla's design that will change the most in the next iteration of updates during next semester. We want to be able to simulate the state-of-the-art design and have a base from how the design can be improved in order to have a better performance

Also, the Cycle-Accurate Simulator will now be purely in Python, so we can have a better development time, better support from AI tools and we can expect newcomers to know Python

### Atalla-Sim

Started coding the skeleton for the core classes for Atalla-Sim

#### Event and Event Queue

```python
class Event:
    time: Time
    callback: Callable[..., Any]
    args: Tuple[Any, ...] = ()
    kwargs: dict = None
    cancelled: bool = False


class EventQueue:
    def now(self) -> Time:
        pass

    def schedule(self, time: Time, callback: Callable[..., Any], *args, **kwargs) -> EventHandle:
        pass

    def cancel(self, handle: EventHandle) -> bool:
        pass

    def run_until(self, time: Time) -> None:
        pass

    def run_all(self) -> None:
        pass
```

Central scheduler for all simulation events (ticks, updates, device actions).

- now(): Return the current simulation time.
- schedule(time, callback, *args, **kwargs): Schedule a callback to run at a future time; return a handle for cancellation.
- cancel(handle): Cancel a previously scheduled event.
- run_until(time): Process all events up to the given time.
- run_all(): Process all events until the queue is empty.

#### Clock Domain

```python
class ClockDomain:

    def __init__(self, event_queue: EventQueue, period: Time, name: str = "clk") -> None:
        pass

    def add_clocked(self, obj: Clocked) -> None:
        pass

    def remove_clocked(self, obj: Clocked) -> None:
        pass

    def __Tick(self, time: Time) -> None:
        pass

    def schedule_next(self, time: Time) -> None:
        pass
```

Drives a group of synchronous devices (Clocked objects) at a fixed period.

- __init__(event_queue, period, name): Store references, initialize clocked list, and schedule first tick.
- add_clocked(obj): Register a device to be ticked by this domain.
- remove_clocked(obj): Unregister a device.
- __Tick(time): Called by the event queue; calls tick(time) and update() on all registered devices, then schedules the next tick.
- schedule_next(time): Schedules the next clock tick at time + period using the event queue.

#### Clocked

```python
class Clocked:
    def __Tick(self, time: Time)-> None:
        pass

    def __update(self, time: Time)-> None:
        pass
```

Base class for synchronous devices (latches, registers, cores).

- tick(time): Perform all work that must happen on the clock edge (sample inputs, compute outputs).
- update(): Apply state changes after all ticks in the cycle (two-phase update).

#### Core

```python
class Core:

    def __init__(self, event_queue: EventQueue) -> None:
        pass

    def add_clock_domain(self, domain: ClockDomain) -> None:
        pass
    
    def reset(self) -> None:
        pass
```

Top-level container for simulation components and clock domains.

- __init__(event_queue): Store event queue, initialize clock domains list.
- add_clock_domain(domain): Register a new clock domain.
- reset(): Reset all domains and devices to initial state.

#### Sim
```python
class Sim:
    def __init__(self) -> None:
        pass

    def init(self, event_queue: EventQueue, core: Core) -> None:
        pass

    def run(self, until: Optional[Time] = None) -> None:
        pass

    def stop(self) -> None:
        pass
```

Simulation manager; orchestrates event queue and core, provides run/stop.

- __init__(): Initialize simulation state.
- init(event_queue, core): Set up the event queue and core.
- run(until=None): Run the simulation until a given time or until all events are processed.
- stop(): Stop the simulation (set running flag, cancel outstanding events).

## Next Steps
- Understand the Lookup-Free Cache RTL (11/02)
- ~Start modelling in C++ (11/04)~
- Start modelling in Python (11/04)
- Understand Vector Core RTL (11/04 - 11/09)
