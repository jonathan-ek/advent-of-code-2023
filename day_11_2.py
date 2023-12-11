from utils import open_input


def main():
    inp = [list(x) for x in open_input("11").split("\n")]
    multiplier = 1000000
    rows = []
    for y, row in enumerate(inp):
        if all([x == '.' for x in row]):
            rows.append(y)
    cols = []
    for col in range(len(inp[0])):
        if all([row[col] == '.' for row in inp]):
            cols.append(col)
    galaxies = []
    for y, row in enumerate(inp):
        for x, v in enumerate(row):
            if v == '#':
                galaxies.append((x, y))
    diff_sum = 0
    for i, galaxy in enumerate(galaxies):
        for galaxy_index in range(i + 1, len(galaxies)):
            pair_galaxy = galaxies[galaxy_index]
            x_diff = abs(galaxy[0] - pair_galaxy[0])
            y_diff = abs(galaxy[1] - pair_galaxy[1])
            for row in rows:
                if galaxy[1] < row < pair_galaxy[1]:
                    y_diff += (multiplier - 1)
            x_min = min([galaxy[0], pair_galaxy[0]])
            x_max = max([galaxy[0], pair_galaxy[0]])
            for col in cols:
                if x_min < col < x_max:
                    x_diff += (multiplier - 1)
            pair_diff = x_diff + y_diff
            diff_sum += pair_diff
    print(diff_sum)


if __name__ == '__main__':
    main()
