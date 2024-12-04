from collections import Counter
from collections.abc import Callable, Generator
from itertools import product

from src.utils import get_input, preview


inp = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""  # Example
inp = get_input(4, 2024)

lines = inp.splitlines()
# preview(lines, n=10)

R = len(lines)
C = len(lines[0])
# print(R, C)


def contained(v: list[tuple[int, int]]) -> bool:
    return all(0 <= r < R and 0 <= c < C for r, c in v)


def candidates(row: int, col: int) -> list[list[tuple[int, int]]]:
    possible = [
        # Horizontal
        [(row, col + d) for d in range(4)],
        [(row, col - d) for d in range(4)],
        # Vertical
        [(row + d, col) for d in range(4)],
        [(row - d, col) for d in range(4)],
        # Diagonal
        [(row + d, col + d) for d in range(4)],
        [(row + d, col - d) for d in range(4)],
        [(row - d, col + d) for d in range(4)],
        [(row - d, col - d) for d in range(4)],
    ]

    return [v for v in possible if contained(v)]


def translate(l: list[tuple[int, int]]) -> str:
    return "".join([lines[r][c] for r, c in l])


total = 0

for row in range(R):
    for col in range(C):
        if lines[row][col] == "X":
            for v in candidates(row, col):
                if translate(v) == "XMAS":
                    total += 1

print("Part 1:", total)


def candidates2(row: int, col: int) -> list[list[tuple[int, int]]]:
    possible = [
        # Diagonal
        [(row + d, col + d) for d in range(3)],
        [(row + d, col - d) for d in range(3)],
        [(row - d, col + d) for d in range(3)],
        [(row - d, col - d) for d in range(3)],
    ]

    return [v for v in possible if contained(v)]


def bbox(v: list[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    rs = [r for r, _ in v]
    cs = [c for _, c in v]
    return (min(rs), min(cs)), (max(rs), max(cs))


boxes: list[tuple[tuple[int, int], tuple[int, int]]] = []

for row in range(R):
    for col in range(C):
        if lines[row][col] == "M":
            for v in candidates2(row, col):
                if translate(v) == "MAS":
                    boxes.append(bbox(v))
                    # print(translate(v), v, bbox(v))


print("Part 2:", len([k for k, v in Counter(boxes).items() if v == 2]))
