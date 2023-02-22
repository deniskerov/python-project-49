import prompt
import math
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


def is_correct_answer(answer, result):
    if is_int(answer):
        if result == int(answer):
            print('Correct')
            return 'Win'
        else:
            return (str(answer) + ' is wrong answer ;(.'
                    ' Correct answer was ' + str(result))
    else:
        return (str(answer) + ' is wrong answer ;(.'
                ' Correct answer was ' + str(result))


def calc_nod():
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    random_string = str(random_int_a) + ' ' + str(random_int_b)
    answer = ask_question(random_string)
    result = math.gcd(random_int_a, random_int_b)
    return is_correct_answer(answer, result)


def calc_progression():
    random_progression_len = randint(7, 12)
    progression = []
    random_first_num = randint(1, 12)
    random_multiplex = randint(2, 10)
    progression.append(str(random_first_num))
    i = 1
    while i < random_progression_len:
        progression.append(str(int(progression[i - 1]) + random_multiplex))
        i += 1
    random_count = randint(1, random_progression_len - 1)
    result = int(progression[random_count])
    random_string = ' '.join(progression)
    answer = ask_question(random_string.replace(str(result), '..'))
    return is_correct_answer(answer, result)


def welcome():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    return name
