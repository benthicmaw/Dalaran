from fireplace.cards.utils import *
from .utils import *

Deal = Hit


def parse_action(token, iterator, **kwargs):
    token_value = token[0]

    target = kwargs.get('target', None)
    action = globals().get(token_value.lower().capitalize(), None)
    assert isinstance(action, ActionMeta)

    next_token = next(iterator)

    token_type = next_token[1]
    token_value = next_token[0]

    assert token_type == 'FIELD' or token_type == 'INT'

    if token_type == 'FIELD':
        amount = 1

    elif token_type == 'INT':
        if token_value.isdigit():
            amount = int(token_value)

        else:
            amount = word_to_num(token_value)

        next_token = next(iterator)

        token_type = next_token[1]
        token_value = next_token[0]

        assert token_type == 'FIELD' or token_type == 'TARGET'

        if action is Draw or action is Discard:
            assert token_value.lower().startswith('card')

        elif action is Silence or action is Destroy:
            assert token_value.lower().startswith('minion')

        elif action is Heal:
            assert token_value.lower() == 'health'

        elif action is Deal:
            assert token_value.lower() == 'damage'

    if target is None:
        if action is Draw or action is Discard:
            target = CONTROLLER

        elif (action is Silence or action is Destroy or
                action is Heal or action is Deal):
            target = TARGET

    if action is Draw or action is Discard:
        return action(target) * amount

    elif action is Deal or action is Heal:
        return action(target, amount)

    elif action is Silence or action is Destroy:
        return action(target)
