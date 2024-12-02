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
