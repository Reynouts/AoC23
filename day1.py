from aocutils import *
import re

def main():
    with open(txt(), 'r') as f:
        lines = f.read().split('\n')

    numbdict = {"one":      "1",
                "two":      "2",
                "three":    "3",
                "four":     "4",
                "five":     "5",
                "six":      "6",
                "seven":    "7",
                "eight":    "8",
                "nine":     "9"}

    p1_result = 0
    p2_result = 0
    for line in lines:
        p1 = re.findall(r'\d', line)
        p1_result += int(p1[0]+p1[-1])
        # positive lookahead regex to avoid missing overlaps
        p2 = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        first = p2[0]
        last = p2[-1]
        if len(first) != 1: first = numbdict[first]
        if len(last) != 1: last = numbdict[last]
        p2_result += int(first+last)
    print(f"p1: {p1_result}")
    print(f"p2: {p2_result}")


if __name__ == "__main__":
    main()