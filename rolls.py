import random


def get_rolls():
    rolls = []
    for i in range(4):
        rolls.append(random.randrange(1, 6))
    return rolls


def get_choices_from_rolls(rolls):
    choices = []
    for roll in rolls:
        other_rolls = rolls
        other_rolls.remove(roll)
        for other_roll in other_rolls:
            choices.append(roll + other_roll)
    return list(dict.fromkeys(choices))
