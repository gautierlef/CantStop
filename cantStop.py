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
    while not boards[player_turn].is_win():
        print('Player turn : ' + str(player_turn))
        print('Turn : ' + str(turn))
        pawn = 3
        stop = False
        while pawn != 0 and stop is False:
            print('Pawn remaining : ' + str(pawn))
            stop = random.choice([False, True])
            pawn -= 1
            rolls = get_rolls()
            print('Rolls :' + str(rolls))
            choices = get_choices_from_rolls(rolls)
            print('Choices : ' + str(choices))
            i = 0
            while i != len(choices):
                i += 1
                if not boards[player_turn].is_valid_move(choices[i - 1]):
                    choices.remove(choices[i - 1])
                    i = 0
            print('Valid choices : ' + str(choices))
            if choices:
                boards[player_turn].put_climber(random.choice(choices))
                boards[player_turn].show_board()
            else:
                boards[player_turn].remove_climber()
                stop = True
        print('Player ' + str(player_turn) + ' finished is turn !')
        boards[player_turn].lock_snap_hook()
        boards[player_turn].show_board()
        if player_turn == 1:
            player_turn = 0
        else:
            player_turn = 1
        turn += 1
    if player_turn == 1:
        player_turn = 0
    else:
        player_turn = 1
    print('Player ' + str(player_turn) + ' has won at turn ' + str(turn) + '!')
