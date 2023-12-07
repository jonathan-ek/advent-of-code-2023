from collections import Counter
from utils import open_input

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
ONE_PAIR = 1
HIGH_CARD = 0

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)
        counter = Counter(self.cards)
        joker_count = counter['J']
        cards_woj = [x for x in self.cards if x != 'J']
        counter = Counter(cards_woj)
        repeats = sorted(counter.values(), reverse=True)
        self.hand = HIGH_CARD
        if joker_count == 5 or repeats[0] + joker_count == 5:
            self.hand = FIVE_OF_A_KIND
        elif repeats[0] + joker_count == 4:
            self.hand = FOUR_OF_A_KIND
        elif repeats[0] + joker_count == 3:
            if repeats[1] == 2:
                self.hand = FULL_HOUSE
            else:
                self.hand = THREE_OF_A_KIND
        elif repeats[0] + joker_count == 2:
            if repeats[1] == 2:
                self.hand = TWO_PAIRS
            else:
                self.hand = ONE_PAIR

    def __lt__(self, other):
        if self.hand == other.hand:
            if CARDS.index(self.cards[0]) == CARDS.index(other.cards[0]):
                if CARDS.index(self.cards[1]) == CARDS.index(other.cards[1]):
                    if CARDS.index(self.cards[2]) == CARDS.index(other.cards[2]):
                        if CARDS.index(self.cards[3]) == CARDS.index(other.cards[3]):
                            if CARDS.index(self.cards[4]) == CARDS.index(other.cards[4]):
                                return False
                            else:
                                return CARDS.index(self.cards[4]) > CARDS.index(other.cards[4])
                        else:
                            return CARDS.index(self.cards[3]) > CARDS.index(other.cards[3])
                    else:
                        return CARDS.index(self.cards[2]) > CARDS.index(other.cards[2])
                else:
                    return CARDS.index(self.cards[1]) > CARDS.index(other.cards[1])
            else:
                return CARDS.index(self.cards[0]) > CARDS.index(other.cards[0])
        else:
            return self.hand < other.hand

    def __str__(self):
        return "".join(self.cards)

    def __repr__(self):
        return str(self)


def main():
    inp = open_input("07").split("\n")
    inp_data = [(Hand(x), int(y)) for x, y in [x.split(" ", 1) for x in inp]]
    data = sorted(inp_data, key=lambda x: x[0])
    res = 0
    for i, (hand, bet) in enumerate(data):
        res += bet * (i + 1)
    print(res)


if __name__ == '__main__':
    main()
