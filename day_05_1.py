from utils import open_input


def handle_map(rows, values):
    next_value = []
    for value in values:
        is_set = False
        for dest, orig, rang in rows:
            if orig <= value <= orig + rang:
                next_value.append(dest + (value - orig))
                is_set = True
                break
        if not is_set:
            next_value.append(value)
    return next_value


def main():
    inp = open_input("05").split("\n\n")
    seeds = [int(x) for x in inp[0].split(": ")[1].split(" ")]
    for inp_map in inp[1:]:
        rows = inp_map.split("\n")
        seeds = handle_map([[int(y) for y in x.split(" ")] for x in rows[1:]], seeds)
    print(min(seeds))
    # print(total)


if __name__ == '__main__':
    main()
