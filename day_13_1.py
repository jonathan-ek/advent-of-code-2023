from utils import open_input

def row_mirror_1(drawing):
    if drawing[0] in drawing[1:]:
        # Could be row mirror
        tmp1 = [i for i, ltr in enumerate(drawing) if ltr == drawing[0] and i != 0]
        for i in tmp1:
            found = True
            for j in range(int(i / 2) + 1):
                if drawing[j] != drawing[i - j]:
                    found = False
                    break
            if found:
                return int(i / 2) + 1


def row_mirror_2(drawing):
    if drawing[-1] in drawing[:-1]:
        # Could be row mirror
        tmp1 = [i for i, ltr in enumerate(drawing) if ltr == drawing[-1] and i != len(drawing) - 1]
        for i in tmp1:
            found = True
            for j in range(int((len(drawing) - i) / 2)):
                if drawing[len(drawing) - 1 - j] != drawing[i + j]:
                    found = False
                    break
            if found:
                # print(drawing)
                return len(drawing) - (int((len(drawing) - 1 - i) / 2) + 1)


def analyze_drawing(drawing):
    res1 = row_mirror_1(drawing)
    res2 = row_mirror_2(drawing)
    transposed = list(map(list, zip(*drawing)))
    res3 = row_mirror_1(transposed)
    res4 = row_mirror_2(transposed)
    res = []
    if res1:
        res.append(('a', res1))
    if res2:
        res.append(('b', res2))
    if res3:
        res.append(('c', res3))
    if res4:
        res.append(('d', res4))
    return res


def main():
    inp = open_input("13").split("\n\n")
    total = 0
    for drawing in inp:
        drawing = [list(x) for x in drawing.split("\n")]
        res = analyze_drawing(drawing)
        if res[0][0] in ['a', 'b']:
            total += res[0][1] * 100
        else:
            total += res[0][1]
    print(total)


if __name__ == '__main__':
    main()
