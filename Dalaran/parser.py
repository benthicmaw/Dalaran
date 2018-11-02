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
        print(node.children[0].element.name)
        return cls.get_sequence_handler(
            node.children[0].element.name)('play')(node.children[0])

    @classmethod
    def battlecry_sequence_handler(cls, node):
        return cls.get_sequence_handler(
            node.children[1].children[0].element.name)('play')(node.children[1].children[0])

    @classmethod
    def opponent_targeted_sequence_handler(cls, event='play'):
        def handler(node, event=event):
            handler = cls.get_sequence_handler(
                node.children[1].children[0].element.name)

            if (handler.__defaults__[
                    handler.__code__.co_varnames.index('target')] == FRIENDLY_HERO):
                return handler(
                    event, ENEMY_HERO)(node.children[1].children[0])

            elif (handler.__defaults__[
                    handler.__code__.co_varnames.index('target')] == CONTROLLER):
                return handler(event, OPPONENT)(node.children[1].children[0])

        return handler

    @classmethod
    def hero_targeted_other_action_handler(cls, event='play'):
        def handler(node, event=event):
            handler = cls.get_sequence_handler(
                node.children[0].children[0].element.name)

            target_hero = (
                FRIENDLY_HERO if node.children[2].children[0].element.name == 'your_hero' else ENEMY_HERO)

            return handler(event, target_hero)(node.children[0].children[0])

        return handler

    @classmethod
    def hero_actions_handler(cls, event='play'):
        def handler(node, event=event):
            return cls.get_sequence_handler(
                node.children[0].element.name)(event)(node.children[0])

        return handler

    @classmethod
    def other_actions_handler(cls, event='play'):
        def handler(node, event=event):
            return cls.get_sequence_handler(
                node.children[0].element.name)(event)(node.children[0])

        return handler

    @staticmethod
    def deal_sequence_handler(event='play', target=TARGET):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (
                Hit(target, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def restore_sequence_handler(event='play', target=TARGET):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (
                Heal(target, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def armor_sequence_handler(event='play', target=FRIENDLY_HERO):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (GainArmor(
                target, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def mana_crystal_sequence_handler(event='play', target=CONTROLLER):
        def handler(node, event=event, target=target):
            res = {}

            if len(node.children) == 4:
                res[event] = GainEmptyMana(
                    target, string_to_num(node.children[1].string))

            else:
                res[event] = (GainMana(
                    target, string_to_num(node.children[1].string)),)

            return res

        return handler

    @staticmethod
    def draw_sequence_handler(event='play', target=CONTROLLER):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (Draw(target) *
                          string_to_num(node.children[1].string),)

            return res

        return handler

    @staticmethod
    def discard_sequence_handler(event='play', target=CONTROLLER):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (Discard(target) *
                          string_to_num(node.children[1].string),)

            return res

        return handler

    @staticmethod
    def freeze_sequence_handler(event='play', target=TARGET):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (Freeze(target),)

            return res

        return handler

    @staticmethod
    def destroy_sequence_handler(event='play', target=TARGET):
        def handler(node, event=event, target=target):
            res = {}

            res[event] = (Destroy(target),)

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
