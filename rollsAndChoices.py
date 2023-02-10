import random


def get_rolls():
    rolls = []
    for i in range(4):
        rolls.append(random.randrange(1, 7))
    return rolls


def get_choices_from_rolls(rolls):
    choices = []
    combinations = [
        rolls[0] + rolls[1],
        rolls[0] + rolls[2],
        rolls[0] + rolls[3],
        rolls[1] + rolls[2],
        rolls[1] + rolls[3],
        rolls[2] + rolls[3]
    ]
    choices.append([combinations[0], combinations[5]])
    choices.append([combinations[1], combinations[4]])
    choices.append([combinations[2], combinations[3]])
    return choices


def clear_choices(choices, board):
    for choice in choices:
        if choice[0] == choice[1]:
            if not board.is_valid_move(choice[0]):
                choice.remove(choice[1])
                choice.remove(choice[0])
            else:
                board.put_climber(choice[0])
                if not board.is_valid_move(choice[1]):
                    choice.remove(choice[1])
                index = board.board[choice[0] - 2].index(board.character)
                if index != 0:
                    board.board[choice[0] - 2][index - 1] = board.character
                board.board[choice[0] - 2][index] = '-'
                board.show_board()
        else:
            if not board.is_valid_move(choice[1]):
                choice.remove(choice[1])
            if not board.is_valid_move(choice[0]):
                choice.remove(choice[0])
    choices = list(filter(None, choices))
    return choices
