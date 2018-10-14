# https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

# basic types
INT = 'INT'
ID = 'ID'

# other
STATS = 'STATS'
ABILITY = 'ABILITY'
PLAYER = 'PLAYER'
EVENT = 'EVENT'
POINTER = 'POINTER'
END = 'END'
SUMMON = 'SUMMON'

token_exprs = [
    (r'[ \n\t]+', None),
    (r'\.', END),
    (r'[0-9]\/[0-9]', STATS),
    (r'one|two|three|four|five|six|seven|eight|nine', INT),
    (r'[0-9]+', INT),
    (r'\([0-9]\)', INT),
    (r'for your', POINTER),
    (r'Summon', SUMMON),
    (r'Charge\.?', ABILITY),
    (r'Battlecry:', EVENT),
    (r'opponent', PLAYER),
    (r'a', None),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]
