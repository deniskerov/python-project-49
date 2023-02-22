import prompt
from random import randint
from random import choice


def is_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False


def ask_question(question):
    print('Question: ', question)
    return prompt.string('Your answer: ')


def calc_question():
    myseq = ('+', '-', '*')
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    operand = choice(myseq)
    random_string = str(random_int_a) + ' ' + operand + ' ' + str(random_int_b)
    answer = ask_question(random_string)
    result = eval(random_string)
    if is_int(answer):
        if result == int(answer):
            print('Correct')
            return 'Win'
        else:
            return (str(answer) + ' is wrong answer ;(.'
                    'Correct answer was ' + str(result))
    else:
        return (str(answer) + ' is wrong answer ;(.'
                'Correct answer was ' + str(result))


def welcome():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    return name
