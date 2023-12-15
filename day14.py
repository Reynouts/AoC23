from aocutils import *


def score_rounds(rounds, h):
    score = 0
    for r in rounds:
        score += h-r[1]
    return score


def tilt(rounds, cubes, w, h):
    # very slow...
    new_rounds = set()
    for x in range(w):
        potential = h
        for y in range(h):
            if (x,y) in rounds:
                new_rounds.add((x, h-potential))
                potential -= 1
            if (x,y) in cubes:
                potential = h-y-1
    return new_rounds


def rotate(rounds, cubes, h):
    new_rounds = [(h-1-y, x) for (x, y) in rounds]
    new_cubes = [(h-1-y, x) for (x, y) in cubes]
    return new_rounds, new_cubes


def quarter(rounds, cubes, w, h):
    rounds = tilt(rounds, cubes, w, h)
    rounds, cubes = rotate(rounds, cubes, h)
    return rounds, cubes, h, w


def cycle(rounds, cubes, w, h):
    for _ in range(4):
        rounds, cubes, w, h = quarter(rounds, cubes, w, h)
    return rounds, cubes, score_rounds(rounds, h)


def get_cycle_length(cubes, h, rounds, w):
    # should have checked the set of rounds instead of score..
    # but it works (slowly)
    scores = []
    pot_cycles = []
    visited = set()
    for x in range(1000):
        rounds, cubes, score = cycle(rounds, cubes, w, h)
        scores.append(score)
        print(score)
        if score in scores and score not in visited:
            for i in range(0, len(scores) - 2):
                if scores[i] == scores[-1]:
                    pot_cycle = len(scores) - 1 - i
                    pot_cycles.append((pot_cycle, i))
                    visited.add(score)
                    if len(pot_cycles) > 3 and pot_cycles[-1][0] == pot_cycles[-2][0]:
                        print(pot_cycles)


def main():
    with open(txt(), 'r') as f:
        lines = f.read().split('\n')

    rounds = set()
    cubes = set()
    w = len(lines[0])
    h = len(lines)
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == "#":
                cubes.add((x,y))
            if cell == "O":
                rounds.add((x,y))
    cl, start = get_cycle_length(cubes, h, rounds, w)

    nth = (1000000000-start)%cl

    for _ in range(nth+start):
        rounds, cubes, score = cycle(rounds, cubes, w, h)
    print(score)





if __name__ == "__main__":
    main()
