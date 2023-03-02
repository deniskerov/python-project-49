#!/usr/bin/env python3
from brain_games.engine import welcome
from brain_games.engine import game
from brain_games.games.progression import progression_game


def brain_games_progression(name):
    game(name, progression_game, 'What number is missing in the progression?')


def main():
    name = welcome()
    brain_games_progression(name)


if __name__ == '__main__':
    main()
