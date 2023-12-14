from utils import open_input


def get_nr_of_options(row, groups):
    options = {('', 0, 0): 1}
    for i, char in enumerate(row):
        new_options = {}
        for option, c in options.items():
            if char == '#' or char == '?':
                if option[1] < len(groups) and groups[option[1]] > option[2]:
                    tmp = ('#', option[1], option[2] + 1)
                    if tmp not in new_options:
                        new_options[tmp] = c
                    else:
                        new_options[tmp] += c
            if char == '.' or char == '?':
                if option[1] < len(groups) and (groups[option[1]] == option[2] and option[0] == '#') or (option[2] == 0 and (option[0] == '.' or option[0] == '')):
                    tmp = ('.', option[1] if (option[0] == '.' or option[0] == '') else option[1] + 1, 0)
                    if tmp not in new_options:
                        new_options[tmp] = c
                    else:
                        new_options[tmp] += c
        options = new_options
    option_keys = [x for x in options.keys() if x[1] == len(groups) or (x[1] + 1 == len(groups) and x[2] == groups[-1])]
    total = 0
    for k in option_keys:
        total += options[k]
    return total


def main():
    mpl = 5
    res = []
    inp = [('?'.join([y[0]]*mpl), tuple([int(z) for z in y[1].split(',')]*mpl)) for y in [x.split(" ") for x in open_input("12").split("\n")]]

    for j, (row, groups) in enumerate(inp):
        res.append(get_nr_of_options(row, groups))
    print(sum(res))


if __name__ == '__main__':
    main()
