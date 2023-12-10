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
            break
    # replace S
    last_node = visited[-1]
    new_s = None
    if last_node[0] == s[0]:
        if last_node[1] < s[1]:
            # last node above s
            new_s = {90: 'L', 180: '|', 270: 'J'}[start_direction]
        else:
            # last node under s
            new_s = {90: 'F', 0: '|', 270: '7'}[start_direction]
    else:
        if last_node[0] < s[0]:
            # last node left of s
            new_s = {0: 'J', 90: '-', 180: '7'}[start_direction]
        else:
            # last node right of s
            new_s = {0: 'L', 270: '-', 180: 'F'}[start_direction]
    inp_map[s[1]][s[0]] = new_s
    enclosed = 0
    for y, row in enumerate(inp_map):
        border_count = 0
        last_turn = None
        for x, val in enumerate(row):
            if (x, y) in visited:
                sym = inp_map[y][x]
                if sym == '-':
                    continue
                if (last_turn == 'F' and sym == '7') or (last_turn == 'L' and sym == 'J'):
                    border_count += 1
                if sym in ['F', 'L']:
                    last_turn = sym
                if sym in ['7', 'J']:
                    last_turn = None
                if sym in ['F', 'L', '|']:
                    border_count += 1
                continue
            if border_count % 2 == 1:
                # print((x, y), '|' if (x, y) in visited else '.', border_count)
                enclosed += 1
    print(enclosed)


if __name__ == '__main__':
    main()
