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


def safe(report: list[int]) -> bool:
    def pairwise(a: int, b: int) -> bool:
        return 1 <= abs(a - b) <= 3

    all_increasing = report == sorted(report)
    all_decreasing = report == sorted(report, reverse=True)
    pairwise_diffs = all(map(pairwise, report[:-1], report[1:]))

    return (all_increasing or all_decreasing) and pairwise_diffs


print("Part 1:", sum(map(safe, reports)))


def safe2(report: list[int]) -> bool:
    reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
    return any(safe(r) for r in reports)


print("Part 2:", sum(map(safe2, reports)))
