# Dalaran

[![Build Status](https://travis-ci.org/kajchang/Dalaran.svg?branch=master)](https://travis-ci.org/kajchang/Dalaran)

Basic Lexer and Parser for Hearthstone Simulations.

Effectively, this project aims to provide a tool that can "read" Hearthstone cards and generate playable versions of them from their text.

In it's current state, the lexer is able to lex cards from the Basic Set or cards that have the same vocabulary. It can parse minions's abilities and basic spell actions and targeting a into a form usable in [fireplace](https://github.com/jleclanche/fireplace), a Python implementation of Hearthstone.

## Installation


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

Install Dalaran and other requirements:
```bash
pip3 install .
```

## Tests

There's a reasonable amount of test coverage, but more is coming in the future.

Run the tests:

```bash
python3 -m unittest discover
```

And that's how you can make and play with your custom hearthstone cards!


## Resources Used

[Building A Simple Interpreter In Python](https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1) for basic knowledge of lexing and code examples.

[Fireplace Documentation, Utilities, and Card Making API](https://github.com/jleclanche/fireplace) for examples of how to make integrate custom cards into their simulation and play and test games in their simulation.

## Related Projects

[Demystify](https://github.com/Zannick/demystify), up-to-date-ish project for the same thing in Magic: the Gathering, which uses a blend of Python and ANTLR, but with a similar approach. However, I don't think there's a real simulation / play aspect, and that it's more of just lexing / parsing.

## Contributing

Feel free to help out and contribute!
