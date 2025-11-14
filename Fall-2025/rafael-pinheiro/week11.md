State: I am not stuck with anything, don't need help right now.

I'm kinda cooked with 2 midterms next week, progress might be slow. I'll try to make more progress during thanksgiving

## Progress summary

Definition of core classes and most core methods done.

## Simulation Framework

The simulator is organized under `src/base` and provides reusable infrastructure for event-driven simulation, timing synchronization, and device scheduling.

## Core Classes

### Event Queue

The `EventQueue` is the heart of the event-based, cycle accurrate simulator — it schedules and executes timed callbacks in chronological order. Each event represents a hardware event (such as a tick, memory access, or pipeline action).

```python
Time = float
EventHandle = Tuple[Time, int]

class Event:
    time: Time
    callback: Callable[..., Any]
    args: Tuple[Any, ...] = ()
    kwargs: dict = None
    cancelled: bool = False


class EventQueue:
    def __init__(self):
        self._queue = []
        self._time = 0.0
        self._next_id = 0

    def now(self) -> Time:
        return self._time

    def schedule(self, time: Time, callback: Callable[..., Any], *args, **kwargs) -> EventHandle:
        handle = (time, self._next_id)
        heapq.heappush(self._queue, (time, self._next_id, callback, args, kwargs))
        self._next_id += 1
        return handle

    def run_until(self, time: Time) -> None:
        while (self._queue and self._queue[0][0] <= time):
            t, eid, callback, args, kwargs = heapq.heappop(self._queue)
            self._time = t
            callback(*args, **(kwargs or {}))
        self._time = time


    def run_all(self) -> None:
        while (self._queue and self._queue[0][0] >= 0):
            t, eid, callback, args, kwargs = heapq.heappop(self._queue)
            self._time = t
            callback(*args, **(kwargs or {}))
```

Purpose:
- Maintain global time simulation time
- Schedule and dispatch all component actions
- Enable cycle-by-cycle determinism and reproducibility

### Clock Domain

A `ClockDomain` drives synchronous components (`Clocked` objects) for a fixed period

It automatically schedules periodic ticks in the event queue and updates all attached devices

```python
class ClockDomain:

    def __init__(self, event_queue: EventQueue, period: Time, name: str = "clk") -> None:
        self.event_queue = event_queue
        self.period = period
        self.name = name
        self.objects = []
        self.next_time = 0.0

    def add_clocked(self, obj: Clocked) -> None:
        self.objects.append(obj)

    def remove_clocked(self, obj: Clocked) -> None:
        self.objects.remove(obj)

    def _Tick(self, time: Time) -> None:
        for obj in self.objects:
            obj._Tick(time)
        self.schedule_next(time)

    def schedule_next(self, time: Time) -> None:
        next_time = time + self.period
        self.event_queue.schedule(next_time, self._Tick, next_time)
```

Purpose:
- Group components that share the same clock
- Automaitcally propagate ticks at fixed intervals
- Support multiple asynchronous domains if needed (e.g. vector vs scalar domains)

### Clocked Objects

`Clocked` is the base class for all synchronous simulations devices. Each derived component (register files, buffers, latches) defines what happens on clock edges via its own `Tick()` method

```python
class Clocked:
    def _Tick(self, time: Time) -> None:
        print(f"{self.__class__.__name__} tick at {time}")
```

### Core and Sim

`Core` groups all clocked domains, while `Sim` controls global simulation flow

```python
class Core:

    def __init__(self, event_queue: EventQueue) -> None:
        self.event_queue = event_queue
        self.domains = []

    def add_clock_domain(self, domain: ClockDomain) -> None:
        self.domains.append(domain)
```

`Core` is the system-level container for all domains and devices. Links them to a single event queue

```python
class Sim:
    def __init__(self) -> None:
        self.event_queue = None
        self.core = None

    def init(self, event_queue: EventQueue, core: Core) -> None:
        self.event_queue = event_queue
        self.core = core

    def run(self, until: Optional[Time] = None) -> None:
        if until is None:
            self.event_queue.run_all()
        else:
            self.event_queue.run_until(until)
```

`Sim` is the entry poiny for running and stopping the simulation

## Next Steps

- Start modelling Vector Core's Register File (Veggie File) and Op Buffer (OpEater)