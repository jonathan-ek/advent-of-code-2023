from utils import open_input


def get_first_digit(string):
    for s in string:
        if s.isdigit():
            return s


def get_last_digit(string):
    for s in reversed(string):
        if s.isdigit():
            return s


def main():
    inp = open_input("01").split("\n")
    total = 0
    for row in inp:
        first = get_first_digit(row)
        last = get_last_digit(row)
        nr = int(f"{first}{last}")
        total += nr
    print(total)


if __name__ == '__main__':
    main()
