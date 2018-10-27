from fireplace.cards.utils import *
from .utils import *

from pyleri import Optional


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
            node.children[0].element.name)('play')(node.children[0])

    @staticmethod
    def deal_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (
                Hit(TARGET, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def restore_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (
                Heal(TARGET, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def armor_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (GainArmor(
                FRIENDLY_HERO, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def mana_crystal_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            if isinstance(node.children[2].element, Optional):
                res[event] = GainEmptyMana(
                    CONTROLLER, string_to_num(node.children[1].string))

            else:
                res[event] = (GainMana(
                    CONTROLLER, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def draw_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (Draw(CONTROLLER) *
                          string_to_num(node.children[1].string),)

            return res

        return handler

    @staticmethod
    def discard_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (Discard(CONTROLLER) *
                          string_to_num(node.children[1].string),)

            return res

        return handler

    @staticmethod
    def freeze_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (Freeze(TARGET),)

            return res

        return handler

    @staticmethod
    def destroy_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res[event] = (Destroy(TARGET),)

            return res

        return handler

    @staticmethod
    def ability_sequence_handler(event='play'):
        def handler(node, event=event):
            res = {}

            res['tags'] = {}
            res['tags'][ability_to_enum(sequence.children[0].string)] = True

            return res

        return handler
