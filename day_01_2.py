from utils import open_input


def get_first_digit(string):
    for s in string:
        if s.isdigit():
            return s


def get_last_digit(string):
    for s in reversed(string):
        if s.isdigit():
            return s


def convert_text_to_nr(string):
    return (string.lower().replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace(
        "four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace(
        "eight", "e8t").replace("nine", "n9e").replace("zero", "z0o"))


def main():
    inp = open_input("01").split("\n")
    total = 0
    for r in inp:
        row = convert_text_to_nr(r)
        first = get_first_digit(row)
        last = get_last_digit(row)
        nr = int(f"{first}{last}")
        print(nr)
        total += nr
    print(total)


if __name__ == '__main__':
    main()
