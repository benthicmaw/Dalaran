# https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1

import sys

from Dalaran.lexer import lex, token_exprs


def hearthstone_lex(characters, token_exprs_=token_exprs):
    return lex(characters, token_exprs_)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as card:
            card_text = card.read()

    else:
        card_text = sys.stdin.read()

    tokens = hearthstone_lex(card_text)

    for token in tokens:
        print(token)
