from utils import open_input


def main():
    inp = open_input("04").split("\n")
    total = 0
    for row in inp:
        _card, numbers = row.split(":", 1)
        winnings, numbers = [set([int(y) for y in x.strip().split(" ") if y != ""]) for x in numbers.split("|", 1)]
        wins = len(winnings.intersection(numbers))
        total += (2 ** (wins - 1)) if wins > 0 else 0
    print(total)


if __name__ == '__main__':
    main()
