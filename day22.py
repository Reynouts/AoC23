import re
from copy import deepcopy

def get_neighbours(c, cells):
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    return [pos for dx, dy in dirs if (pos := (c[0] + dx, c[1] + dy)) in cells]


class block:
    blocks = set()
    def __init__(self, sx, sy, sz, ex, ey, ez):
        self.tiles = []
        for z in range(sz+1, sz-1, -1):
            for y in range(sy, ey+1):
                for x in range(sx, sx+1):
                    self.tiles.append([x, y, z])

    def __gt__(self, other):
        return min([tile[2] for tile in self.tiles]) < min([tile[2] for tile in other.tiles])



def main():
    with open("day22.txt", 'r') as f:
        instructions = f.read().split('\n')

    blocks = []
    occupied = set()
    total = 0
    for i in instructions:
        blocks.append([])
        sx, sy, sz, ex, ey, ez = map(int, re.findall("\d+", i))
        for z in range(ez, sz-1, -1):
            for y in range(sy, ey+1):
                for x in range(sx, ex+1):
                    blocks[-1].append((x, y, z))
                    total += 1
                    occupied.add((x, y, z))
    print(total, len(occupied))
    print(blocks)
    down = True
    while down:
        down = False
        for i, b in enumerate(blocks):
            can_fall = True
            for c in b:
                if (c[0], c[1], c[2]-1) in (occupied - set(b)) or c[2]-1 == 0:
                    can_fall = False
            if can_fall:
                down = True
                new_block = []
                for c in b:
                    occupied.remove(c)
                for c in b:
                    new_block.append((c[0], c[1], c[2]-1))
                    occupied.add((c[0], c[1], c[2]-1))
                blocks[i] = new_block
    mx = 0
    for b in blocks:
        for c in b:
            if c[2] > mx:
                mx = c[2]
    print(mx)

    cant = []
    for b in blocks:
        copycied = deepcopy(occupied)
        for c in b:
            copycied.remove(c)
        for b2 in blocks:
            if b2 != b:
                can_fall = True
                for c in b2:
                    if (c[0], c[1], c[2] - 1) in (copycied - set(b2)) or c[2] - 1 == 0:
                        can_fall = False
                if can_fall:
                    cant.append(b)
                    #break
                print(b, b2, can_fall)

        print("L:",len(cant))
    print(len(blocks), len(cant))
    print(len(blocks)-len(cant))
    print(len(cant))

if __name__ == "__main__":
    main()
