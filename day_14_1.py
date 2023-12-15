from utils import open_input


def main():
    inp = open_input("14").split("\n")
    new_state = []
    for x in range(len(inp[0])):
        next_stop = 0
        for y in range(len(inp)):
            if inp[y][x] == ".":
                continue
            elif inp[y][x] == "#":
                next_stop = y + 1
                continue
            elif inp[y][x] == "O":
                new_state.append(next_stop)
                next_stop += 1
    print(sum([len(inp) - x for x in new_state]))


if __name__ == '__main__':
    main()
