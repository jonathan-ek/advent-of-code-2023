from utils import open_input


def main():
    inp = open_input("04").split("\n")
    card_count = [1 for _ in inp]

    for i, row in enumerate(inp):
        card, numbers = row.split(":", 1)
        winnings, numbers = [set([int(y) for y in x.strip().split(" ") if y != ""]) for x in numbers.split("|", 1)]
        wins = len(winnings.intersection(numbers))
        for w in range(wins):
            card_count[i + w + 1] += card_count[i]

    print(sum(card_count))


if __name__ == '__main__':
    main()
