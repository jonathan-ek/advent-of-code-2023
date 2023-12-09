from utils import open_input


def main():
    instructions, nodes = open_input("08").split("\n\n", 1)
    node = "AAA"
    end = "ZZZ"
    nodes = dict([[y.strip("()").split(", ") if ',' in y else y for y in x.split(" = ", 1)] for x in nodes.split("\n")])
    i = 0
    c = 0
    while True:
        inst = 0 if instructions[i] == "L" else 1
        node = nodes[node][inst]
        c += 1
        if node == end:
            print(c)
            break
        i += 1
        i %= len(instructions)


if __name__ == '__main__':
    main()
