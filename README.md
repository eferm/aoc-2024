## Setup
Copy session cookie from browser to `.env` as `SESSION`.

## Run

Download and bootstrap new day's puzzle:

```shell
uv run --env-file .env src/cli.py 1
```

```shell
env $(cat .env | xargs) bootstrap 1
```

Run a puzzle script:

```shell
uv run src/day01/main.py
```

Or in VSCode: _> Python: Run Python File_.
