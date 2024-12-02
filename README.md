## Setup

Copy session cookie from browser to `.env` as `SESSION`.

To load env vars into the environment, do one of the following:

- Configure VSCode with:
  ```json
  "python.experiments.optInto": ["pythonTerminalEnvVarActivation"]
  ```

- Run scripts with:
  ```shell
  uv run --env-file .env path/to/script.py
  ```

  ```shell
  env $(cat .env | xargs) python path/to/script.py
  ```

Alternatively, manually download input files and save them to

```shell
data/input_{year}-{day:02}.txt
```

## Run

Download and bootstrap new day's puzzle:

```shell
uv run src/utils.py 1
```

```shell
bootstrap 1
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

```python-console
>>> map(lambda odd, even: odd + even, [1, 3], [2, 4])
>>> map(lambda t: t[0] + t[1], zip([1, 3], [2, 4]))
>>> map(lambda t: t[0] + t[1], [(1, 2), (3, 4)])
```

Useful since Python 3 doesn't do tuple unpacking in lambdas.

Reflecting on last year, I got massively stuck on day 12. Not wanting to "cheat," nor jump ahead to day 13 onwards, I abandoned AoC entirely for the year. That seems suboptimal, so this year I'll allow myself to skip past days I'm stuck on once a new day unlocks.

#### Day 2

Easy. One realization was that you can use `map` with list slices to implement `itertools.pairwise`. So:

```python-console
>>> seq = [1, 2, 3, 4, 5]
>>> list(map(lambda a, b: (a, b), seq[:-1], seq[1:]))
[(1, 2), (2, 3), (3, 4), (4, 5)]
>>> from itertools import pairwise
>>> list(pairwise([1, 2, 3, 4, 5]))
[(1, 2), (2, 3), (3, 4), (4, 5)]
```
