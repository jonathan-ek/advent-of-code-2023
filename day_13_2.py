from utils import open_input


def row_mirror_1(drawing):
    res = []
    if drawing[0] in drawing[1:]:
        tmp1 = [i for i, ltr in enumerate(drawing) if ltr == drawing[0] and i != 0]
        for i in tmp1:
            if i % 2 == 0:
                continue
            found = True
            for j in range(int(i / 2) + 1):
                if drawing[j] != drawing[i - j]:
                    found = False
                    break
            if found:
                res.append(int(i / 2) + 1)
    return res


def row_mirror_2(drawing):
    res = []
    if drawing[-1] in drawing[:-1]:
        tmp1 = [i for i, ltr in enumerate(drawing) if ltr == drawing[-1] and i != len(drawing) - 1]
        for i in tmp1:
            if ((len(drawing) - 1) - i) % 2 == 0:
                continue
            found = True
            for j in range(int((len(drawing) - i) / 2)):
                if drawing[len(drawing) - 1 - j] != drawing[i + j]:
                    found = False
                    break
            if found:
                # print(drawing)
                res.append(len(drawing) - (int((len(drawing) - 1 - i) / 2) + 1))
    return res


def analyze_drawing(drawing):
    res1 = row_mirror_1(drawing)
    res2 = row_mirror_2(drawing)
    transposed = list(map(list, zip(*drawing)))
    res3 = row_mirror_1(transposed)
    res4 = row_mirror_2(transposed)
    res = []
    for r in res1 + res2:
        res.append(('a', r))
    for r in res3:
        res.append(('c', r))
    for r in res4:
        res.append(('d', r))
    return res


def main():
    inp = open_input("13").split("\n\n")
    total = 0
    for i, drawing in enumerate(inp):
        original_drawing = drawing.split("\n")
        drawing = [list(x) for x in original_drawing]
        orig_res = analyze_drawing(drawing)[0]
        found_mirror = False
        row = 0
        col = 0
        while not found_mirror:
            drawing = [list(x) for x in original_drawing]
            if col == len(drawing[0]):
                col = 0
                row += 1
            if drawing[row][col] == '.':
                drawing[row][col] = '#'
            else:
                drawing[row][col] = '.'
            res = [x for x in analyze_drawing(drawing) if x != orig_res]
            if len(res) == 1:
                found_mirror = True
                if res[0][0] in ['a', 'b']:
                    total += res[0][1] * 100
                else:
                    total += res[0][1]

            col += 1
    print(total)


if __name__ == '__main__':
    main()
