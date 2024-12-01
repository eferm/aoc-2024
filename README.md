## Setup

Copy session cookie from browser to `.env` as `SESSION`.

Load the env vars with one of:

- In VSCode set `"python.experiments.optInto": ["pythonTerminalEnvVarActivation"]`
- Run Python scripts with `uv run --env-file .env`
- Prefix commands with `env $(cat .env | xargs)`

## Run

Download and bootstrap new day's puzzle:

```shell
uv run src/utils.py 1
bootstrap 1
```

Run a puzzle script:

```shell
uv run src/year_2024/day_01.py
```

Or in VSCode: _> Python: Run Python File_.
