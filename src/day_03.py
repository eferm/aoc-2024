import re

from src.utils import get_input


inp = get_input(3, 2024)
tape = re.findall(r"(do|don't|mul)\((?:(\d{1,3}),(\d{1,3}))?\)", inp)

prods = [int(a) * int(b) for _, a, b in tape if a and b]
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
