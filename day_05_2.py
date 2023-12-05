from utils import open_input


def merge_maps(start, map2):
    new_ranges = []
    for orig, rang in sorted(start, key=lambda x: x[0]):
        start = orig
        for dest_2, orig_2, rang_2 in sorted(map2, key=lambda x: x[1]):
            if (orig + rang < orig_2) or (orig > orig_2 + rang_2):
                continue
            if start < orig_2:
                new_ranges.append([start, orig_2 - start])
                start = orig_2
            diff = start - orig_2
            if orig_2 + rang_2 >= orig + rang:
                new_ranges.append([dest_2 + diff, orig + rang - start])
                start = orig + rang
            else:
                new_ranges.append([dest_2 + diff, rang_2 - diff])
                start = orig_2 + rang_2
        if start < orig + rang:
            new_ranges.append([start, orig + rang - start])
    return sorted(new_ranges, key=lambda x: x[0])


def main():
    inp = open_input("05").split("\n\n")
    tmp = [int(x) for x in inp[0].split(": ")[1].split(" ")]
    start_map = []
    for x in range(int(len(tmp) / 2)):
        start_map.append([tmp[x*2], tmp[x*2 + 1]])
    for inp_map in inp[1:]:
        rows = inp_map.split("\n")
        start_map = merge_maps(start_map, [[int(y) for y in x.split(" ")] for x in rows[1:]])
    print(start_map[0][0])


if __name__ == '__main__':
    main()
