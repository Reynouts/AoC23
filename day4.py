from aocutils import *
import re
from collections import defaultdict


def main():
    with open(txt(), 'r') as f:
        cards = f.read().split('\n')
    p1 = 0
    copies = defaultdict(int)
    for i, card in enumerate(cards):
        x, y = card.split(": ")[1].split(" | ")
        x = set(map(int, re.findall("-?\d+", x)))
        y = set(map(int, re.findall("-?\d+", y)))
        bingo = len(x.intersection(y))
        # p1
        p1 += 2 ** (bingo - 1)
        # p2
        for _ in range(copies[i] + 1):
            for j in range(bingo):
                copies[j + i + 1] += 1
    print(f'p1: {int(p1)}')
    print(f'p2: {sum(copies.values()) + len(cards)}')


if __name__ == "__main__":
    main()
