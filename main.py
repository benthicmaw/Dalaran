# https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

import sys
import json

from Dalaran.lexer.lexer import lex
from Dalaran.lexer.tokens import token_exprs

from Dalaran.parser.parser import parse_card


def hearthstone_lex(characters,
                    token_exprs=token_exprs):
    return lex(characters, token_exprs)


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as card:
        card_data = json.load(card)
        card_text = card_data['text']

    tokens = hearthstone_lex(card_text)

    card = parse_card(card_data['name'], card_data['type'], card_data['cost'], card_data['class'],
                      tokens, card_data.get('attack', None), card_data.get('health', None))

    print(card)
