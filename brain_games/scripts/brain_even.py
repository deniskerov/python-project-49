#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import game, is_even_question


def brain_games_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(name, is_even_question)


def main():
    name = welcome()
    brain_games_even(name)


if __name__ == '__main__':
    main()
