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


def is_correct_answer_prime(answer):
    if (answer == 'yes') or (answer == 'no'):
        return True
    else:
        return False


def right_answer_prime():
    prime_string = "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, " \
                   "37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79," \
                   "83, 89, 97, 101, 103, 107, 109, 113, 127, 131," \
                   "137, 139, 149, 151, 157, 163, 167, 173, 179, 181," \
                   "191, 193, 197, 199"
    random_number = randint(2, 199)
    is_prime = prime_string.find(', ' + str(random_number))
    answer = ask_question(random_number)
    if is_correct_answer_prime(answer):
        if (is_prime > 0) and (answer == 'yes') \
                or (is_prime < 0) and (answer == 'no'):
            print('Correct')
            return 'Win'
        elif answer == 'yes':
            return ('"yes" is wrong answer ;(.'
                    ' Correct answer was "no"')
        else:
            return ('"no" is wrong answer ;(.'
                    ' Correct answer was "yes"')
    else:
        if is_prime > 0:
            return (str(answer) + ' is wrong answer ;(.'
                    ' Correct answer was "yes"')
        else:
            return (str(answer) + ' is wrong answer ;(.'
                    ' Correct answer was "no"')


def welcome():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    return name
