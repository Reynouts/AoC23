from aocutils import *


def main():
    with open(txt(), 'r') as f:
        lines = [list(map(int, line.split())) for line in f.read().split('\n')]

    p1, p2 = 0, 0
    for line in lines:
        seqs = [line]
        while any(e != 0 for e in seqs[-1]):
            seqs.append([seqs[-1][i] - seqs[-1][i-1] for i in range(1, len(seqs[-1]))])

        p1_last, p2_last = 0, 0
        for r in reversed(seqs[:-1]):
            p1_last = r[-1] + p1_last
            p2_last = r[0] - p2_last
        p1 += p1_last
        p2 += p2_last

    print(f"p1: {p1}")
    print(f"p2: {p2}")


if __name__ == "__main__":
    main()
