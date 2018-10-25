from fireplace.cards.utils import *


def string_to_num(el):
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'a': 1, 'an': 1}

    return int(el) if el.isdigit() else numbers[el]


def ability_to_enum(el):
    return GameTag[el.upper()]
