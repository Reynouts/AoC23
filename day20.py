from aocutils import *
import copy
from math import lcm


def process(signal, sender, destination, modules):
    if destination in ("rx", "output"):
        return []
    if destination == "broadcaster":
        return [[0, destination, d] for d in modules[destination][1]]
    if modules[destination][0] == "%" and signal == 0:
        modules[destination][2] = 1 - modules[destination][2]
        return [(modules[destination][2], destination, d) for d in modules[destination][1]]
    elif modules[destination][0] == "&":
        modules[destination][-1][sender] = signal
        flipped = int(not all([modules[destination][-1][s] for s in modules[destination][-1]]))
        return [(flipped, destination, d) for d in modules[destination][1]]


def main():
    with open(txt(), 'r') as f:
        rules = f.read().split('\n')

    modules = {}
    cons = []
    for rule in rules:
        name, destinations_str = rule.split(" -> ")
        t = name[0]
        name = name if name == "broadcaster" else name[1:]
        destinations = destinations_str.split(", ")
        modules[name] = [t, destinations, 0]
        if t == "&":
            cons.append(name)
        if "rx" in destinations:
            prev = name  # assuming only one connection to rx (con)

    for module_key in modules:
        for cons_key in cons:
            if len(modules[cons_key]) == 3:
                modules[cons_key].append({})
            if cons_key in modules[module_key][1]:
                modules[cons_key][3][module_key] = 0

    low, high = 0, 0
    cons = copy.deepcopy(modules[prev][-1])
    for press in range(10**10):
        if press == 1000:
            print("p1:", low*high)
        q = [(0, "", "broadcaster")]
        while q:
            if all(cons[v] != 0 for v in cons):
                print("p2:", lcm(*cons.values()))
                return
            for n in modules[prev][-1]:
                if modules[prev][-1][n] == 1 and cons[n] == 0:
                    cons[n] = press+1
            current = q.pop(0)
            low += current[0] == 0
            high += current[0] != 0
            calls = process(*current, modules)
            if calls:
                q.extend(calls)


if __name__ == "__main__":
    main()