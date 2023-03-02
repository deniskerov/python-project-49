from random import randint


def is_even(random_int):
    if random_int % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    random_int = randint(1, 100)
    is_even_value = is_even(random_int)
    return [str(random_int), is_even_value]
