import re
from collections import defaultdict


def intersects(b1, b2):
    return max(b1[0], b2[0]) <= min(b1[3], b2[3]) \
            and max(b1[1], b2[1]) <= min(b1[4], b2[4])


def checkfall(supporting, supported, n, falling):
    if n in falling:
        return 0
    falling.add(n)
    return sum(1 + checkfall(supporting, supported, i, falling)
               for i in supporting[n] if not supported[i] - falling)


def main():
    with open("day22.txt", 'r') as f:
        blocks = [list(map(int, re.findall("\d+", line))) for line in f.read().split('\n')]
    blocks.sort(key=lambda b: b[2])

    for i, b1 in enumerate(blocks):
        z = 1
        for b2 in blocks[:i]:
            if intersects(b1, b2):
                z = max(z, b2[5] + 1)
        b1[5] += z - b1[2]
        b1[2] = z

    supporting = defaultdict(set)
    supported = defaultdict(set)
    for j, b1 in enumerate(blocks):
        for i, b2 in enumerate(blocks[:j]):
            if intersects(b1, b2) and b1[2] == b2[5] + 1:
                supporting[i].add(j)
                supported[j].add(i)
    print("p1:", sum([1 for i, b in enumerate(blocks) if all(len(supported[j]) >= 2 for j in supporting[i])]))
    print("p2:", sum([checkfall(supporting, supported, i, set()) for i, _ in enumerate(blocks)]))


if __name__ == "__main__":
    main()
