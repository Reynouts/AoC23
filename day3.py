from aocutils import *
import re


def main():
    grid = get_gridfromfile("day3.txt")
    print(grid)

    checked = set()
    number = ""
    valid = False
    numbers = []
    for y, line in enumerate(grid):
        for x, element in enumerate(line):
            if element.isdigit():
                number += element
                checked.add((x,y))
                nbs = set(get_neighbours((x,y), grid))
                for nb in nbs.difference(checked):
                    nb = grid[nb[1]][nb[0]]
                    if nb != "." and not nb.isdigit():
                        valid = True
            else:
                if number:
                    numbers.append((int(number), valid))
                number = ""
                valid = False
    total = 0
    for n in numbers:
        if n[1]:
            total += n[0]
    print(total)

    # p2

    def check_number(location):
        if not grid[location[1]][location[0]].isdigit():
            return "no digit"
        # scan left
        shift = 1
        lefts = []
        while location[0]-shift >= 0:
            left = grid[location[1]][location[0]-shift]
            if left.isdigit():
                lefts.append(left)
                shift += 1
            else:
                break
        # scan right
        width = len(grid)
        shift = 1
        rights = []
        while location[0]+shift <= (width-1):
            right = grid[location[1]][location[0]+shift]
            if right.isdigit():
                rights.append(right)
                shift += 1
            else:
                break
        result = ""
        for left in reversed(lefts):
            result += left
        result += grid[location[1]][location[0]]
        for right in rights:
            result += right
        return int(result)

    numbers = []
    for y, line in enumerate(grid):
        for x, element in enumerate(line):
            if element == "*":
                nbs = get_neighbours((x,y), grid)
                surrounds = set()
                for nb in nbs:
                    nb_value = grid[nb[1]][nb[0]]
                    if nb_value.isdigit():
                        surrounds.add(check_number((nb[0],nb[1])))
                if len(surrounds) == 2:
                    print(surrounds)
                    numbers.append(surrounds)
    print(numbers)
    total = 0
    for gear in numbers:
        total += list(gear)[0] * list(gear)[1]
    print(total)

if __name__ == "__main__":
    main()