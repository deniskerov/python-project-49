#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import calc_progression


def brain_games_progression(name):
    print('What number is missing in the progression?')
    i = 0
    while i <= 2:
        result_calc = calc_progression()
        if result_calc == 'Win':
            i += 1
        else:
            print(result_calc)
            print("Let's try again,", name, "!")
            return
    print('Congratulations,', name, "!")


def main():
    name = welcome()
    brain_games_progression(name)


if __name__ == '__main__':
    main()
