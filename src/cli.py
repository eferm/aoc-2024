"""Download input file and create boilerplate."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import requests


YEAR = 2024
URL = "https://adventofcode.com/{year}/day/{day}/input"
TEMPLATE = """\
import pathlib

from src.utils import lprint


with pathlib.Path("{folder}/input.txt").open() as f:
    lines = f.read().splitlines()

lprint(lines[:10])
"""


def bootstrap() -> None:
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("day", type=int)
    parser.add_argument("-y", "--year", type=int, default=YEAR)

    args = parser.parse_args()

    folder = Path("src") / f"day{args.day:02}"
    folder.mkdir(parents=True, exist_ok=True)

    if not (f := folder / "main.py").exists():
        print(f"Seeding file {f}...")
        f.write_text(TEMPLATE.format(folder=folder))

    if not (f := folder / "input.txt").exists():
        f.write_text(get_input(args.year, args.day))

    folder.joinpath("example1.txt").touch()
    folder.joinpath("example2.txt").touch()


def get_input(year: int, day: int) -> str:
    print(f"Fetching input for {year=} {day=} from server...")
    resp = requests.get(
        URL.format(year=year, day=day),
        headers={"Cookie": f"session={os.environ['SESSION']}"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.text


if __name__ == "__main__":
    bootstrap()
