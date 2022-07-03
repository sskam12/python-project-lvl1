#!/usr/bin/env python


"""Prime game."""


from brain_games.games import prime
from brain_games.main_logic import run_game


def main():
    """Start prime game."""
    run_game(prime)


if __name__ == '__main__':
    main()
