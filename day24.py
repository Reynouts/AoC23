from aocutils import *
import re
import sympy


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def line_intersection(s1, s2):
    x, y, _, vx, vy, _ = s1
    l1 = ((x, y), (x + vx, y + vy))
    x, y, _, vx, vy, _ = s2
    l2 = ((x, y), (x + vx, y + vy))
    xdiff = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
    ydiff = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

    div = det(xdiff, ydiff)
    if div == 0:
        return None, None

    d = (det(*l1), det(*l2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if future_check(x, s1) and future_check(x, s2):
        return x, y
    return None, None


def future_check(t, s):
    x, _, _, vx, _, _ = s
    return (t - x) / vx >= 0


def main():
    with open(txt(), 'r') as f:
        stones = [tuple(map(int, re.findall("-?\d+", line))) for line in f.readlines()]

    limits = 200000000000000, 400000000000000

    count = 0
    for i, s1 in enumerate(stones):
        for j, s2 in enumerate(stones[:i]):
            x, y = line_intersection(s1, s2)
            if x and  limits[0] <= x <= limits[1] and limits[0] <= y <= limits[1]:
                count += 1
    print("p1:", count)

    x, y, z, vx, vy, vz = sympy.symbols("x, y, z, vx, vy, vz")
    eqs = []
    for i, s in enumerate(stones[:3]):
        x_, y_, z_, vx_, vy_, vz_ = s
        eqs.append((x - x_) * (vy_ - vy) - (y - y_) * (vx_ - vx))
        eqs.append((y - y_) * (vz_ - vz) - (z - z_) * (vy_ - vy))

    results = sympy.solve(eqs)
    for r in results:
        if (r[x] + r[y] + r[z]) % 1 == 0:
            print("p2:", r[x] + r[y] + r[z])
            break


if __name__ == "__main__":
    main()
