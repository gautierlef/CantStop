import random
from rollsAndChoices import get_rolls, get_choices_from_rolls, clear_choices
from board import Board


if __name__ == '__main__':
    turn = 0
    random.seed()
    boards = [Board('x'), Board('o')]
    player_turn = 0
    rolls = []
    conquered_ways = []
    # Check if a player won
    while not boards[player_turn - 1 % 2].is_win():
        print('Player turn : ' + str(player_turn))
        print('Turn : ' + str(turn))
        climber = 3
        stop = False
        current_climbers_position = []
        # Continue playing until player stop his turn
        while stop is False:
            print('Climber remaining : ' + str(climber))
            # Decide if random player keeps playing
            stop = random.choice([False, True])
            rolls = get_rolls()
            print('Rolls : ' + str(rolls))
            choices = get_choices_from_rolls(rolls)
            print('Choices : ' + str(choices))
            choices = clear_choices(choices, boards[player_turn], conquered_ways)
            print('Valid choices : ' + str(choices))
            # Check if any valid choice available
            if choices:
                if len(choices) == 1:
                    for choice in choices[0]:
                        boards[player_turn].put_climber(choice)
                        if climber not in current_climbers_position and climber > 0:
                            climber -= 1
                            current_climbers_position.append(choice)
                else:
                    # Take a choice randomly
                    for choice in choices[random.randrange(0, len(choices))]:
                        boards[player_turn].put_climber(choice)
                        # Remove 1 to climber count and save his position if there was none in the way
                        if climber not in current_climbers_position and climber > 0:
                            climber -= 1
                            current_climbers_position.append(choice)
                boards[player_turn].show_board()
            else:
                # Remove climbers in case if no valid choice available
                boards[player_turn].remove_climbers()
                stop = True
                print('No valid choices : All climbers falls !')
        print('Player ' + str(player_turn) + ' finished is turn !')
        boards[player_turn].lock_snap_hook()
        # Save conquered ways
        way_number = 0
        for way in boards[player_turn].board:
            if way[-1] == boards[player_turn].character.capitalize() and way_number not in conquered_ways:
                conquered_ways.append(way_number)
            way_number += 1
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
