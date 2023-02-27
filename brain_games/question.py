import prompt
import math
from random import randint
from random import choice
ROUNDS_COUNT = 3


def is_even(random_int):
    if random_int % 2 == 0:
        return 'yes'
    else:
        return 'no'


def ask_question(question):
    print('Question: ' + question)
    return prompt.string('Your answer: ')


def is_correct_answer(answer, correct_answer):
    if correct_answer == answer:
        print('Correct')
        return 'Win'
    else:
        print("'" + answer + "'" + " is wrong answer "
              ";(. Correct answer was '" + correct_answer + "'.")
        return 'Mistake'


def is_even_question():
    random_int = randint(1, 100)
    is_even_value = is_even(random_int)
    answer = ask_question(str(random_int))
    return is_correct_answer(answer, is_even_value)


def calc_question():
    myseq = ('+', '-', '*')
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    operand = choice(myseq)
    random_string = str(random_int_a) + ' ' + operand + ' ' + str(random_int_b)
    answer = ask_question(random_string)
    result = eval(random_string)
    return is_correct_answer(answer, str(result))


def calc_nod():
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    random_string = str(random_int_a) + ' ' + str(random_int_b)
    answer = ask_question(random_string)
    result = math.gcd(random_int_a, random_int_b)
    return is_correct_answer(answer, str(result))


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
    answer = ask_question(random_string.replace(str(result), '..', 1))
    return is_correct_answer(answer, str(result))


def right_answer_prime():
    prime_string = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                    83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                    137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                    191, 193, 197, 199]
    random_number = randint(2, 199)
    if prime_string.count(random_number) > 0:
        is_prime = 'yes'
    else:
        is_prime = 'no'
    answer = ask_question(str(random_number))
    return is_correct_answer(answer, is_prime)


def welcome():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    return name


def game(name, game_name):
    i = 1
    while i <= ROUNDS_COUNT:
        result_calc = game_name()
        if result_calc == 'Win':
            i += 1
        else:
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + "!")
