from aocutils import *


def check_tile(beam, c):
    p, h = beam
    if c == ".":
        return beam,
    if c == "/":
        return [p, (-h[1], -h[0])],
    if c == "\\":
        return [p, (h[1], h[0])],
    if c == "-":
        return (beam,) if h in ((1, 0), (-1, 0)) else ([p, (1, 0)], [p, (-1, 0)])
    if c == "|":
        return (beam,) if h in ((0, 1), (0, -1)) else ([p, (0, 1)], [p, (0, -1)])


def energize(start, grid):
    beams = check_tile(start, grid[start[0][1]][start[0][0]])
    visited = {tuple(start)}
    while beams:
        new_beams = []
        for b in beams:
            b[0] = tuple(sum(pair) for pair in zip(*b))
            if 0 <= b[0][0] < len(grid[0]) and 0 <= b[0][1] < len(grid):
                beam_tuple = tuple(b)
                if beam_tuple not in visited:
                    visited.add(beam_tuple)
                    new_beams.extend(check_tile(b, grid[b[0][1]][b[0][0]]))
        beams = new_beams
    return len({v[0] for v in visited})


def main():
    grid = get_gridfromfile(txt())
    print (f'p1: {energize([(0,0), (1,0)], grid)}')
    config = 0
    for start in range(len(grid[0])):
        config = max(config, energize([(start, 0), (0, 1)], grid), energize([(start, len(grid)-1), (0, -1)], grid))
    for start in range(len(grid)):
        config = max(config, energize([(0, start), (1, 0)], grid), energize([(len(grid[0])-1, start), (-1, 0)], grid))
    print(f'p2: {config}')

if __name__ == "__main__":
    main()
