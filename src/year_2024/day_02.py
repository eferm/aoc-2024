from src.utils import get_input


inp = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
inp = get_input(2, 2024)
lines = inp.splitlines()


def parse(line: str) -> list[int]:
    levels = line.split()
    return list(map(int, levels))


reports = list(map(parse, lines))


def safe(levels: list[int]) -> bool:
    def pairwise(a: int, b: int) -> bool:
        return 1 <= abs(a - b) <= 3

    all_increasing = levels == sorted(levels)
    all_decreasing = levels == sorted(levels, reverse=True)
    pairwise_diffs = all(map(pairwise, levels[:-1], levels[1:]))

    return (all_increasing or all_decreasing) and pairwise_diffs


print("Part 1:", sum(map(safe, reports)))


def safe2(levels: list[int]) -> bool:
    def permutations(levels: list[int]):
        for i in range(len(levels)):
            yield [l for j, l in enumerate(levels) if i != j]

    return any(safe(p) for p in permutations(levels))


print("Part 2:", sum(map(safe2, reports)))
