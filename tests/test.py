import unittest

import json
import os

from .utils import *

from Dalaran.lexer import lex, token_exprs

from Dalaran.parser import parse_card, register_card


class Test_Cards(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'RecklessRocketeer.json')) as card:
            self.card_data = json.load(card)

    def test_tokenization(self):
        tokens = lex(self.card_data['text'], token_exprs)

        self.assertEqual(len(tokens), 1)

    def test_parsing(self):
        tokens = lex(self.card_data['text'], token_exprs)

        card = parse_card(self.card_data['name'], self.card_data['type'], self.card_data['cost'], self.card_data['class'],
                          tokens, self.card_data.get('attack', None), self.card_data.get('health', None))

        self.assertEqual(card.tags[GameTag.CHARGE], True)
        self.assertEqual(card.tags[GameTag.CARDNAME], 'Reckless Rocketeer')
        self.assertEqual(card.tags[GameTag.CARDTYPE], CardType.MINION)
        self.assertEqual(card.tags[GameTag.CLASS], CardClass.NEUTRAL)
        self.assertEqual(card.tags[GameTag.ATK], 5)
        self.assertEqual(card.tags[GameTag.HEALTH], 2)

    def test_playing(self):
        tokens = lex(self.card_data['text'], token_exprs)

        card = parse_card(self.card_data['name'], self.card_data['type'], self.card_data['cost'], self.card_data['class'],
                          tokens, self.card_data.get('attack', None), self.card_data.get('health', None))

        register_card(card)

        game = prepare_game(CardClass.WARRIOR, CardClass.WARRIOR)
        rocketeer = game.player1.give(card.__name__)

        rocketeer.play()

        self.assertTrue(rocketeer.can_attack())

        rocketeer.attack(game.current_player.opponent.hero)

        self.assertFalse(rocketeer.can_attack())
