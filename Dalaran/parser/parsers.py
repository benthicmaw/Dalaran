from fireplace.cards.utils import *
from .utils import *

Deal = Hit


def parse_action(token, iterator, **kwargs):
    token_value = token[0]

    target = kwargs.get('target', None)
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

    if target is None:
        if action is Draw or action is Discard:
            target = CONTROLLER

        if (action is Silence or action is Destroy or
                action is Heal or action is Deal):
            target = TARGET

    if action is Draw or action is Discard:
        return action(target) * amount

    elif action is Deal or action is Heal:
        return action(target, amount)

    elif action is Silence or action is Destroy:
        return action(target)
