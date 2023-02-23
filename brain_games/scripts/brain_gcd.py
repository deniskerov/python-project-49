#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import calc_nod


def brain_games_nod(name):
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i <= 2:
        result_calc = calc_nod()
        if result_calc == 'Win':
            i += 1
        else:
            print(result_calc)
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + "!")


def main():
    name = welcome()
    brain_games_nod(name)


if __name__ == '__main__':
    main()
