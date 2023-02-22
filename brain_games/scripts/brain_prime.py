#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import right_answer_prime


def brain_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i <= 2:
        result_calc = right_answer_prime()
        if result_calc == 'Win':
            i += 1
        else:
            print(result_calc)
            print("Let's try again,", name, "!")
            return
    print('Congratulations,', name, "!")


def main():
    name = welcome()
    brain_prime(name)


if __name__ == '__main__':
    main()
