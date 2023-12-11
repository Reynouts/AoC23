from aocutils import *
from itertools import combinations


def main():
    grid = get_gridfromfile(txt())

    ys = {y for y, line in enumerate(grid) if all(e == "." for e in line)}
    xs = {x for x, line in enumerate(map(list, zip(*grid))) if all(e == "." for e in line)}
    points = {(x, y) for y, line in enumerate(grid) for x, e in enumerate(line) if e == "#"}

    total, add = 0, 0
    for p in combinations(points, 2):
        total += sum(abs(val1 - val2) for val1, val2 in zip(*p))
        add += sum(1 for x in range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0])) if x in xs)
        add += sum(1 for y in range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1])) if y in ys)

    print(f'p1: {total + add}')
    print(f'p2: {total + (add * 100000) - add}')


if __name__ == "__main__":
    main()
