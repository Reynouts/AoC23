from aocutils import *
import re
from functools import lru_cache


@lru_cache
def check(s, numbers):
    if s == "":
        return 1 if len(numbers) == 0 else 0
    if len(numbers) == 0:
        return 0 if "#" in s else 1

    if s[0] == ".":
        return check(s[1:], numbers)
    elif s[0] == "?":
        return check("." + s[1:], numbers) + check("#" + s[1:], numbers)
    elif s[0] == "#":
        if len(s) < numbers[0] or "." in s[:numbers[0]]:
            return 0
        if len(s) > numbers[0]:
            return 0 if s[numbers[0]] == "#" else check(s[numbers[0] + 1:], numbers[1:])
        return check(s[numbers[0]:], numbers[1:])


def main():
    with open(txt(), 'r') as f:
        instructions = f.read().split('\n')
    p1, p2 = 0, 0
    for instruction in instructions:
        i, numbers = instruction.split(" ")
        numbers = list(map(int, re.findall("\d+", numbers)))
        p1 += check(i, tuple(numbers))
        p2 += check(i + (("?" + i) * 4), tuple(numbers * 5))
    print(f'p1: {p1}')
    print(f'p2: {p2}')


if __name__ == "__main__":
    main()
