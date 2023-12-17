from aocutils import *
import heapq
from collections import defaultdict


def dijksdrama(grid, start, end, min_steps, max_steps):
    def get_move_cost(current, direction, steps):
        x, y = current
        dx, dy = direction
        move_cost = 0
        for _ in range(steps):
            x, y = x + dx, y + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                move_cost += grid[x][y]
            else:
                return float('inf')
        return move_cost

    def get_neighbors(node, prev_direction):
        neighbors = []
        x, y = node
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = -1
        change_set = range(1, 5)
        if prev_direction: # not the starting node
            dir_index = directions.index(prev_direction)
            change_set = [-1, 1]
        for i in change_set:
            dx, dy = directions[(dir_index + i) % len(directions)]
            for step in range(min_steps, max_steps + 1):
                new_x, new_y = x + dx * step, y + dy * step
                if 0 <= new_x < n and 0 <= new_y < m:
                    neighbors.append(((dx, dy), (new_x, new_y), step))
        return neighbors

    n, m = len(grid), len(grid[0])
    distance = defaultdict(lambda: float('inf'))
    pq = []
    heapq.heappush(pq, (0, start, None, 0))  # (cost, node, direction, steps)
    distance[(start, None, 0)] = 0

    while pq:
        cost, node, direction, steps = heapq.heappop(pq)
        if node == end:
            return cost
        for next_direction, next_node, next_steps in get_neighbors(node, direction):
            move_cost = get_move_cost(node, next_direction, next_steps)
            new_cost = cost + move_cost
            if new_cost < distance[(next_node, next_direction, next_steps)]:
                distance[(next_node, next_direction, next_steps)] = new_cost
                heapq.heappush(pq, (new_cost, next_node, next_direction, next_steps))
    return float('inf')


def main():
    grid = get_intgridfromfile(txt())
    print(f'p1: {dijksdrama(grid, (0, 0), (len(grid[0])-1, len(grid)-1), 1, 3)}')
    print(f'p2: {dijksdrama(grid, (0, 0), (len(grid[0])-1, len(grid)-1), 4, 10)}')


if __name__ == "__main__":
    main()
