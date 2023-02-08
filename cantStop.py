import random
from rolls import get_rolls, get_choices_from_rolls
from board import Board
from datetime import datetime


if __name__ == '__main__':
    turn = 0
    random.seed(datetime.now())
    boards = [Board(), Board()]
    player_turn = 0
    while turn != 10:
        print(turn)
        choices = get_choices_from_rolls(get_rolls())
        boards[player_turn].put_climber(random.choice(choices), player_turn)
        boards[player_turn].show_board()
        boards[player_turn].lock_snap_hook()
        boards[player_turn].show_board()
        if player_turn == 1:
            player_turn = 0
        else:
            player_turn = 1
        turn += 1
