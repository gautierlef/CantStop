import random
from rollsAndChoices import get_rolls, get_choices_from_rolls, clear_choices
from board import Board
from datetime import datetime


if __name__ == '__main__':
    turn = 0
    random.seed(datetime.now())
    boards = [Board('x'), Board('o')]
    player_turn = 0
    rolls = []
    while not boards[player_turn - 1 % 2].is_win():
        print('Player turn : ' + str(player_turn))
        print('Turn : ' + str(turn))
        climber = 3
        stop = False
        while climber > 0 and stop is False:
            print('Climber remaining : ' + str(climber))
            stop = random.choice([False, True])
            rolls = get_rolls()
            print('Rolls : ' + str(rolls))
            choices = get_choices_from_rolls(rolls)
            print('Choices : ' + str(choices))
            choices = clear_choices(choices, boards[player_turn])
            print('Valid choices : ' + str(choices))
            if choices:
                if len(choices) == 1:
                    for choice in choices[0]:
                        boards[player_turn].put_climber(choice)
                        climber -= 1
                else:
                    for choice in choices[random.randrange(0, len(choices))]:
                        boards[player_turn].put_climber(choice)
                        climber -= 1
                boards[player_turn].show_board()
            else:
                boards[player_turn].remove_climbers()
                stop = True
                print('No valid choices : All climbers falls !')
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
