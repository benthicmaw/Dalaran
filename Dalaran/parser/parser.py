from fireplace.cards.utils import *

from .utils import *


def parse_tokens(tokens):
    tags = {}
    attributes = {}

    tokens = iter(tokens)

    in_ability_block = True

    while True:
        try:
            token = next(tokens)

        except StopIteration:
            break

        token_type = token[1]
        token_value = token[0]

        if token_type == 'ABILITY':
            if in_ability_block:
                tags[GameTag[token_value.upper()]] = True

        elif token_type == 'ACTION':
            in_ability_block = False

            action = globals().get(token_value.lower().capitalize(), None)
            assert isinstance(action, ActionMeta)

            target = CONTROLLER

            next_token = next(tokens)

            if next_token[1] == 'FIELD':
                amount = 1

            elif next_token[1] == 'INT':
                if next_token[0].isdigit():
                    amount = int(next_token[0])

                else:
                    amount = word_to_num(next_token[0])

                next(tokens)

            attributes['play'] = action(target) * amount

    return tags, attributes


def parse_card(name, type_, cost, class_, tokens, atk=None, health=None):
    tags, attributes = parse_tokens(tokens)

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

    values = {'tags': tags}
    values.update(attributes)

    card = type('CUSTOM_{}'.format(name), (), values)
    return card


def register_card(card):
    custom_card(card)
