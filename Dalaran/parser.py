import re

from pyleri import *


class Numbers(Grammar):
    RE_KEYWORDS = re.compile('^[A-Za-z]+')

    number_words = Choice(Keyword('one', ign_case=True), Keyword('two', ign_case=True), Keyword('three', ign_case=True), Keyword('four', ign_case=True), Keyword(
        'five', ign_case=True), Keyword('six', ign_case=True), Keyword('seven', ign_case=True), Keyword('eight', ign_case=True), Keyword('nine', ign_case=True), Keyword('ten', ign_case=True))

    numbers_digits = Regex('[0-9]+')

    numbers = Choice(number_words, numbers_digits)


class Actions(Grammar):
    RE_KEYWORDS = re.compile('^[A-Za-z]+')

    summon = Keyword('summon', ign_case=True)
    destroy = Keyword('destroy', ign_case=True)
    restore = Keyword('restore', ign_case=True)
    give = Keyword('give', ign_case=True)
    deal = Keyword('deal', ign_case=True)
    draw = Keyword('draw', ign_case=True)
    freeze = Keyword('freeze', ign_case=True)
    gain = Keyword('gain', ign_case=True)
    put = Keyword('put', ign_case=True)
    change = Keyword('change', ign_case=True)
    copy = Keyword('copy', ign_case=True)
    transform = Keyword('transform', ign_case=True)
    return_ = Keyword('return', ign_case=True)
    discard = Keyword('discard', ign_case=True)
    look = Keyword('look', ign_case=True)


class Main(Numbers, Actions):
    pass
