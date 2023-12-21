def get_neighbours(c, cells):
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    return [pos for dx, dy in dirs if (pos := (c[0] + dx, c[1] + dy)) in cells]


def walk(cells, start, max_steps):
    plots = set()
    q = [(start, 0)]
    visited = set()
    while q:
        current, steps = q.pop(0)
        # dependent if max_steps is odd or even what is valid
        if steps % 2 == max_steps % 2:
            plots.add(current)
        if steps < max_steps:
            for nb in get_neighbours(current, cells):
                if nb not in visited:
                    visited.add(nb)
                    q.append((nb, steps + 1))
    return len(plots)


def main():
    cells = set()
    start = (0, 0)
    with open("day21.txt", 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, cell in enumerate(line.strip()):
                if cell in ".S":
                    cells.add((i, j))
                if cell == "S":
                    start = (i, j)
    length = i + 1

    print("p1:", walk(cells, start, 64))

    asked_steps = 26501365
    grid_repeats = (asked_steps - asked_steps % length) // length

    # Calculate for odd and even enterings from center point
    odd_grids = walk(cells, start, length * 2 + 1) * (((grid_repeats - 1) // 2) * 2 + 1) ** 2
    even_grids = walk(cells, start, length * 2) * ((grid_repeats // 2) * 2) ** 2

    # 4 corners of big diamond
    corner_steps = length - 1
    mid_enter_points = [(length // 2, length - 1), (length // 2, 0), (length - 1, length // 2), (0, length // 2)]
    corners = sum(walk(cells, pos, corner_steps) for pos in mid_enter_points)

    # diagonal parts (two distinct parts!)
    diagonal_small_steps = (length // 2) - 1
    diagonal_big_steps = length * 2 - 1 - length // 2 - 1
    corner_enter_points = [(length - 1, length - 1), (0, length - 1), (length - 1, 0), (0, 0)]
    small_diagonals = sum(walk(cells, pos, diagonal_small_steps) for pos in corner_enter_points) * grid_repeats
    big_diagonals = sum(walk(cells, pos, diagonal_big_steps) for pos in corner_enter_points) * (grid_repeats - 1)

    print("p2:", odd_grids + even_grids + corners + small_diagonals + big_diagonals)


if __name__ == "__main__":
    main()
