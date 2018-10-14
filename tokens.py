# https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

# basic types
INT = 'INT'
ID = 'ID'

# other
STATS = 'STATS'
ABILITY = 'ABILITY'
TARGET = 'TARGET'
EVENT = 'EVENT'
POINTER = 'POINTER'
END = 'END'
ACTION = 'ACTION'
FIELD = 'FIELD'
MODIFER = 'MODIFER'
RANDOM = 'RANDOM'

token_exprs = [
    (r'[ \n\t]+', None),
    (r'[0-9]\/[0-9]', STATS),
    (r'one|two|three|four|five|six|seven|eight|nine|ten', INT),
    (r'[0-9]+', INT),
    (r'\([0-9]\)', INT),
    (r'your', POINTER),
    (r'all', POINTER),
    (r'enemy', POINTER),
    (r'friendly', POINTER),
    (r'[Ss]ummon', ACTION),
    (r'[Dd]estroy', ACTION),
    (r'[Rr]estore', ACTION),
    (r'[Gg]ive', ACTION),
    (r'[Dd]eal', ACTION),
    (r'[Dd]raw', ACTION),
    (r'Charge', ABILITY),
    (r'Taunt', ABILITY),
    (r'Spell Damage', ABILITY),
    (r'Battlecry:', EVENT),
    (r"opponent(\'s)?", TARGET),
    (r'minions?', TARGET),
    (r'it', TARGET),
    (r'enemies', TARGET),
    (r'split', MODIFER),
    (r'to full', MODIFER),
    (r'undamaged', MODIFER),
    (r'this turn', MODIFER),
    (r'\+[0-9]\/\+[0-9]', MODIFER),
    (r'\+[0-9]', MODIFER),
    (r'[Ww]eapon', FIELD),
    (r'[Dd]amage', FIELD),
    (r'[Hh]ealth', FIELD),
    (r'[Cc]ards', FIELD),
    (r'[Aa]ttack', FIELD),
    (r'[Aa]rmor', FIELD),
    (r'hero', FIELD),
    (r'random(ly)?', RANDOM),
    (r'\.', None),
    (r'to', None),
    (r'among', None),
    (r'and', None),
    (r'for', None),
    (r'an|a', None),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]
