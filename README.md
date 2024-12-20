## Rules

Some rules I follow for myself, optimizing for fun and learning:

- Standard library code only, no third-party dependencies*
  - I use `requests` for downloading puzzle inputs, but this is basically a first-party library anyway.
- In general I can use Google or LLM for _generic_ programming questions:
  - Look up docs, syntax, etc.
  - Basics I should know but always forget, e.g.:
    - "How to reverse a linked list in Python"
    - "How to breadth first search in Python"
  - I never Google for anything related to AoC or programming competitions.
- After solving and pushing a dirty but working solution I might revisit and clean things up. This may include edits based on someone else's solution I liked, but entire refactors would only be of my own design.
- (New for 2024) If I'm stuck on day X's problem, I'm allowed to skip ahead to day X+1 once that's released.
  - I can be severely nerd-sniped by unsolved problems and I'm unsure how to move past this; this remains an unsolved problem.


## Setup

Copy session cookie from browser to `.env` as `SESSION`.

To run things with env vars loaded:

- Run scripts with:
  ```shell
  uv run --env-file .env path/to/script.py
  ```

  ```shell
  env $(cat .env | xargs) python path/to/script.py
  ```

- Or, configure VSCode terminal with:
  ```json
  "python.experiments.optInto": ["pythonTerminalEnvVarActivation"]
  ```

Alternatively, manually download input files and save them to

```shell
data/input_{year}-{day:02}.txt
```

## Run

Download and bootstrap new day's puzzle:

```shell
bootstrap 1
```

```shell
uv run src/utils.py 1
```

Run a puzzle script:

```shell
uv run src/year_2024/day_01.py
```

Or in VSCode:

```
> Python: Run Python File
```

## Notes

### 2024

#### Day 1

Very easy. Had some fun setting up a fresh repo. Rewrote the solution a few times, experimenting with _not_ jumping to complex functional style solutions (`map`, `reduce`, etc), specifically forcing myself to write more loops.

One thing I learned was passing multiple iterables to `map`. E.g. these are equivalent:

```python
map(lambda odd, even: odd + even, [1, 3], [2, 4])
map(lambda t: t[0] + t[1], zip([1, 3], [2, 4]))
map(lambda t: t[0] + t[1], [(1, 2), (3, 4)])
```

Useful since Python 3 doesn't do tuple unpacking in lambdas.

Reflecting on last year, I got massively stuck on day 12. Not wanting to "cheat," nor jump ahead to day 13 onwards, I abandoned AoC entirely for the year. That seems suboptimal, so this year I'll allow myself to skip past days I'm stuck on once a new day unlocks.

#### Day 2

Easy. One realization was that you can use `map` with list slices to implement `itertools.pairwise`. So:

```python
>>> seq = [1, 2, 3, 4, 5]
>>> list(map(lambda a, b: (a, b), seq[:-1], seq[1:]))
[(1, 2), (2, 3), (3, 4), (4, 5)]

>>> from itertools import pairwise
>>> list(pairwise([1, 2, 3, 4, 5]))
[(1, 2), (2, 3), (3, 4), (4, 5)]
```

#### Day 3

Easy. Part 1 being an obvious regex problem, my immediate thought was whether part 2 would contain a gotcha in which regexes would turn out to _not_ work. Heh.

I experimented a bit with what it would look like to replace the part 2 instruction-eval loop with a function. It's not a straightforward `map` or `reduce` since each iteration depends on state (`do()` / `don't()`) set by previous instructions. However, state being so minimal (a boolean) I figured `reduce` might work anyway, and we can use the sign of the accumulated value as a flag:

```python
from functools import reduce

def parse(total: int, instr: tuple[str, str, str]) -> int:
    match instr:
        case ("do", *_):
            return abs(total)
        case ("don't", *_):
            return -abs(total)  # Store state in sign
        case ("mul", a, b):
            return total + int(a) * int(b) if total > 0 else total
        case _:
            raise ValueError(instr)

print(reduce(parse, tape, 1) - 1)  # Initial 1 to allow flipping sign
```

While this works I'm not sure it's preferred in any way over a simple loop! For a similar but less hacky approach can also make the accumulator value a tuple of `(flag, total)`, with initial value `(True, 0)`.

Further mini learning: you can transpose a matrix (list of lists) with `list(zip(*matrix))`. So say you have a list of tuples (in today's puzzle this was (a, b) extracted from each `mul(a,b)`), and you want each tuple to be the input to some function `f(a, b)`:

```python
>>> ts = [(1, 2), (3, 4), (5, 6), (7, 8)]

>>> list(map(lambda a, b: a * b, *zip(*ts)))  # This is pretty nice!
[2, 12, 30, 56]

>>> list(map(lambda t: t[0] * t[1], ts))  # Eww no tuple unpacking
[2, 12, 30, 56]
```

Inspecting various ways of passing arguments to a lambda in `map`:

```python
# 1 param, each a 2-tuple -> 4 items
>>> list(map(lambda t2: t2, ts))
[(1, 2), (3, 4), (5, 6), (7, 8)]

# 2 params, each an int -> 4 items
>>> list(map(lambda a, b: (a, b), *zip(*ts)))
[(1, 2), (3, 4), (5, 6), (7, 8)]

# 1 param, each a 4-tuple -> 2 items
>>> list(map(lambda t4: t4, zip(*ts)))
[(1, 3, 5, 7), (2, 4, 6, 8)]

# 4 params, each an int -> 2 items
>>> list(map(lambda a, b, c, d: (a, b, c, d), *ts))
[(1, 3, 5, 7), (2, 4, 6, 8)]
```
