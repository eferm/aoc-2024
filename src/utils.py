from __future__ import annotations

import os
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests


YEAR = 2024

INP_URL = "https://adventofcode.com/{year}/day/{day}/input"

INP_FILENAME = "data/input_{year}-12-{day:02}.txt"
SRC_FILENAME = "src/year_{year}/day_{day:02}.py"

SRC_TEMPLATE = '''\
from src.utils import get_input


inp = """\\
co py
pa ste
ex ample
"""
inp = get_input({day}, {year})

lines = inp.splitlines()
print(*lines[:10], sep="\\n")
'''


def get_input(day: int, year: int) -> str:
    target = Path(INP_FILENAME.format(year=year, day=day))
    if not target.exists():
        contents = fetch_input(day, year)
        target.write_text(contents)
    return target.read_text()


def fetch_input(day: int, year: int) -> str:
    if not is_past_midnight(day):
        msg = "It's not midnight yet."
        raise ValueError(msg)

    print(f"Fetching input for {year=} {day=} from server...")
    resp = requests.get(
        INP_URL.format(year=year, day=day),
        headers={"Cookie": f"session={os.environ['SESSION']}"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.text


def cli() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int)
    parser.add_argument("-y", "--year", type=int, default=YEAR)

    args = parser.parse_args()

    target = Path(SRC_FILENAME.format(**vars(args)))
    if not target.exists():
        print(f"Seeding file {target}...")
        target.parent.mkdir(exist_ok=True)
        target.write_text(SRC_TEMPLATE.format(**vars(args)))

    get_input(**vars(args))


def is_past_midnight(day: int, month: int = 12, year: int = YEAR) -> bool:
    """True if it's year-month-day, or later, in Eastern Time."""
    tz = ZoneInfo("America/New_York")
    return datetime.now(tz) >= datetime(year, month, day, tzinfo=tz)


if __name__ == "__main__":
    cli()
