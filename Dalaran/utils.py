def string_to_num(token):
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'a': 1, 'an': 1}

    return int(token) if token.isdigit() else numbers[token]
