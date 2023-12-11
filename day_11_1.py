from utils import open_input


def main():
    inp = [list(x) for x in open_input("11").split("\n")]
    expanded_map = []
    for row in inp:
        if all([x == '.' for x in row]):
            expanded_map.append(list([*row]))
        expanded_map.append(row)
    cols = []
    for col in range(len(inp[0])):
        if all([row[col] == '.' for row in expanded_map]):
            cols.append(col)
    for row in expanded_map:
        for col in reversed(cols):
            row.insert(col, '.')
    galaxies = []
    for y, row in enumerate(expanded_map):
        for x, v in enumerate(row):
            if v == '#':
                galaxies.append((x, y))
    diff_sum = 0
    for i, galaxy in enumerate(galaxies):
        for galaxy_index in range(i + 1, len(galaxies)):
            pair_galaxy = galaxies[galaxy_index]
            x_diff = abs(galaxy[0] - pair_galaxy[0])
            y_diff = abs(galaxy[1] - pair_galaxy[1])
            pair_diff = x_diff + y_diff
            diff_sum += pair_diff

    print(diff_sum)


if __name__ == '__main__':
    main()
