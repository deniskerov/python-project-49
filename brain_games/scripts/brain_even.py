#!/usr/bin/env python3
from brain_games.engine import run
from brain_games.games.even import generate_round, FIRST_ANSWER


def main():
    run(generate_round, FIRST_ANSWER)


if __name__ == '__main__':
    main()
