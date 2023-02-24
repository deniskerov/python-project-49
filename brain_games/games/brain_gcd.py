#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import game, calc_nod


def brain_games_gcd(name):
    print('Find the greatest common divisor of given numbers.')
    game(name, calc_nod)


def main():
    name = welcome()
    brain_games_gcd(name)


if __name__ == '__main__':
    main()
