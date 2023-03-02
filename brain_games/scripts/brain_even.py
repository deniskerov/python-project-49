#!/usr/bin/env python3
from brain_games.engine import welcome
from brain_games.engine import game
from brain_games.games.even import even_game


def brain_games_even(name):
    game(name, even_game, 'Answer "yes" if the number'
                          ' is even, otherwise answer "no".')


def main():
    name = welcome()
    brain_games_even(name)


if __name__ == '__main__':
    main()
