from random import randint
FIRST_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even(random_int):
    if random_int % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_round():
    random_int = randint(1, 100)
    is_even_value = check_even(random_int)
    return [str(random_int), is_even_value]
