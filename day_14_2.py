import math

from utils import open_input

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def tilt(pos, stops, size, direction):
    new_pos = []
    if direction == NORTH:
        for x in range(size[0]):
            next_stop = 0
            for y in range(size[1]):
                if (x, y) in stops:
                    next_stop = y + 1
                elif (x, y) in pos:
                    new_pos.append((x, next_stop))
                    next_stop += 1
    elif direction == SOUTH:
        for x in range(size[0]):
            next_stop = size[1] - 1
            for y in range(size[1]-1, -1 ,-1):
                if (x, y) in stops:
                    next_stop = y - 1
                elif (x, y) in pos:
                    new_pos.append((x, next_stop))
                    next_stop -= 1
    elif direction == WEST:
        for y in range(size[1]):
            next_stop = 0
            for x in range(size[0]):
                if (x, y) in stops:
                    next_stop = x + 1
                elif (x, y) in pos:
                    new_pos.append((next_stop, y))
                    next_stop += 1
    elif direction == EAST:
        for y in range(size[1]):
            next_stop = size[0] - 1
            for x in range(size[0]-1, -1 ,-1):
                if (x, y) in stops:
                    next_stop = x - 1
                elif (x, y) in pos:
                    new_pos.append((next_stop, y))
                    next_stop -= 1
    return new_pos


def print_map(pos, stops, size):
    for y in range(size[1]):
        for x in range(size[0]):
            if (x, y) in stops:
                print("#", end="")
            elif (x, y) in pos:
                print("O", end="")
            else:
                print(".", end="")
        print()


def main():
    inp = open_input("14").split("\n")
    pos = []
    stops = []
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] == ".":
                continue
            elif inp[y][x] == "#":
                stops.append((x, y))
            elif inp[y][x] == "O":
                pos.append((x, y))
    answers = []
    while True:
        pos = tilt(pos, stops, (len(inp[0]), len(inp)), NORTH)
        pos = tilt(pos, stops, (len(inp[0]), len(inp)), WEST)
        pos = tilt(pos, stops, (len(inp[0]), len(inp)), SOUTH)
        pos = tilt(pos, stops, (len(inp[0]), len(inp)), EAST)
        # print_map(pos, stops, (len(inp[0]), len(inp)))
        w = sum([len(inp) - y for (x, y) in pos])
        print('.', end='')
        if w in answers:
            answers.append(w)
            tmp1 = [i for i, ltr in enumerate(answers) if w == ltr]
            if len(tmp1) == 3 and tmp1[2] - tmp1[1] == tmp1[1] - tmp1[0]:
                diff = tmp1[2] - tmp1[1]
                t = diff - (1000000000-tmp1[2]) % diff
                print()
                print(answers[tmp1[2] - t - 1])
                break
        else:
            answers.append(w)


if __name__ == '__main__':
    main()
