#!/usr/bin/env python


"""Yes or no game."""


from brain_games.games import even
from brain_games.main_logic import run_game


def main():
    """Start even game."""
    run_game(even)


if __name__ == '__main__':
    main()
