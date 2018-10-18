import unittest

from Dalaran.utils import *

from Dalaran.lexer import lex, token_exprs
from Dalaran.parser import parse_card, register_card


class Test_Cards(unittest.TestCase):
    def test_tokenization(self):
        tokens = lex('draw two cards.', token_exprs)

        self.assertListEqual(
            tokens, [('draw', 'ACTION'), ('two', 'INT'), ('cards', 'FIELD')])

    def test_parsing(self):
        tokens = lex('Charge. Windfury.', token_exprs)

        card = parse_card('Charge Windfury Boi', 'Minion', 4, 'Neutral',
                          tokens, 3, 2)

        self.assertDictEqual({GameTag.CHARGE: True, GameTag.WINDFURY: True, GameTag.CARDNAME: 'Charge Windfury Boi', GameTag.COST: 4,
                              GameTag.CARDTYPE: CardType.MINION, GameTag.CLASS: CardClass.NEUTRAL, GameTag.ATK: 3, GameTag.HEALTH: 2}, card.tags)

    def test_card_abilities(self):
        tokens = lex('Charge. Windfury.', token_exprs)

        card = parse_card('Charge Windfury Boi', 'Minion', 4, 'Neutral',
                          tokens, 3, 2)

        register_card(card)

        game = prepare_game(CardClass.WARRIOR, CardClass.WARRIOR)
        charge_boi = game.player1.give(card.__name__)

        charge_boi.play()

        self.assertTrue(charge_boi.can_attack())

        charge_boi.attack(game.current_player.opponent.hero)

        self.assertTrue(charge_boi.can_attack())

        charge_boi.attack(game.current_player.opponent.hero)

        self.assertFalse(charge_boi.can_attack())

    def test_controller_actions(self):
        tokens = lex('Draw a Card', token_exprs)
        card_1 = parse_card('a', CardType.SPELL, 2, CardClass.MAGE, tokens)

        tokens = lex('Draw two Cards', token_exprs)
        card_2 = parse_card('two', CardType.SPELL, 3, CardClass.MAGE, tokens)

        tokens = lex('Draw 2 Cards', token_exprs)
        card_3 = parse_card('2', CardType.SPELL, 3, CardClass.MAGE, tokens)

        register_card(card_1)
        register_card(card_2)
        register_card(card_3)

        game = prepare_game(CardClass.MAGE, CardClass.MAGE)

        self.assertEqual(len(game.current_player.hand), 4)

        a = game.player1.give(card_1.__name__)
        two = game.player1.give(card_2.__name__)
        number_two = game.player1.give(card_3.__name__)

        self.assertEqual(len(game.current_player.hand), 7)
        self.assertEqual(game.current_player.cards_drawn_this_turn, 1)

        a.play()

        self.assertEqual(len(game.current_player.hand), 7)
        self.assertEqual(game.current_player.cards_drawn_this_turn, 2)

        two.play()

        self.assertEqual(len(game.current_player.hand), 8)
        self.assertEqual(game.current_player.cards_drawn_this_turn, 4)

        number_two.play()

        self.assertEqual(len(game.current_player.hand), 9)
        self.assertEqual(game.current_player.cards_drawn_this_turn, 6)

    def test_targeted_actions(self):
        tokens = lex('Deal 5 Damage', token_exprs)
        card = parse_card('Bolt Bolt', CardType.SPELL, 3, CardClass.MAGE, tokens)

        register_card(card)

        game = prepare_game(CardClass.MAGE, CardClass.MAGE)

        bolt_bolt = game.player1.give(card.__name__)

        self.assertEqual(game.current_player.opponent.hero.health, 30)

        bolt_bolt.play(target=game.current_player.opponent.hero)

        self.assertEqual(game.current_player.opponent.hero.health, 25)
