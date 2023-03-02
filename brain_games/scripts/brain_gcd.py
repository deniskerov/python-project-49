#!/usr/bin/env python3
from brain_games.engine import welcome
from brain_games.engine import game
from brain_games.games.gcd import gcd_game


def brain_games_gcd(name):
    game(name, gcd_game, 'Find the greatest common divisor of given numbers.')


def main():
    name = welcome()
    brain_games_gcd(name)


if __name__ == '__main__':
    main()
