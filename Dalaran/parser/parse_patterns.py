from fireplace.cards.utils import *
from .utils import *

Deal = Hit
Gain = TargetedAction


def parse_action(token, iterator, **kwargs):
    token_value = token[0]

    target = kwargs.get('target', None)

    action = parse_action_token(token_value)

    token = iterator.next()

    token_type = token[1]
    token_value = token[0]

    assert token_type == 'INT'

    amount = parse_int_token(token_value)

    token = iterator.next()

    token_type = token[1]
    token_value = token[0]

    assert (token_type == 'FIELD' or token_type == 'MODIFIER' or
            token_type == 'TARGET')

    if action is Draw or action is Discard:
        assert token_type == 'FIELD'
        assert token_value.casefold().startswith('card')

    elif action is Silence or action is Destroy:
        assert token_type == 'TARGET'
        assert token_value.casefold().startswith('minion')

    elif action is Heal:
        assert token_type == 'FIELD'
        assert token_value.casefold() == 'health'

    elif action is Deal:
        assert token_type == 'FIELD'
        assert token_value.casefold() == 'damage'

    elif action is Gain:
        assert token_type == 'MODIFIER' or token_type == 'FIELD'

        if token_type == 'FIELD':
            assert (token_value.casefold() ==
                    'armor' or token_value.casefold() == 'mana crystal')

            if token_value.casefold() == 'armor':
                action = GainArmor

            elif token_value.casefold() == 'mana crystal':
                action = GainMana

        elif token_type == 'MODIFIER':
            assert token_value.casefold() == 'empty'

            token = iterator.next()

            token_type = token[1]
            token_value = token[0]

            assert token_type == 'FIELD'
            assert token_value.casefold() == 'mana crystal'

            action = GainEmptyMana

    try:
        token = iterator.next()

        token_type = token[1]
        token_value = token[0]

        if token_type == 'MODIFIER':
            modifier = token_value

            try:
                token = iterator.next()

                token_type = token[1]
                token_value = token[0]

                targets = token_value

            except StopIteration as e:
                raise e

            target = parse_target(modifier, targets)

        else:
            iterator.prev()

    except StopIteration:
        pass

    if target is None:
        if (action is Draw or action is Discard
                or action is GainEmptyMana or action is GainMana):
            target = CONTROLLER

        elif (action is Silence or action is Destroy or
                action is Heal or action is Deal):
            target = TARGET

        elif action is GainArmor:
            target = FRIENDLY_HERO

    if action is Draw or action is Discard:
        return action(target) * amount

    elif (action is Deal or action is Heal or action is GainArmor or action
          is GainEmptyMana or action is GainMana):
        return action(target, amount)

    elif action is Silence or action is Destroy:
        return action(target)


def parse_int_token(token):
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'a': 1, 'an': 1}

    return int(token) if token.isdigit() else numbers[token]


def parse_action_token(token):
    action = globals().get(token.lower().capitalize(), None)
    assert isinstance(action, ActionMeta)

    return action


def parse_target(modifier, targets):
    target = globals().get('_'.join((modifier, targets),).upper(), None)
    assert isinstance(target, SetOpSelector)

    return target
