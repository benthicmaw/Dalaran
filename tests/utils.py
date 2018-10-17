# https://github.com/jleclanche/fireplace/blob/master/tests/utils.py

import random

from hearthstone.enums import *

import fireplace.cards
from fireplace.brawls import *
from fireplace.game import BaseGame, CoinRules
from fireplace.logging import log
from fireplace.player import Player
from fireplace.utils import random_draft


# Collectible cards excluded from random drafts
BLACKLIST = (
    "GVG_007",  # Flame Leviathan
    "AT_022",  # Fist of Jaraxxus
    "AT_130",  # Sea Reaver
)

_draftcache = {}


def _draft(card_class, exclude):
    # random_draft() is fairly slow, this caches the drafts
    if (card_class, exclude) not in _draftcache:
        _draftcache[(card_class, exclude)] = random_draft(card_class, exclude + BLACKLIST)
    return _draftcache[(card_class, exclude)], card_class.default_hero


_heroes = fireplace.cards.filter(collectible=True, type=CardType.HERO)


class BaseTestGame(CoinRules, BaseGame):
    def start(self):
        super().start()
        self.player1.max_mana = 10
        self.player2.max_mana = 10


def _random_class():
    return CardClass(random.randint(2, 10))


def _empty_mulligan(game):
    for player in game.players:
        if player.choice:
            player.choice.choose()


def init_game(class1=None, class2=None, exclude=(), game_class=BaseTestGame):
    log.info("Initializing a new game")
    if class1 is None:
        class1 = _random_class()
    if class2 is None:
        class2 = _random_class()
    player1 = Player("Player1", *_draft(class1, exclude))
    player2 = Player("Player2", *_draft(class2, exclude))
    game = game_class(players=(player1, player2))
    return game


def prepare_game(*args, **kwargs):
    game = init_game(*args, **kwargs)
    game.start()
    _empty_mulligan(game)

    return game


def prepare_empty_game(class1=None, class2=None, game_class=BaseTestGame):
    log.info("Initializing a new game with empty decks")
    if class1 is None:
        class1 = _random_class()
    if class2 is None:
        class2 = _random_class()
    player1 = Player("Player1", [], class1.default_hero)
    player1.cant_fatigue = True
    player2 = Player("Player2", [], class2.default_hero)
    player2.cant_fatigue = True
    game = game_class(players=(player1, player2))
    game.start()
    _empty_mulligan(game)

    return game
