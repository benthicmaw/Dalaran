# Dalaran

[![Build Status](https://travis-ci.org/kajchang/Dalaran.svg?branch=master)](https://travis-ci.org/kajchang/Dalaran)

Basic Lexer and Parser for Hearthstone Simulations.

Built in the hope of creating an easy way to add custom cards to a simulation and to learn parsing and lexing a "language".

Currently in the stage of building out the lexer to tokenize all current cards correctly and getting basic parsing working.

In it's current state, the lexer is able to lex cards from the Basic Set or cards that have the same vocabulary, and can parse card's abilities into a form usable in [fireplace](https://github.com/jleclanche/fireplace), a Python implementation of Hearthstone.

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

`main.py` can make cards from a `.json` file formatted like this:

```json
{
    "name": "Reckless Rocketeer",
    "type": "Minion",
    "class": "Neutral",
    "cost": 6,
    "attack": 5,
    "health": 2,
    "text": "Charge"
}
```

The above file can be found in the `tests/` folder.

```bash
python3 main.py tests/RecklessRocketeer.json
<GameTag.CHARGE: 197>: True
<GameTag.CARDNAME: 185>: 'Reckless Rocketeer'
<GameTag.COST: 48>: 6
<GameTag.CARDTYPE: 202>: <CardType.MINION: 4>
<GameTag.CLASS: 199>: <CardClass.NEUTRAL: 12>
<GameTag.ATK: 47>: 5
<GameTag.HEALTH: 45>: 2
```

Feel free to help out and contribute!
