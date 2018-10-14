# Dalaran

Basic Lexer and Parser for Hearthstone Simulations.

Built in the hope of building an easy way to add custom cards to a simulation and to learn parsing and lexing a "language".

Currently in the stage of building out the lexer to tokenize all current cards correctly.

In it's current state, the lexer is only able to parse Leeroy Jenkins and any cards that have the same vocabulary as an example.

## Try it Out

Clone this repository:

```bash
git clone https://github.com/kajchang/Dalaran.git
Cloning into 'Dalaran'...
cd Dalaran
```

`main.py` can lex from `sys.stdin`, and it can also read from a file.

From `sys.stdin`:

```bash
echo "Charge. Battlecry: Summon two 1/1 Whelps for your opponent." | python3 main.py
('Charge.', 'ABILITY')
('Battlecry:', 'EVENT')
('Summon', 'SUMMON')
('two', 'INT')
('1/1', 'STATS')
('Whelps', 'ID')
('for your', 'POINTER')
('opponent', 'PLAYER')
('.', 'END')
```

From a file:

```bash
echo "Charge. Battlecry: Summon two 1/1 Whelps for your opponent." > LeeroyJenkins.card
python3 main.py LeeroyJenkins.card
('Charge.', 'ABILITY')
('Battlecry:', 'EVENT')
('Summon', 'SUMMON')
('two', 'INT')
('1/1', 'STATS')
('Whelps', 'ID')
('for your', 'POINTER')
('opponent', 'PLAYER')
('.', 'END')
```

Feel free to help out and contribute!
