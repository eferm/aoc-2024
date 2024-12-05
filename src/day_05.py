from graphlib import TopologicalSorter

from src.utils import get_input


inp = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
inp = get_input(5, 2024)

section1, section2 = inp.split("\n\n")

updates = [list(map(int, p.split(","))) for p in section2.splitlines()]
rules = [tuple(map(int, r.split("|"))) for r in section1.splitlines()]

priors: dict[int, list[int]] = {}
afters: dict[int, list[int]] = {}

for l, r in rules:
    afters.setdefault(l, []).append(r)
    priors.setdefault(r, []).append(l)

middle: list[int] = []

for update in updates:
    valid = True
    for i in range(len(update)):
        prior, this, after = update[:i], update[i], update[i + 1 :]
        for p in prior:
            if p in afters.get(this, []):
                valid = False
                break
        for a in after:
            if a in priors.get(this, []):
                valid = False
                break

    if valid:
        mid = len(update) // 2
        middle.append(update[mid])

print("Part 1:", sum(middle))


middles: list[int] = []

for update in updates:
    sorter: TopologicalSorter[int] = TopologicalSorter()
    for pre, node in rules:
        if node in update:  # Only add relevant nodes to avoid cycles
            sorter.add(node, pre)
    ordering = list(sorter.static_order())
    idxs = [ordering.index(page) for page in update]
    if sorted(idxs) != idxs:  # Incorrectly ordered
        correct = [o for o in ordering if o in update]
        mid = len(correct) // 2
        middles.append(correct[mid])

print("Part 2:", sum(middles))
