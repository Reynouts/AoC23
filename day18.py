import re


def create_path(dig_plan):
    x, y = 0, 0
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    path = [(x, y)]
    for dir, dist in dig_plan:
        path.append((path[-1][0] + dirs[dir][0] * dist, path[-1][1] + dirs[dir][1] * dist))
    return path


def lace_it(instructions):
    path = create_path(instructions)
    # get the trench length, by just calculating distance between the points in the path
    trench = sum([abs(path[i + 1][0] - path[i][0]) + abs(path[i + 1][1] - path[i][1]) for i in range(len(path) - 1)])
    # calculate the inside area of the path, according the the shoelace theory
    area = abs(sum([path[i][0] * path[i - 1][1] - path[i - 1][0] * path[i][1] for i in range(len(path))])) // 2
    # because we only want integer points to count, we need to adjust this area using Pick's theorem.. just do it
    return (area - trench // 2 + 1) + trench


def main():
    with open("day18.txt", 'r') as f:
        instructions = f.read().split('\n')

    directions = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    p1_instructions = []
    p2_instructions = []
    for i in instructions:
        p1_instructions.append((i[0], int(re.findall("\d+", i)[0])))
        hex = i.split("#")[1][:-1]
        p2_instructions.append((directions[int(hex[-1], 16)], int(hex[:-1], 16)))
    print(f'p1: {lace_it(p1_instructions)}')
    print(f'p2: {lace_it(p2_instructions)}')


if __name__ == "__main__":
    main()
