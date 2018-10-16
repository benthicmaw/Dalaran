from fireplace.cards.utils import *


def parse(tokens):
    tags = {}
    return tags


def add_card(name, type_, cost, tokens, atk=0, health=0):
    tags = parse(tokens)
    card = type(name, {}, {"tags": tags})
    custom_card(card)
