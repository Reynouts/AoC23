from aocutils import *
from collections import Counter


class Hand:
    score = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def hand_score(self):
        if self.score["J"] == 1:
            return min(calc_score(self.cards.replace("J", r)) for r in self.cards)
        return calc_score(self.cards)

    def card_compare(self, other):
        for s, o in zip(self.cards, other.cards):
            if s != o:
                return self.score[s] > other.score[o]

    def __gt__(self, other):
        s, o = self.hand_score(), other.hand_score()
        return s < o or (s == o and self.card_compare(other))


def calc_score(cards):
    v = Counter(cards).values()

    if 5 in v:
        return 1
    if 4 in v:
        return 2
    if 3 in v and 2 in v:
        return 3
    if 3 in v:
        return 4
    if list(v).count(2) == 2:
        return 5
    if 2 in v:
        return 6
    return 7


def total_winnings(hands):
    hands.sort()
    total = 0
    for rank, hand in enumerate(hands):
        total += hand.bid * (rank + 1)
    return total


def main():
    with open(txt(), 'r') as f:
        data = f.read().split('\n')
    hands = []
    for line in data:
        cards, bid = line.split(" ")
        hands.append(Hand(cards, int(bid)))

    print(f"p1: {total_winnings(hands)}")
    hands[1].score["J"] = 1
    print(f"p2: {total_winnings(hands)}")


if __name__ == "__main__":
    main()
