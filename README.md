# Dalaran

Basic Lexer and Parser for Hearthstone Simulations.

Built in the hope of building an easy way to add custom cards to a simulation and to learn parsing and lexing a "language".

Currently in the stage of building out the lexer to tokenize all current cards correctly.

In it's current state, the lexer is only able to lex cards from the Basic Set or cards that have the same vocabulary.

## Try it Out


Clone this repository:

```bash
git clone https://github.com/kajchang/Dalaran.git
Cloning into 'Dalaran'...
cd Dalaran
```

Install [fireplace](https://github.com/jleclanche/fireplace), a Python implementation of Hearthstone:
```bash
pip3 install -e git+https://github.com/kajchang/fireplace.git#egg=fireplace
```

`main.py` can lex from `sys.stdin`, and it can also read from a file.

From `sys.stdin`:

```bash
echo "Charge. Battlecry: Summon two 1/1 Whelps for your opponent." | python3 main.py
('Charge', 'ABILITY')
('Battlecry:', 'EVENT')
('Summon', 'ACTION')
('two', 'INT')
('1/1', 'MODIFIER')
('Whelps', 'ID')
('your', 'MODIFIER')
('opponent', 'TARGET')
```

From a file:

```bash
echo "Charge. Battlecry: Summon two 1/1 Whelps for your opponent." > LeeroyJenkins.card
python3 main.py LeeroyJenkins.card
('Charge', 'ABILITY')
('Battlecry:', 'EVENT')
('Summon', 'ACTION')
('two', 'INT')
('1/1', 'MODIFIER')
('Whelps', 'ID')
('your', 'MODIFIER')
('opponent', 'TARGET')
```

Feel free to help out and contribute!
