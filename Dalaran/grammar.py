import re

from pyleri import *


class HearthstoneGrammar(Grammar):

    RE_KEYWORDS = re.compile('^[A-Za-z:]+')

    # NUMBERS

    number_words = Choice(
        Keyword('one', ign_case=True),
        Keyword('two', ign_case=True),
        Keyword('three', ign_case=True),
        Keyword('four', ign_case=True),
        Keyword('five', ign_case=True),
        Keyword('six', ign_case=True),
        Keyword('seven', ign_case=True),
        Keyword('eight', ign_case=True),
        Keyword('nine', ign_case=True),
        Keyword('ten', ign_case=True))

    special_number_words = Choice(
        Keyword('a', ign_case=True), Keyword('an', ign_case=True))

    numbers_digits = Regex('[0-9]+')

    number = Choice(numbers_digits, number_words, special_number_words)

    # ACTIONS

    destroy = Keyword('destroy', ign_case=True)
    deal = Keyword('deal', ign_case=True)
    draw = Regex('(D|d)raws?')
    freeze = Keyword('freeze', ign_case=True)
    gain = Regex('(G|g)ains?')
    discard = Regex('(D|d)iscards? ')
    restore = Keyword('restore', ign_case=True)

    # action = Choice(destroy, deal, draw, freeze, gain, discard, restore)

    # ABILITIES

    # spell_damage = Keyword('spell damage', ign_case=True)

    charge = Keyword('charge', ign_case=True)
    taunt = Keyword('taunt', ign_case=True)
    divine_shield = Keyword('shield', ign_case=True)
    windfury = Keyword('windfury', ign_case=True)

    ability = Choice(charge, taunt, divine_shield, windfury)

    # EVENTS

    battlecry = Keyword('battlecry:', ign_case=True)
    """
    deathrattle = Keyword('deathrattle:', ign_case=True)

    event = Choice(battlecry, deathrattle)
    """

    # TARGETS

    # character = Choice(Keyword('character', ign_case=True),
    #                   Keyword('characters', ign_case=True))

    minion = Choice(Keyword('minion', ign_case=True),
                    Keyword('minions', ign_case=True))
    hero = Keyword('hero', ign_case=True)

    your_opponent = Regex('(Y|y)our (O|o)pponent')
    your_hero = Regex('(Y|y)our (H|h)ero')

    target = Choice(your_opponent,
                    your_hero,
                    Sequence(
                       Keyword('a', ign_case=True),
                       minion),
                    Sequence(
                       Keyword('a', ign_case=True),
                       hero))
    """
    owner = Keyword('owner', ign_case=True)

    target = Choice(character, minion, opponent, owner)
    """

    # MODIFIERS

    empty = Keyword('empty', ign_case=True)

    """
    friendly = Keyword('friendly', ign_case=True)
    enemy = Keyword('enemy', ign_case=True)
    all_ = Keyword('all', ign_case=True)

    modifier = Choice(friendly, enemy, all_)
    """

    # FIELDS

    card = Choice(Keyword('card', ign_case=True),
                  Keyword('cards', ign_case=True))
    damage = Keyword('damage', ign_case=True)
    armor = Keyword('armor', ign_case=True)
    health = Keyword('health', ign_case=True)
    mana_crystals = Regex('(M|m)ana (C|c)rystals?')

    # field = Choice(card, damage, armor, health)

    # SEQUENCES

    draw_sequence = Sequence(draw, number, card)
    discard_sequence = Sequence(discard, number, card)
    deal_sequence = Sequence(deal, number, damage)
    restore_sequence = Sequence(restore, number, health)
    armor_sequence = Sequence(gain, number, armor)
    mana_crystal_sequence = Sequence(
        gain, number, Optional(empty), mana_crystals)
    destroy_sequence = Sequence(destroy, minion)
    freeze_sequence = Sequence(freeze, minion)

    hero_actions = Choice(
        armor_sequence, mana_crystal_sequence, discard_sequence, draw_sequence)
    other_actions = Choice(deal_sequence, restore_sequence,
                           destroy_sequence, freeze_sequence)

    opponent_targeted_sequence = Sequence(your_opponent, hero_actions)
    targeted_other_action = Sequence(other_actions,
                                     Keyword('to', ign_case=True),
                                     target)

    action_sequence = Choice(targeted_other_action,
                             opponent_targeted_sequence,
                             hero_actions,
                             other_actions)

    ability_sequence = Sequence(ability)

    battlecry_sequence = Sequence(battlecry, action_sequence)

    skip_chars = Regex('\.')

    # MAIN

    # ID = Regex("[A-Za-z][A-Za-z0-9\']*")

    START = Repeat(Choice(action_sequence,
                          ability_sequence,
                          battlecry_sequence,
                          skip_chars), 0)
