#!/usr/bin/env python


"""Yes or no game."""


from brain_games.games.even import description, game_with_answers
from brain_games.main_logic import main_logic


def main():
    """Start even game."""
    main_logic(game_with_answers, description)


if __name__ == '__main__':
    main()
