import pathlib
from collections import Counter

from src.utils import lmap, lzip


with pathlib.Path("src/day01/input.txt").open() as f:
    lines = f.read().splitlines()


left = [int(left) for left, _ in [line.split() for line in lines]]
right = [int(right) for _, right in [line.split() for line in lines]]

# Part 1

dists = lmap(lambda t: abs(t[0] - t[1]), lzip(sorted(left), sorted(right)))
print("Part 1:", sum(dists))

# Part 2

counts = Counter(right)
similarity = lmap(lambda val: val * counts.get(val, 0), left)
print("Part 2:", sum(similarity))
