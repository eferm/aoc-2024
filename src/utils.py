from __future__ import annotations

import argparse
import os
from pathlib import Path

import requests


YEAR = 2024

INPUT_URL = "https://adventofcode.com/{year}/day/{day}/input"

BOILERPLATE = '''\
from src.utils import get_input


inp = """\\
co py
pa ste
ex ample
"""
inp = get_input({year}, {day})

lines = inp.splitlines()
print(*lines[:10], sep="\\n")
'''


src_file = "src/year_{year}/day_{day:02}.py"
inp_file = "data/input_{year}-12-{day:02}.txt"


def get_input(year: int, day: int) -> str:
    target = Path(inp_file.format(year=year, day=day))
    if not target.exists():
        contents = fetch_input(year, day)
        target.write_text(contents)
    return target.read_text()


def fetch_input(year: int, day: int) -> str:
    print(f"Fetching input for {year=} {day=} from server...")
    resp = requests.get(
        INPUT_URL.format(year=year, day=day),
        headers={"Cookie": f"session={os.environ['SESSION']}"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.text


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int)
    parser.add_argument("-y", "--year", type=int, default=YEAR)

    args = parser.parse_args()

    target = Path(src_file.format(**vars(args)))
    if not target.exists():
        print(f"Seeding file {target}...")
        target.parent.mkdir(exist_ok=True)
        target.write_text(BOILERPLATE.format(**vars(args)))

    get_input(**vars(args))


if __name__ == "__main__":
    cli()
