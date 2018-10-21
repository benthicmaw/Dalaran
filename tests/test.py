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

        charge_boi.attack(game.player2.hero)

        self.assertTrue(charge_boi.can_attack())

        charge_boi.attack(game.player2.hero)

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

        self.assertEqual(game.player2.hero.health, 30)

        bolt_bolt.play(target=game.player2.hero)

        self.assertEqual(game.player2.hero.health, 25)

    def test_multiple_actions(self):
        tokens = lex('Deal 10 Damage. Draw 5 Cards.', token_exprs)
        card = parse_card('Weak Spell', 'Spell', 1, 'Mage', tokens)

        register_card(card)

        game = prepare_game(CardClass.MAGE, CardClass.MAGE)

        weak_spell = game.player1.give(card.__name__)

        self.assertEqual(len(game.player1.hand), 5)
        self.assertEqual(game.player2.hero.health, 30)

        weak_spell.play(target=game.player2.hero)

        self.assertEqual(len(game.player1.hand), 9)
        self.assertEqual(game.player2.hero.health, 20)

    def test_area_of_effect_actions(self):
        tokens = lex('Deal 5 Damage to all characters', token_exprs)
        card_1 = parse_card('Big Splash', CardType.SPELL, 1, CardClass.MAGE, tokens)

        card_2 = parse_card('Placeholder', CardType.MINION, 0, CardClass.NEUTRAL, [], 1, 1)

        register_card(card_1)
        register_card(card_2)

        game = prepare_game(CardClass.MAGE, CardClass.MAGE)

        placeholder_1 = game.player1.give(card_2.__name__)
        placeholder_2 = game.player1.give(card_2.__name__)

        placeholder_1.play()
        placeholder_2.play()

        game.end_turn()

        self.assertEqual(game.player1.hero.health, 30)
        self.assertEqual(game.player2.hero.health, 30)

        big_splash = game.player2.give(card_1.__name__)

        big_splash.play()

        self.assertEqual(game.player1.hero.health, 25)
        self.assertEqual(game.player2.hero.health, 25)

        self.assertTrue(placeholder_1.dead)
        self.assertTrue(placeholder_2.dead)

    def test_armor(self):
        tokens = lex('Gain 5000 Armor', token_exprs)
        card = parse_card('Shield Up', CardType.SPELL, 0, CardClass.WARRIOR, tokens)

        register_card(card)

        game = prepare_game(CardClass.WARRIOR, CardClass.WARRIOR)
        shield_up = game.player1.give(card.__name__)

        self.assertEqual(game.player1.hero.armor, 0)

        shield_up.play()

        self.assertEqual(game.player1.hero.armor, 5000)

    def test_leading_target(self):
        tokens = lex('Your opponent draws two cards', token_exprs)
        card = parse_card('Library', CardType.SPELL, 1, CardClass.DRUID, tokens)

        register_card(card)

        game = prepare_game(CardClass.DRUID, CardClass.DRUID)
        library = game.player1.give(card.__name__)

        self.assertEqual(len(game.player2.hand), 5)

        library.play()

        self.assertEqual(len(game.player2.hand), 7)

    def test_mana_crystals(self):
        tokens = lex('Gain 9 mana crystals', token_exprs)
        card = parse_card('Steroids', CardType.SPELL, 0, CardClass.DRUID, tokens)

        register_card(card)

        game = prepare_game(game_class=BaseGame)
        steroids = game.player1.give(card.__name__)

        self.assertEqual(game.player1.max_mana, 1)

        steroids.play()

        self.assertEqual(game.player1.max_mana, 10)

