from random import randint
from random import choice


def calc_game():
    myseq = ('+', '-', '*')
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    operand = choice(myseq)
    random_string = str(random_int_a) + ' ' + operand + ' ' + str(random_int_b)
    result = eval(random_string)
    return [random_string, str(result)]
