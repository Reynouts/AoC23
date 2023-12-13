from aocutils import *


def check_syn(p, i):
    for x in range(1, i + 1):
        if i + 1 + x == len(p):
            return True
        if p[i - x] != p[i + 1 + x]:
            return False
    return True


def get_mirror_index(p, original=0):
    m = 1
    for v in ([''.join(pair) for pair in zip(*p)], p):
        for i in range(len(v) - 1):
            if v[i] == v[i + 1] and check_syn(v, i):
                if original == 0 or original != (i + 1) * m:
                    return (i + 1) * m
        m *= 100
    return 0


def main():
    with open(txt(), 'r') as f:
        patterns = [p.split("\n") for p in f.read().split('\n\n')]

    indices = [get_mirror_index(p) for p in patterns]
    print(f'p1: {sum(indices)}')

    p2_indices = []
    for dex, p in enumerate(patterns):
        for pos in range(len(p[0])):
            found = False
            for i in range(len(p)):
                if pos >= len(p[i]):
                    break
                modified_p = [list(line) for line in p]
                modified_p[i][pos] = '#' if p[i][pos] == '.' else '.'
                modified_p = [''.join(line) for line in modified_p]
                index = get_mirror_index(modified_p, indices[dex])
                if index != 0:
                    p2_indices.append(index)
                    found = True
                    break
            if found:
                break
    print(f'p2: {sum(p2_indices)}')


if __name__ == "__main__":
    main()
