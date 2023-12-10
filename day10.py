from aocutils import *
from matplotlib import path as pt


def get_start(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                return x, y


def get_neighbours(cell, cells):
    neighbours = []
    heading = {(1, 0): ("-", "J", "7"),
               (-1, 0): ("-", "L", "F"),
               (0, 1): ("|", "L", "J"),
               (0, -1): ("|", "7", "F")}

    for dx, dy in heading:
        x, y = cell[0] + dx, cell[1] + dy
        if (0 <= x < len(cells[0])
                and 0 <= y < len(cells)
                and cells[y][x] in heading[(dx, dy)]):
            neighbours.append((x, y))
    return neighbours


def main():
    grid = get_gridfromfile(txt())
    start = get_start(grid)
    first, last = get_neighbours(start, grid)
    previous = start
    current = first

    directions = {"|": ((0, 1), (0, -1)),
                  "-": ((1, 0), (-1, 0)),
                  "J": ((-1, 0), (0, -1)),
                  "F": ((1, 0), (0, 1)),
                  "L": ((1, 0), (0, -1)),
                  "7": ((-1, 0), (0, 1))}
    heading = {(1, 0): ("-", "J", "7"),
               (-1, 0): ("-", "L", "F"),
               (0, 1): ("|", "L", "J"),
               (0, -1): ("|", "7", "F")}

    path = [start, current]
    while current != last:
        for d in directions[grid[current[1]][current[0]]]:
            pos = current[0] + d[0], current[1] + d[1]
            if (pos != previous
                  and 0 <= pos[0] < len(grid[0])
                  and 0 <= pos[1] < len(grid)
                  and grid[pos[1]][pos[0]] in heading[d]):
                previous, current = current, pos
                path.append(current)
                break

    print(f'p1: {(len(path)) // 2}')

    polygon = pt.Path(path)
    total = 0
    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            if (x, y) not in path and polygon.contains_point((x, y)):
                total += 1
    print(f'p2: {total}')


if __name__ == "__main__":
    main()
