#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import game, calc_question


def brain_games_calc(name):
    print('What is the result of the expression?')
    game(name, calc_question)


def main():
    name = welcome()
    brain_games_calc(name)


if __name__ == '__main__':
    main()
