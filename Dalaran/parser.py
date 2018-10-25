from fireplace.cards.utils import *
from .utils import *


def parse_tree(tree):
    res = {}

    root = tree.tree.children[0]
    sequences = [el.children[0] for el in root.children]

    for sequence in sequences:
        if sequence.element.name == 'action_sequence':
            sequence = sequence.children[0]

        if sequence.element.name == 'deal_sequence':
            if res.get('play') is None:
                res['play'] = (
                    Hit(TARGET, string_to_num(sequence.children[1].string)),)

            else:
                res['play'] += (Hit(TARGET,
                                    string_to_num(sequence.children[1].string)),)

        elif sequence.element.name == 'draw_sequence':
            if res.get('play') is None:
                res['play'] = (Draw(CONTROLLER) *
                               string_to_num(sequence.children[1].string),)

            else:
                res['play'] += (Draw(CONTROLLER) *
                                string_to_num(sequence.children[1].string),)

    return res
