from aocutils import *
import re


def check_pair(time, distance):
    for hold in range(time):
        if (time-hold) * hold > distance:
            return time - (hold * 2) + 1
    return 0


def main():
    with open(txt(), 'r') as f:
        t_, d_ = f.read().split('\n')
    t = re.findall("\d+", t_)
    d = re.findall("\d+", d_)

    total = 1
    for p in zip(map(int, t), map(int, d)):
        total *= check_pair(*p)

    print(f'p1: {total}')
    print(f'p2: {check_pair(int("".join(t)), int("".join(d)))}')


if __name__ == "__main__":
    main()
