# Dalaran

[![Build Status](https://travis-ci.org/kajchang/Dalaran.svg?branch=Simulator%2FParser)](https://travis-ci.org/kajchang/Dalaran)

Basic Lexer and Parser for Hearthstone Simulations.

Effectively, this project aims to provide a tool that can "read" Hearthstone cards and generate playable versions of them from their text.

In it's current state, the lexer is able to lex cards from the Basic Set or cards that have the same vocabulary. It can parse card's abilities and basic actions like drawing cards into a form usable in [fireplace](https://github.com/jleclanche/fireplace), a Python implementation of Hearthstone.

## Try it Out


Clone this repository:

```bash
git clone https://github.com/kajchang/Dalaran.git
Cloning into 'Dalaran'...
cd Dalaran
```

Install [fireplace](https://github.com/jleclanche/fireplace):
```bash
pip3 install -e git+https://github.com/kajchang/fireplace.git#egg=fireplace
```

Install Dalaran:
```bash
pip3 install .
```

Open up a shell for `python3.6` or `python3.7`, now we're going to make a very weak, basic spell:
```python
>>> from Dalaran.lexer import lex, token_exprs
>>> from Dalaran.parser import parse_card, register_card
>>> from Dalaran.utils import prepare_game
>>> tokens = lex('Deal 10 Damage. Draw 5 Cards.', token_exprs) # tokenize the text
>>> card = parse_card('Weak Spell', 'Spell', 1, 'Mage', tokens) # create the card
>>> register_card(card)
>>> game = prepare_game()
>>> weak_spell = game.player1.give(card.__name__) # give the card to the first player
>>> print(len(game.player1.hand)) # 5
>>> print(game.player1.opponent.hero.health) # 30
>>> weak_spell.play(target=game.player1.opponent.hero) # play the spell
>>> print(len(game.player1.hand)) # 5 + 5 - 1 = 9
>>> print(game.player1.opponent.hero.health) # 30 - 10 = 20
```

And that's how you can make and play with your custom hearthstone cards!

Feel free to help out and contribute!
