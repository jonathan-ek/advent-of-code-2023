from utils import open_input


def main():
    inp = open_input("15").split(",")
    total = 0
    for w in inp:
        val = 0
        for c in w:
            ascii_val = ord(c)
            val += ascii_val
            val = val * 17
            val = val % 256
        total += val
    print(total)


if __name__ == '__main__':
    main()
