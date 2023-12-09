from utils import open_input


def main():
    instructions, nodes = open_input("08").split("\n\n", 1)
    nodes = dict([[y.strip("()").split(", ") if ',' in y else y for y in x.split(" = ", 1)] for x in nodes.split("\n")])
    current_nodes = [x for x in nodes.keys() if x[2] == "A"]
    end_nodes = [x for x in nodes.keys() if x[2] == "Z"]
    i = 0
    nr_of_nodes = len(current_nodes)
    a = 0
    b = 0
    c = 0

    a_set = False
    b_set = False
    c_set = False
    while True:
        inst = 0 if instructions[i] == "L" else 1
        for node_index in range(len(current_nodes)):
            current_nodes[node_index] = nodes[current_nodes[node_index]][inst]
        if not a_set:
            a += 1
        if not b_set:
            b += 1
        if not c_set:
            c += 1
        if all([x in end_nodes for x in current_nodes[0:int(nr_of_nodes / 3)]]):
            print("1", a)
            a_set = True
        if all([x in end_nodes for x in current_nodes[int(nr_of_nodes / 3):int(nr_of_nodes / 3)*2]]):
            print("2", b)
            b_set = True
        if all([x in end_nodes for x in current_nodes[int(nr_of_nodes / 3)*2:]]):
            print("3", c)
            c_set = True
        if a_set and b_set and c_set:
            break
        i += 1
        i %= len(instructions)
    j = 0
    m = max([a, b, c])
    while True:
        j += 1
        r = m * j
        if r % a == 0 and r % b == 0 and r % c == 0:
            print(r)
            break


if __name__ == '__main__':
    main()
