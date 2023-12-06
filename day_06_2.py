import math

from utils import open_input


def main():
    inp = open_input("06").split("\n")
    times = int(inp[0].split(" ", 1)[1].replace(" ", ""))
    distances = int(inp[1].split(" ", 1)[1].replace(" ", ""))
    wins = 0
    # x² + (times * x) + distances = 0
    r = math.sqrt(((times/2)**2) - distances)
    x1 = math.floor((times/2) + r)
    x2 = math.ceil((times/2) - r)
    print(x1-x2 + 1)
    for x in range(times):
        if x * (times - x) > distances:
            wins += 1
    print(wins)


if __name__ == '__main__':
    main()
