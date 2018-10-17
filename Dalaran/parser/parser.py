from fireplace.cards.utils import *


def parse_tokens(tokens):
    tags = {}

    pos = 0

    while pos <= len(tokens) - 1:
        token = tokens[pos]

        token_type = token[1]
        token_value = token[0]

        if token_type == "ABILITY":
            if all(token[1] == "ABILITY" for token in tokens[:pos]):
                tags[GameTag[token_value.upper()]] = True

        pos += 1

    return tags


def parse_card(name, type_, cost, class_, tokens, atk=None, health=None):
    tags = parse_tokens(tokens)

    tags[GameTag.CARDNAME] = name
    tags[GameTag.COST] = cost
    tags[GameTag.CARDTYPE] = type_ if isinstance(
        type_, CardType) else CardType[type_.upper()]
    tags[GameTag.CLASS] = class_ if isinstance(
        class_, CardClass) else CardClass[class_.upper()]

    if atk is not None:
        tags[GameTag.ATK] = atk

    if health is not None:
        tags[GameTag.HEALTH] = health

    card = type('CUSTOM_{}'.format(name), (), {"tags": tags})
    return card


def register_card(card):
    custom_card(card)
