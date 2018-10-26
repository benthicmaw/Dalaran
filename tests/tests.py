import unittest

from Dalaran import Dalaran

from .utils import *


class Test_Dalaran(unittest.TestCase):
    def setUp(self):
        self.game = prepare_game()
        self.dalaran = Dalaran()

    def test_action(self):
        cls = self.dalaran.parse_card(
            'Pong', CardType.SPELL, 1, CardClass.MAGE, 'Deal 1 Damage.')

        self.dalaran.register_card(cls)

        pong = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)

        pong.play(target=self.game.player2.hero)

        self.assertEqual(self.game.player2.hero.health, 29)

    def test_multiple_actions(self):
        cls = self.dalaran.parse_card(
            'Ping Pong', CardType.SPELL, 1, CardClass.WARRIOR, 'Deal 1 Damage. Gain 1 Armor.')

        self.dalaran.register_card(cls)

        ping_pong = self.game.player1.give(cls.__name__)

        self.assertEqual(self.game.player2.hero.health, 30)
        self.assertEqual(self.game.player1.hero.armor, 0)

        ping_pong.play(target=self.game.player2.hero)

        self.assertEqual(self.game.player2.hero.health, 29)
        self.assertEqual(self.game.player1.hero.armor, 1)
