from utils import open_input


def main():
    inp = open_input("03").split("\n")
    total = 0
    has_symbol = False
    number = 0
    for y, row in enumerate(inp):
        for x, c in enumerate(row):
            if c.isdigit():
                if number:
                    number = int(f"{number}{c}")
                else:
                    number = int(c)
                for i in range(3):
                    for j in range(3):
                        x1 = x + i - 1
                        y1 = y + j - 1
                        if 0 <= x1 < len(row) and 0 <= y1 < len(inp):
                            if not inp[y1][x1].isdigit() and inp[y1][x1] != ".":
                                has_symbol = True
            else:
                if number and has_symbol:
                    total += number
                number = 0
                has_symbol = False
    print(total)


if __name__ == '__main__':
    main()
