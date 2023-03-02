#!/usr/bin/env python3
from brain_games.engine import welcome
from brain_games.engine import game
from brain_games.games.prime import prime_game


def brain_games_prime(name):
    game(name, prime_game, 'Answer "yes" if given number is prime.'
         'Otherwise answer "no".')


def main():
    name = welcome()
    brain_games_prime(name)


if __name__ == '__main__':
    main()
