from aocutils import *
import re
import math


def p1(current, g, instruction):
    steps = 0
    dir = {"L": 0, "R": 1}
    while current[-1] != "Z":
        for c in instruction:
            current = g[current][dir[c]]
            steps += 1
    return steps


def main():
    with open(txt(), 'r') as f:
        instruction, _, *graph = f.read().split('\n')
    g = {}
    for line in graph:
        fr, left, right = re.findall("\d*[A-Z]+", line)
        g[fr] = (left, right)
    print(f'p1: {p1("AAA", g, instruction)}')
    starts = {n: n for n in g if n[-1] == "A"}
    print(f'p2: {math.lcm(*[p1(s, g, instruction) for s in starts])}')


if __name__ == "__main__":
    main()
