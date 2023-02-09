import random
from rolls import get_rolls, get_choices_from_rolls
from board import Board
from datetime import datetime


if __name__ == '__main__':
    turn = 0
    random.seed(datetime.now())
    boards = [Board('x'), Board('o')]
    player_turn = 0
    rolls = []
    while turn != 20:
        print(turn)
        pawn = 3
        stop = False
        while pawn != 0 or stop is True:
            stop = random.choice([False, True])
            pawn -= 1
            choices = get_choices_from_rolls(get_rolls())
            for choice in choices:
                if not boards[player_turn].is_valid_move(choice):
                    choices.remove(choice)
            print(choices)
            if choices:
                boards[player_turn].put_climber(random.choice(choices))
                boards[player_turn].show_board()
        boards[player_turn].lock_snap_hook()
        boards[player_turn].show_board()
        if player_turn == 1:
            player_turn = 0
        else:
            player_turn = 1
        turn += 1
