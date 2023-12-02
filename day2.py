from aocutils import *
import re


def main():
    with open(txt(), 'r') as f:
        lines = f.read().split('\n')
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    valid_games = []
    power_set = []
    for line in lines:
        count = {"red": 0, "blue": 0, "green": 0}
        game, info = line.split(":")
        game = int(re.findall("\d+", game)[0])
        for i in info.split(";"):
            for draw in i.split(","):
                _, amount, color = draw.split(" ")
                amount = int(amount)
                if amount > count[color]:
                    count[color] = amount
        if count["red"] <= red_limit and count["green"] <= green_limit and count["blue"] <= blue_limit:
            valid_games.append(game)
        power_set.append(count["red"]*count["blue"]*count["green"])
    print(f'part1: {sum(valid_games)}')
    print(f'part2: {sum(power_set)}')


if __name__ == "__main__":
    main()