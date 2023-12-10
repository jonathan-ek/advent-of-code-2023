from utils import open_input


def main():
    sequences = [[int(z) for z in y if z != ""] for y in [x.split(" ") for x in open_input("09").split("\n")]]
    total = 0
    for sequence in sequences:
        s = [sequence]
        v = sequence
        while True:
            diffs = []
            for i in range(len(v) - 1):
                diffs.append(v[i + 1] - v[i])
            if all([x == 0 for x in diffs]):
                break
            else:
                v = diffs
                s.append(v)
        reversed_s = list(reversed(s))
        for i in range(len(s) - 1):
            reversed_s[i + 1].append(reversed_s[i+1][len(reversed_s[i+1]) - 1] + reversed_s[i][len(reversed_s[i]) - 1])
        total += reversed_s[-1][-1]
    print(total)


if __name__ == '__main__':
    main()
