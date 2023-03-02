#!/usr/bin/env python3
from brain_games.engine import welcome
from brain_games.engine import game
from brain_games.games.calc import calc_game


def brain_games_calc(name):
    game(name, calc_game, 'What is the result of the expression?')


def main():
    name = welcome()
    brain_games_calc(name)


if __name__ == '__main__':
    main()
