with open("src/day01/input.txt") as f:
    lines = f.read().splitlines()


def split(line: str) -> tuple[int, int]:
    a, b = line.split(maxsplit=1)
    return int(a), int(b)


splits = map(split, lines)
left, right = map(sorted, zip(*splits, strict=True))

# Part 1

distances = map(lambda a, b: abs(a - b), left, right)
print("Part 1:", sum(distances))

# Part 2

similarities = (l * right.count(l) for l in left)
print("Part 2:", sum(similarities))
