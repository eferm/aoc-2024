import re

from src.utils import get_input


inp = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""  # Part 1
inp = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""  # Part 2
inp = get_input(3, 2024)

# Part 1

strings = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)

muls = map(lambda a, b: int(a) * int(b), *zip(*strings, strict=True))
print("Part 1:", sum(muls))

# Part 2

tape = re.findall(r"(do|don't|mul)\((?:(\d{1,3}),(\d{1,3}))?\)", inp)

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
