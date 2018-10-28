from dalaran.parser import Hearthstone_Parser
from dalaran.grammar import Hearthstone_Grammar

from fireplace.cards.utils import *
from .utils import deep_merge


class Dalaran:
    def __init__(self,
                 grammar_class=Hearthstone_Grammar,
                 parser_class=Hearthstone_Parser):
        self.grammar = grammar_class()
        self.parser = parser_class()

    def parse_card(self, name, type_, cost, class_, text,
                   atk=None, health=None):
        type_ = type_ if isinstance(
            type_, CardType) else CardType[type_.upper()]
        class_ = class_ if isinstance(
            class_, CardClass) else CardClass[class_.upper()]

        attributes = {'tags': {}}

        attributes['tags'][GameTag.CARDNAME] = name
        attributes['tags'][GameTag.COST] = cost
        attributes['tags'][GameTag.CARDTYPE] = type_
        attributes['tags'][GameTag.CLASS] = class_

        if atk is not None:
            attributes['tags'][GameTag.ATK] = int(atk)

        if health is not None:
            attributes['tags'][GameTag.HEALTH] = int(health)

        res = self.parse_text(text)
        deep_merge(attributes, res)

        card = type('CUSTOM_' + name, (), attributes)

        return card

    def parse_text(self, text):
        tree = self.grammar.parse(text)
        res = self.parser.parse_tree(tree)

        return res

    def register_card(self, cls):
        custom_card(cls)
