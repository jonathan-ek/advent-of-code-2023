from utils import open_input


def parse_sets(sets):
    sets = sets.split(";")
    r = 0
    g = 0
    b = 0
    for s in sets:
        colors = s.split(",")
        for c in colors:
            nr, color = c.strip().split(" ")
            if color == "red":
                r = max(r, int(nr))
            elif color == "green":
                g = max(g, int(nr))
            elif color == "blue":
                b = max(b, int(nr))
    return r, g, b


def main():
    inp = open_input("02").split("\n")
    total = 0
    for row in inp:
        x, sets = row.split(":", 1)
        _, nr = x.split(' ')
        r, g, b = parse_sets(sets)
        total += r * g * b
    print(total)


if __name__ == '__main__':
    main()
