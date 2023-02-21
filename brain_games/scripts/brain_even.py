#!/usr/bin/env python3
import prompt
from random import randint


def ask_question(name):
    i = 0
    while i <= 2:
        random_int = randint(0, 100)
        print('Question: ', random_int)
        answer = prompt.string()
        if ((random_int % 2) == 0 and answer == 'yes') or \
           ((random_int % 2) != 0 and answer == 'no'):
            print('Correct')
            i += 1
        elif answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return 'Mistake'
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return 'Mistake'


def main():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if ask_question(name) != 'Mistake':
        print('Congratulations,', name, "!")
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
