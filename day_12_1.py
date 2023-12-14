import collections

from utils import open_input

def check(row, group):
    index = 0
    count = 0
    # print(row, group)
    for c in row:
        if c == '#':
            count += 1
        elif c == '.':
            if count != 0:
                if index < len(group) and group[index] == count:
                    index += 1
                else:
                    # print(False, count, index)
                    return False
            count = 0

        # print(count, index)
    if index < len(group) and count != 0:
        if group[index] == count:
            return index == len(group) - 1
        else:
            return False
    return index == len(group)


def main():
    inp = [(y[0], tuple([int(z) for z in y[1].split(',')])) for y in [x.split(" ") for x in open_input("12").split("\n")]]
    total = 0
    for row, groups in inp:
        nr_of_broken = sum(groups)
        options = ['']
        for char in row:
            new_options = []
            if char == '?':
                for option in options:
                    new_options.append(option + '.')
                    if nr_of_broken > collections.Counter(option)['#']:
                        new_options.append(option + '#')
                options = new_options
            else:
                for option in options:
                    if char == '#' and nr_of_broken == collections.Counter(option)['#']:
                        continue
                    new_options.append(option + char)
                options = new_options
        options = [x for x in options if nr_of_broken == collections.Counter(x)['#']]

        t = [x for x in options if check(x, groups)]
        total += len(t)
    print(total)


if __name__ == '__main__':
    main()
