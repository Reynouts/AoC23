from aocutils import *
import copy
from math import prod


def check_part(x, m, a, s, wfs):
    nxt = "in"
    while nxt not in ("A", "R"):
        r = wfs[nxt]
        for i in range(len(r)):
            if len(r[i]) == 1:
                nxt = r[i][0]
                break
            if eval(r[i][0]):
                nxt = r[i][1]
                break
    return nxt == "A"


def search(wfs):
    q = [("in", {c: [1, 4001] for c in "xmas"})]
    total = 0

    while q:
        current, ranges = q.pop(0)

        if current == "R":
            continue
        if current == "A":
            total += prod(ranges[r][1] - ranges[r][0] for r in ranges)
            continue

        for rule in wfs[current]:
            if len(rule) == 1:
                q.append((rule[0], copy.deepcopy(ranges)))
                continue
            condition, target = rule
            letter, value = condition[0], int(condition[2:])
            cranges = copy.deepcopy(ranges)
            if "<" in condition:
                cranges[letter][1] = min(cranges[letter][1], value)
                ranges[letter][0] = max(ranges[letter][0], value)
            elif ">" in condition:
                cranges[letter][0] = max(cranges[letter][0], value + 1)
                ranges[letter][1] = min(ranges[letter][1], value + 1)
            if all(r[0] < r[1] for r in cranges.values()):
                q.append((target, cranges))
    return total


def main():
    with open(txt(), 'r') as f:
        inputwfs, inputparts = f.read().split('\n\n')

    wfs = {}
    for wf in inputwfs.split("\n"):
        name, rules = wf[:-1].split("{")
        rules = [rule.split(":") for rule in rules.split(",")]
        wfs[name] = rules

    prts = []
    for prt in inputparts.split("\n"):
        x, m, a, s = map(int, re.findall("-?\d+", prt))
        prts.append({"x": x, "m": m, "a": a, "s": s})

    print(f'p1: {sum(sum(prt.values()) for prt in prts if check_part(*prt.values(), wfs))}')
    print(f'p2: {search(wfs)}')


if __name__ == "__main__":
    main()