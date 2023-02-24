#!/usr/bin/env python3
from brain_games.question import welcome
from brain_games.question import game, right_answer_prime


def brain_games_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game(name, right_answer_prime)


def main():
    name = welcome()
    brain_games_prime(name)


if __name__ == '__main__':
    main()
