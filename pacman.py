import random
from datetime import datetime


def create_pacmap():
    return [
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],    # 1
        ['o', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'o', 'x', 'o'],    # 2
        ['o', 'x', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'x', 'o'],    # 3
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],    # 4
        ['x', 'x', 'o', 'x', 'x', ' ', 'x', 'x', 'o', 'x', 'x'],    # 5
        ['C', 'o', 'o', 'x', ' ', ' ', ' ', 'x', 'o', 'o', 'o'],    # 6
        ['x', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'o', 'x', 'x'],    # 7
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],    # 8
        ['o', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'o', 'x', 'o'],    # 9
        ['o', 'x', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'x', 'o'],    # 10
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']     # 11
        # 1    2    3    4    5    6    7    8    9    10   11
    ]


def show_pacmap(pacmap):
    for column in pacmap:
        print(column)


def is_win(pacmap):
    for column in pacmap:
        if 'o' in column:
            return False
    return True


if __name__ == '__main__':
    random.seed()
    pacmap = create_pacmap()
    show_pacmap(pacmap)
    pacman_pos = [5, 0]
    pacman_last_pos = [5, 0]
    pacmap[pacman_pos[0]][pacman_pos[1]] = 'C'
    action_number = 1
    while not is_win(pacmap):
        print('Action number ' + str(action_number) + ' :')
        pacman_last_pos[0] = pacman_pos[0]
        pacman_last_pos[1] = pacman_pos[1]
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            if pacman_pos[0] != 0:
                if pacmap[pacman_pos[0] - 1][pacman_pos[1]] != 'x':
                    pacman_pos[0] += -1
        elif direction == 'right':
            if pacman_pos[0] != 10:
                if pacmap[pacman_pos[0] + 1][pacman_pos[1]] != 'x':
                    pacman_pos[0] += 1
        elif direction == 'up':
            if pacman_pos[1] != 0:
                if pacmap[pacman_pos[0]][pacman_pos[1] - 1] != 'x':
                    pacman_pos[1] += -1
        else:
            if pacman_pos[1] != 10:
                if pacmap[pacman_pos[0]][pacman_pos[1] + 1] != 'x':
                    pacman_pos[1] += 1
        if pacmap[pacman_pos[0]][pacman_pos[1]] != 'x':
            pacmap[pacman_last_pos[0]][pacman_last_pos[1]] = ' '
            pacmap[pacman_pos[0]][pacman_pos[1]] = 'C'
            show_pacmap(pacmap)
            action_number += 1
