from utils import open_input


def main():
    inp_map = [list(x) for x in open_input("10").split("\n")]
    s = None
    x_min = 0
    x_max = len(inp_map[0]) - 1
    y_min = 0
    y_max = len(inp_map) - 1

    def can_go_left(x_int, y_int):
        return x_int > x_min and inp_map[y_int][x_int - 1] in ['-', 'F', 'L', 'S']

    def can_go_right(x_int, y_int):
        return x_int < x_max and inp_map[y_int][x_int + 1] in ['-', '7', 'J', 'S']

    def can_go_up(x_int, y_int):
        return y_int > y_min and inp_map[y_int - 1][x_int] in ['|', '7', 'F', 'S']

    def can_go_down(x_int, y_int):
        return y_int < y_max and inp_map[y_int + 1][x_int] in ['|', 'L', 'J', 'S']

    def get_dir(new_node, old_direction):
        if inp_map[new_node[1]][new_node[0]] == 'S':
            return -1
        if old_direction == 0:  # up
            return {'|': 0, '7': 270, 'F': 90}[inp_map[new_node[1]][new_node[0]]]
        if old_direction == 90:  # right
            return {'-': 90, '7': 180, 'J': 0}[inp_map[new_node[1]][new_node[0]]]
        if old_direction == 180:  # down
            return {'|': 180, 'L': 90, 'J': 270}[inp_map[new_node[1]][new_node[0]]]
        if old_direction == 270:  # left
            return {'-': 270, 'L': 0, 'F': 180}[inp_map[new_node[1]][new_node[0]]]

    for y, row in enumerate(inp_map):
        for x, val in enumerate(row):
            if val == "S":
                s = (x, y)
    start_direction = 0
    visited = []
    while True:
        visited = []
        node = s
        direction = start_direction
        while True:
            visited.append(node)
            if direction == 0 and can_go_up(*node):
                next_node = (node[0], node[1] - 1)
            elif direction == 90 and can_go_right(*node):
                next_node = (node[0] + 1, node[1])
            elif direction == 180 and can_go_down(*node):
                next_node = (node[0], node[1] + 1)
            elif direction == 270 and can_go_left(*node):
                next_node = (node[0] - 1, node[1])
            else:
                break
            direction = get_dir(next_node, direction)
            if direction == -1:
                break
            node = next_node
        if direction != -1:
            start_direction += 90
        else:
            visited.append(s)
            break
    print(int(len(visited) / 2))


if __name__ == '__main__':
    main()
