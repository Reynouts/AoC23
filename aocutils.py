import os
import sys
from aocd import get_data
import time
import heapq
import re


def txt(ext = ".txt"):
    return sys.argv[0].split("/")[-1].split(".")[0] + ext

def get_input(day, token="\n"):
    "Open input file of corresponding day. Returns a list of strings"
    return get_data(day=day).split(token)


def get_file(day, token="\n"):
    with open('day{}.txt'.format(day), 'r') as f:
        return f.read().split(token)

def get_digits_from_input(day):
    with open('day{}.txt'.format(day), 'r') as f:
        return list(map(int, (re.findall("\d+", f.read()))))


def write_input(day):
    with open('day{}.txt'.format(day), 'w') as f:
        f.write(get_data(day=day))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



def get_dictgridfromfile(file):
    cells = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, cell in enumerate(line):
                if cell != "\n":
                    cells[(i, j)] = int(cell)
    return cells


def get_gridfromfile(file):
    grid = []
    with open(file, 'r') as f:
        for line in f.read().splitlines():
            grid.append([c for c in line])
    return grid


def print_griddict(griddict, frame, default=" "):
    res = ""
    for i in range(frame[0], frame[1]):
        for j in range(frame[2], frame[3]):
            if (j, i) in griddict:
                res += griddict[(j, i)]
            else:
                res += default
        res += "\n"
    print(res)


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed



#Pathfinding stuff
# (not very generic, works for fully connected grids, should add graph class with neigbours method)
class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0

    def __lt__(self, other):
        return self.G < other.G


def a_star_grid(start, goal, grid, dist=distance):
    openlist = []
    heapq.heappush(openlist, (0, start))
    parents = {start: None}
    cost = {start: 0}

    while openlist:
        current = heapq.heappop(openlist)[1]
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path, cost
        for nb_pos in get_neighbours(current.point, grid, False):
            nb = grid[nb_pos[0]][nb_pos[1]]
            new_cost = cost[current] + nb.value
            if nb not in cost or new_cost < cost[nb]:
                cost[nb] = new_cost
                priority = new_cost + dist(nb.point, goal.point)
                heapq.heappush(openlist, (priority, nb))
                parents[nb] = current
    # no path found
    return [], 0


def get_neighbours(cell, cells, diag=True):
    neighbours = []
    heading = ((1, 0), (-1, 0), (0, 1), (0, -1))
    if diag:
        heading = heading + ((1, 1), (-1, -1), (-1, 1), (1, -1))
    for h in heading:
        pos = cell[0] + h[0], cell[1] + h[1]
        if type(cells) is dict:
            if pos in cells:
                neighbours.append(pos)
        else:
            width = len(cells)
            height = len(cells[0])
            if (0 <= pos[0] < width) and (0 <= pos[1] < height):
                neighbours.append((pos[0],pos[1]))
    return neighbours