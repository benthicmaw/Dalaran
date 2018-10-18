# https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

# basic types
INT = 'INT'
ID = 'ID'

# other
ABILITY = 'ABILITY'
TARGET = 'TARGET'
EVENT = 'EVENT'
MODIFIER = 'MODIFIER'
ACTION = 'ACTION'
FIELD = 'FIELD'
CONDITIONAL = 'CONDITIONAL'

token_exprs = [
    (r'[ \n\t]+', None),
    (r'one|two|three|four|five|six|seven|eight|nine|ten', INT),
    (r'\([0-9]\)', INT),
    (r'[Ss]ummon', ACTION),
    (r'[Dd]estroy', ACTION),
    (r'[Rr]estore', ACTION),
    (r'[Gg]ive', ACTION),
    (r'[Dd]eal', ACTION),
    (r'[Dd]raw', ACTION),
    (r'[Ff]reeze', ACTION),
    (r'[Gg]ain', ACTION),
    (r'[Hh]ave', ACTION),
    (r'[Cc]hange', ACTION),
    (r'[Tt]akes?', ACTION),
    (r'[Pp]ut', ACTION),
    (r'[Cc]opy', ACTION),
    (r'[Tt]ransform', ACTION),
    (r'[Rr]eturn', ACTION),
    (r'[Dd]iscard', ACTION),
    (r'[Ll]ook', ACTION),
    (r'is [a-z]+ed', ACTION),
    (r'Charge', ABILITY),
    (r'Taunt', ABILITY),
    (r'Spell Damage', ABILITY),
    (r'Divine Shield', ABILITY),
    (r'Windfury', ABILITY),
    (r'Battlecry:', EVENT),
    (r'Whenever', EVENT),
    (r'random(ly)?', MODIFIER),
    (r'split', MODIFIER),
    (r'to full', MODIFIER),
    (r'undamaged', MODIFIER),
    (r'damaged', MODIFIER),
    (r'this turn( only)?', MODIFIER),
    (r'all|ALL', MODIFIER),
    (r'others?', MODIFIER),
    (r'enemy', MODIFIER),
    (r'friendly', MODIFIER),
    (r'each', MODIFIER),
    (r'on the', MODIFIER),
    (r'instead', MODIFIER),
    (r'into', MODIFIER),
    (r'in', MODIFIER),
    (r'with', MODIFIER),
    (r'or more', MODIFIER),
    (r'or less', MODIFIER),
    (r'top', MODIFIER),
    (r'any', MODIFIER),
    (r'by', MODIFIER),
    (r'empty', MODIFIER),
    (r'[0-9]\/[0-9]', MODIFIER),
    (r'\+[0-9]\/\+[0-9]', MODIFIER),
    (r'\+[0-9]', MODIFIER),
    (r"owner(\'s)?", TARGET),
    (r"opponent(\'s)?", TARGET),
    (r"(this )?minion(s|\'s)?", TARGET),
    (r'characters?', TARGET),
    (r'it', TARGET),
    (r'enemies', TARGET),
    (r'[Ww]eapon', FIELD),
    (r'[Dd]amage', FIELD),
    (r'[Hh]ealth', FIELD),
    (r'[Cc]ards?', FIELD),
    (r'[Aa]ttack', FIELD),
    (r'[Aa]rmor', FIELD),
    (r'Mana Crystal', FIELD),
    (r'deck', FIELD),
    (r'hand', FIELD),
    (r'weapon', FIELD),
    (r'hero', FIELD),
    (r'battlefield', FIELD),
    (r'If you', CONDITIONAL),
    (r'\.|,', None),
    (r'at', None),
    (r'their', None),
    (r'the', None),
    (r'of', None),
    (r'to', None),
    (r'among', None),
    (r'and', None),
    (r'for', None),
    (r'an|a', None),
    (r'[0-9]+', INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]
