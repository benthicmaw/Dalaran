from fireplace.cards.utils import *
from .utils import *


class Hearthstone_Parser:
    @classmethod
    def parse_tree(cls, tree):
        res = {}

        root = tree.tree.children[0]
        sequences = [el.children[0] for el in root.children]

        for sequence in sequences:
            handler = cls.get_sequence_handler(
                sequence.element.name)

            if handler is not None:
                new = handler(sequence)

                deep_merge(res, new)

        return res

    @classmethod
    def get_sequence_handler(cls, name):
        handler = getattr(cls, name + '_handler', None)
        return handler if callable(handler) else None

    @classmethod
    def action_sequence_handler(cls, node):
        return cls.get_sequence_handler(
            node.children[0].element.name)(node.children[0])

    @staticmethod
    def deal_sequence_handler(node):
        res = {}

        res['play'] = (
            Hit(TARGET, string_to_num(node.children[1].string)),)

        return res

    @staticmethod
    def armor_sequence_handler(node):
        res = {}

        res['play'] = (
            GainArmor(CONTROLLER, string_to_num(node.children[1].string)),)

        return res

    @staticmethod
    def draw_sequence_handler(node):
        res = {}

        res['play'] = (Draw(CONTROLLER) *
                       string_to_num(node.children[1].string),)

        return res

    @staticmethod
    def discard_sequence_handler(node):
        res = {}

        res['play'] = (Discard(CONTROLLER) *
                       string_to_num(node.children[1].string),)

        return res

    @staticmethod
    def freeze_sequence_handler(node):
        res = {}

        res['play'] = (Freeze(TARGET),)

        return res

    @staticmethod
    def destroy_sequence_handler(node):
        res = {}

        res['play'] = (Destroy(TARGET),)

        return res

    @staticmethod
    def ability_sequence_handler(node):
        res = {}

        if res.get('tags') is None:
            res['tags'] = {}

        res['tags'][ability_to_enum(sequence.children[0].string)] = True

        return res
