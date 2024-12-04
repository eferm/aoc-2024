from collections import Counter
from collections.abc import Generator
from functools import partial
from itertools import product

from src.utils import get_input


inp = get_input(4, 2024)
lines = inp.splitlines()

R = len(lines)
C = len(lines[0])

type coord = tuple[int, int]
type vector = list[coord]


def vectors(length: int, mask: list[int], origin: coord) -> Generator[vector]:
    row, col = origin
    for rm, cm in product(mask, repeat=2):  # (0,0), (0,1), (1,0), (1,1), ...
        v = [(row + step * rm, col + step * cm) for step in range(length)]
        if all(0 <= r < R and 0 <= c < C for r, c in v):  # Contained in box
            yield v


def coords(char: str) -> Generator[coord]:
    for row, col in product(range(R), range(C)):
        if lines[row][col] == char:
            yield row, col


def string(v: vector) -> str:
    return "".join([lines[r][c] for r, c in v])


vectors1 = partial(vectors, 4, [-1, 0, 1])  # Diag, vert, hori
total = 0

for row, col in coords("X"):
    for v in vectors1((row, col)):
        total += string(v) == "XMAS"

print("Part 1:", total)


def bbox(v: vector) -> tuple[coord, coord]:  # (min coord, max coord)
    rs = [r for r, _ in v]
    cs = [c for _, c in v]
    return (min(rs), min(cs)), (max(rs), max(cs))


vectors2 = partial(vectors, 3, [-1, 1])  # Diag
boxes: Counter[tuple[coord, coord]] = Counter()

for row, col in coords("M"):
    for v in vectors2((row, col)):
        if string(v) == "MAS":
            boxes[bbox(v)] += 1


print("Part 2:", len([k for k, count in boxes.items() if count == 2]))
