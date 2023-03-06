from random import randint
from random import choice
FIRST_ANSWER = 'What is the result of the expression?'


def generate_round():
    myseq = ('+', '-', '*')
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    operand = choice(myseq)
    random_string = str(random_int_a) + ' ' + operand + ' ' + str(random_int_b)
    match operand:
        case '+':
            result = random_int_a + random_int_b
        case '-':
            result = random_int_a - random_int_b
        case '*':
            result = random_int_a * random_int_b
    return [random_string, str(result)]
