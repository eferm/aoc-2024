import re

from src.utils import get_input


inp = get_input(3, 2024)
tape = re.findall(r"(do|don't|mul)\((?:(\d{1,3}),(\d{1,3}))?\)", inp)

prods = [int(a) * int(b) for op, a, b in tape if op == "mul"]
print("Part 1:", sum(prods))


flag = 1
total = 0

for instr in tape:
    match instr:
        case ("do", *_):
            flag = True
        case ("don't", *_):
            flag = False
        case ("mul", a, b):
            total += flag * int(a) * int(b)
        case _:
            raise ValueError(instr)

print("Part 2:", total)


# Alternative for using reduce()
# Explored passing "state" in the sign of the accumulated value


def parse(total: int, instr: tuple[str, str, str]) -> int:
    match instr:
        case ("do", *_):
            return abs(total)
        case ("don't", *_):
            return -abs(total)  # Use sign to store state
        case ("mul", a, b):
            return total + int(a) * int(b) if total > 0 else total
        case _:
            raise ValueError(instr)


# from functools import reduce
# prod = reduce(parse, tape, 1) - 1  # Offset to allow flipping sign
# print("Part 2:", prod)
