#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import game, calc_progression


def brain_games_progression(name):
    print('What number is missing in the progression?')
    game(name, calc_progression)


def main():
    name = welcome()
    brain_games_progression(name)


if __name__ == '__main__':
    main()
