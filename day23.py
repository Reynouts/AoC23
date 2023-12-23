from aocutils import *
from collections import deque
from collections import defaultdict


def get_neighbours(c, cells, chars="."):
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    if cells[c] in chars:
        return [pos for dx, dy in dirs if (pos := (c[0] + dx, c[1] + dy)) in cells]
    nbs = []
    if cells[c] == ">":
        nbs.append((c[0] + 1, c[1]))
    elif cells[c] == "<":
        nbs.append((c[0] - 1, c[1]))
    elif cells[c] == "v":
        nbs.append((c[0], c[1] + 1))
    elif cells[c] == "^":
        nbs.append((c[0], c[1] - 1))
    return nbs


def search(start, end, cells, chars="."):
    steps = 0
    visited = {start}
    q = deque()
    q.append((start, steps, visited.copy()))

    while q:
        current, steps, visited = q.popleft()
        if current == end:
            p1 = steps
        for nb in get_neighbours(current, cells, chars):
            if nb not in visited:
                c_visited = visited.copy()
                c_visited.add(nb)
                q.append((nb, steps + 1, c_visited))
    return p1


def get_junctions(cells):
    junctions = set()
    for c in cells:
        nbs = get_neighbours(c, cells, "v^<>.")
        if len(nbs) > 2:
            junctions.add(c)
    return junctions


def create_graph(junctions, cells):
    graph = defaultdict(list)
    for j in junctions:
        steps = 0
        q = [j]
        visited = {j}
        while q:
            cq = []
            steps += 1
            for c in q:
                for nb in get_neighbours(c, cells, "v^<>."):
                    if nb not in visited:
                        if nb in junctions:
                            graph[j].append((nb, steps))
                            visited.add(nb)
                        else:
                            visited.add(nb)
                            cq.append(nb)
            q = cq
    return graph


def search_to(start, end, graph):
    steps = 0
    visited = {start}
    q = deque()
    q.append((start, steps, visited.copy()))
    p2 = 0
    while q:
        current, steps, visited = q.popleft()
        if current == end:
            p2 = max(steps, p2)
        for node, cost in graph[current]:
            if node not in visited:
                c_visited = visited.copy()
                c_visited.add(node)
                q.append((node, steps + cost, c_visited))
    return p2


def main():
    start = (0, 0)
    end = (0, 0)
    cells = {}
    with open(txt(), 'r') as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line):
                if cell not in ("\n", "#"):
                    if y == 0:
                        start = (x, y)
                    cells[(x, y)] = cell
                    end = (x, y)
    print("p1:", search(start, end, cells))

    junctions = get_junctions(cells)
    junctions.add(start)
    junctions.add(end)
    graph = create_graph(junctions, cells)
    print('p2:', search_to(start, end, graph))

if __name__ == "__main__":
    main()
