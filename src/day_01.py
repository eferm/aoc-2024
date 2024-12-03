from src.utils import get_input


inp = get_input(1, 2024)
lines = inp.splitlines()


def split(line: str) -> tuple[int, int]:
    a, b = line.split(maxsplit=1)
    return int(a), int(b)


splits = map(split, lines)
left, right = map(sorted, zip(*splits, strict=True))

distances = map(lambda a, b: abs(a - b), left, right)
print("Part 1:", sum(distances))

similarities = (l * right.count(l) for l in left)
print("Part 2:", sum(similarities))
