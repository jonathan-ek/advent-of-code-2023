from utils import open_input


def hash(word):
    val = 0
    for c in word:
        ascii_val = ord(c)
        val += ascii_val
        val = val * 17
        val = val % 256
    return val


def main():
    inp = open_input("15").split(",")
    boxes = {}
    for w in inp:
        if '-' in w:
            k = w.split('-')[0]
            key = hash(k)
            boxes[key] = [x for x in boxes.get(key, []) if x[0] != k]
        if '=' in w:
            k, nr = w.split('=', 1)
            nr = int(nr)
            key = hash(k)
            if k in [x[0] for x in boxes.get(key, [])]:
                boxes[key] = [x if k != x[0] else (k, nr) for x in boxes.get(key, [])]
            else:
                boxes[key] = boxes.get(key, []) + [(k, nr)]
    total = 0
    for k, v in boxes.items():
        for i, l in enumerate(v):
            total += (k + 1) * (i + 1) * l[1]
    print(total)


if __name__ == '__main__':
    main()
