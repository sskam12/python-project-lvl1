#!/usr/bin/env python


"""Calculator game."""


from brain_games.games import calc
from brain_games.main_logic import run_game


def main():
    """Start calculator game."""
    run_game(calc)


if __name__ == '__main__':
    main()
