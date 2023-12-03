from utils import open_input


def main():
    inp = open_input("03").split("\n")
    total = 0
    symbols = set()
    number = 0
    potential_cogs = {}
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
                            if inp[y1][x1] == "*":
                                symbols.add((x1, y1))
            else:
                if number and len(symbols) > 0:
                    for s in symbols:
                        if s in potential_cogs:
                            potential_cogs[s].append(number)
                        else:
                            potential_cogs[s] = [number]
                number = 0
                symbols = set()
    for symbol, numbers in potential_cogs.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]

    print(total)


if __name__ == '__main__':
    main()
