import re

from pyleri import *


class Numbers:
    number_words = Choice(Keyword('one', ign_case=True), Keyword('two', ign_case=True), Keyword('three', ign_case=True), Keyword('four', ign_case=True), Keyword(
        'five', ign_case=True), Keyword('six', ign_case=True), Keyword('seven', ign_case=True), Keyword('eight', ign_case=True), Keyword('nine', ign_case=True), Keyword('ten', ign_case=True))

    special_number_words = Choice(
        Keyword('a', ign_case=True), Keyword('an', ign_case=True))

    numbers_digits = Regex('[0-9]+')

    number = Choice(numbers_digits, number_words, special_number_words)


class Actions:
    destroy = Keyword('destroy', ign_case=True)
    deal = Keyword('deal', ign_case=True)
    draw = Keyword('draw', ign_case=True)
    freeze = Keyword('freeze', ign_case=True)
    gain = Keyword('gain', ign_case=True)
    discard = Keyword('discard', ign_case=True)

    action = Choice(destroy, deal, draw, freeze, gain, discard)


class Abilities:
    spell_damage = Keyword('spell damage', ign_case=True)

    charge = Keyword('charge', ign_case=True)
    taunt = Keyword('taunt', ign_case=True)
    divine_shield = Keyword('shield', ign_case=True)
    windfury = Keyword('windfury', ign_case=True)

    ability = Choice(charge, taunt, divine_shield, windfury)


class Events:
    battlecry = Keyword('battlecry:', ign_case=True)
    deathrattle = Keyword('deathrattle:', ign_case=True)

    event = Choice(battlecry, deathrattle)


class Targets:
    character = Choice(Keyword('character', ign_case=True),
                       Keyword('characters', ign_case=True))

    minion = Choice(Keyword('minion', ign_case=True),
                    Keyword('minions', ign_case=True))

    opponent = Keyword('opponent', ign_case=True)
    owner = Keyword('owner', ign_case=True)

    target = Choice(character, minion, opponent, owner)


class Modifiers:
    friendly = Keyword('friendly', ign_case=True)
    enemy = Keyword('enemy', ign_case=True)
    all_ = Keyword('all', ign_case=True)

    modifier = Choice(friendly, enemy, all_)


class Fields:
    card = Choice(Keyword('card', ign_case=True),
                  Keyword('cards', ign_case=True))
    damage = Keyword('damage', ign_case=True)
    armor = Keyword('armor', ign_case=True)

    field = Choice(card, damage, armor)


class Sequences(Numbers, Actions, Abilities, Events, Targets,
                Modifiers, Fields):
    draw_sequence = Sequence(Actions.draw, Numbers.number, Fields.card)
    discard_sequence = Sequence(Actions.discard, Numbers.number, Fields.card)
    deal_sequence = Sequence(Actions.deal, Numbers.number, Fields.damage)
    destroy_sequence = Sequence(Actions.destroy, Targets.minion)
    freeze_sequence = Sequence(Actions.freeze, Targets.minion)

    action_sequence = Choice(draw_sequence, discard_sequence,
                             deal_sequence, destroy_sequence, freeze_sequence)

    ability_sequence = Sequence(Abilities.ability)


class Main(Grammar, Sequences):
    # ID = Regex("[A-Za-z][A-Za-z0-9\']*")

    START = Repeat(Choice(Sequences.action_sequence,
                          Sequences.ability_sequence), 0)
