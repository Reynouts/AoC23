from aocutils import *
from collections import defaultdict
from functools import reduce


def process(box, label, op, boxes):
    for i, lens in enumerate(boxes[box]):
        if lens[0] == label:
            if "=" in op:
                boxes[box][i][1] = int(op[1:])
            else:
                boxes[box].pop(i)
            break
    else:
        if "=" in op:
            boxes[box].append([label, int(op[1:])])
    return boxes



def main():
    with open(txt(), 'r') as f:
        seqs = f.read().split('\n')[0].split(",")

    print(f'p1: {sum(reduce(lambda h, c: ((ord(c) + h) * 17) % 256, seq, 0) for seq in seqs)}')

    boxes = defaultdict(list)
    for seq in seqs:
        offset = -2 if seq[-1].isdigit() else -1
        label, op = seq[:offset], seq[offset:]
        boxes = process(reduce(lambda acc, c: ((ord(c) + acc) * 17) % 256, label, 0), label, op, boxes)
    print(f'p2: {sum((1 + n) * (i + 1) * lens[1] for n, box in boxes.items() for i, lens in enumerate(box))}')


if __name__ == "__main__":
    main()
