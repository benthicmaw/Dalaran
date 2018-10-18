from fireplace.cards.utils import *
from .utils import *


def parse_action(token, iterator, **kwargs):
    token_value = token[0]

    action = globals().get(token_value.lower().capitalize(), None)
    assert isinstance(action, ActionMeta)

    next_token = next(iterator)

    if next_token[1] == 'FIELD':
        amount = 1

    elif next_token[1] == 'INT':
        if next_token[0].isdigit():
            amount = int(next_token[0])

        else:
            amount = word_to_num(next_token[0])

        next(iterator)

    return action(kwargs.get('target', CONTROLLER)) * amount
