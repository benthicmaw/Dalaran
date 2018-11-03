import unittest

from Dalaran import Dalaran

from .utils import *


class Test_Dalaran(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dalaran = Dalaran()

        cls = self.dalaran.parse_card(
            'Placeholder', CardType.MINION, 0, CardClass.NEUTRAL)
        self.dalaran.register_card(cls)
        self.placeholder = cls.__name__

    def setUp(self):
        self.game = prepare_game()

    def test_ability(self):
        cls = self.dalaran.parse_card(
            'Charger', CardType.MINION, 1, CardClass.NEUTRAL, 'Charge.', 1, 1
        )

        self.dalaran.register_card(cls)

        charger = self.game.player1.give(cls.__name__)

        charger.play()

        self.assertTrue(charger.can_attack())

        charger.attack(self.game.player2.hero)

        self.assertFalse(charger.can_attack())

    def test_action(self):
        cls = self.dalaran.parse_card(
            'Pong', CardType.SPELL, 1, CardClass.MAGE, 'Deal 1 Damage.'
        )

        self.dalaran.register_card(cls)

        pong = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)

        pong.play(target=self.game.player2.hero)

        self.assertEqual(self.game.player2.hero.health, 29)

    def test_multiple_actions(self):
        cls = self.dalaran.parse_card(
            'Ping Pong', CardType.SPELL, 1, CardClass.WARRIOR, 'Deal 1 Damage. Gain 1 Armor.'
        )

        self.dalaran.register_card(cls)

        ping_pong = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)
        self.assertEqual(self.game.player1.hero.armor, 0)

        ping_pong.play(target=self.game.player2.hero)

        self.assertEqual(self.game.player2.hero.health, 29)
        self.assertEqual(self.game.player1.hero.armor, 1)

    def test_mana_crystals(self):
        self.game = prepare_game(game_class=BaseGame)

        cls = self.dalaran.parse_card(
            'Ramp', CardType.SPELL, 1, CardClass.DRUID, 'Gain 2 mana crystals.'
        )

        self.dalaran.register_card(cls)

        ramp = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player1.max_mana, 1)
        self.assertEqual(self.game.player1.mana, 1)

        ramp.play()

        self.assertEqual(self.game.player1.max_mana, 3)
        self.assertEqual(self.game.player1.mana, 2)

    def test_empty_mana_crystals(self):
        self.game = prepare_game(game_class=BaseGame)

        cls = self.dalaran.parse_card(
            'Empty Ramp', CardType.SPELL, 1, CardClass.DRUID, 'Gain 2 empty mana crystals.'
        )

        self.dalaran.register_card(cls)

        empty_ramp = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player1.max_mana, 1)
        self.assertEqual(self.game.player1.mana, 1)

        empty_ramp.play()

        self.assertEqual(self.game.player1.max_mana, 3)
        self.assertEqual(self.game.player1.mana, 0)

    def test_battlecry(self):
        cls = self.dalaran.parse_card(
            'Ping Kid', CardType.MINION, 1, CardClass.NEUTRAL, 'Battlecry: Deal 1 Damage.'
        )

        self.dalaran.register_card(cls)

        ping_kid = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)

        ping_kid.play(target=self.game.player2.hero)

        self.assertEqual(self.game.player2.hero.health, 29)

    def test_opponent_armor_gain(self):
        cls = self.dalaran.parse_card(
            'Armor Gift', CardType.SPELL, 1, CardClass.DRUID, 'Your opponent gains two armor.'
        )

        self.dalaran.register_card(cls)

        armor_gift = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.armor, 0)

        armor_gift.play()

        self.assertEqual(self.game.player2.hero.armor, 2)

    def test_opponent_card_draw(self):
        cls = self.dalaran.parse_card(
            'Neutralize', CardType.SPELL, 1, CardClass.DRUID, 'Your opponent draws two cards.'
        )

        self.dalaran.register_card(cls)

        neutralize = self.game.player1.give(cls.__name__)

        self.assertEqual(len(self.game.player2.hand), 5)

        neutralize.play()

        self.assertEqual(len(self.game.player2.hand), 7)

    def test_self_damage(self):
        cls = self.dalaran.parse_card(
            'Self Damage', CardType.SPELL, 1, CardClass.WARLOCK, 'Deal 5 damage to your hero.'
        )

        self.dalaran.register_card(cls)

        self_damage = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player1.hero.health, 30)

        self_damage.play()

        self.assertEqual(self.game.player1.hero.health, 25)

    def test_opponent_damage(self):
        cls = self.dalaran.parse_card(
            'Opponent Damage', CardType.SPELL, 1, CardClass.WARLOCK, 'Deal 5 damage to your opponent.'
        )

        self.dalaran.register_card(cls)

        opponent_damage = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)

        opponent_damage.play()

        self.assertEqual(self.game.player2.hero.health, 25)
