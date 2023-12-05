from aocutils import *
import re


def seed_to_location(seed, processed_maps):
    for processed_map in processed_maps:
        location = seed
        for dest_start, source_start, range_val in processed_map:
            if source_start <= seed < (source_start + range_val):
                location = seed - (source_start - dest_start)
                break
        seed = location
    return seed


def location_to_seed(location, processed_maps):
    for processed_map in reversed(processed_maps):
        for dest_start, source_start, range_val in processed_map:
            if dest_start <= location < (dest_start + range_val):
                location = location + (source_start - dest_start)
                break
    return location


def is_seed(number, seed_input):
    for start, end in zip(seed_input[0::2], seed_input[1::2]):
        if start <= number < (start + end):
            return True
    return False


def main():
    with open(txt(), 'r') as f:
        seeds, *maps = f.read().split('\n\n')
    initial_seeds = list(map(int, re.findall(r'\d+', seeds)))
    processed_maps = [[tuple(map(int, re.findall(r'\d+', line))) for line in mp.split("\n")[1:]]for mp in maps]

    p1 = 10**10
    for seed in initial_seeds:
        location = seed_to_location(seed, processed_maps)
        if location < p1:
            p1 = location
    print(f'p1: {p1}')

    for i in range(p1):
        nl = location_to_seed(i, processed_maps)
        if is_seed(nl, initial_seeds):
            print(f'p2: {i}')
            return


if __name__ == "__main__":
    main()
