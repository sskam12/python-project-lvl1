#!/usr/bin/env python


"""Yes or no game."""


from brain_games.games.even import description, get_question_and_answer
from brain_games.main_logic import run_game


def main():
    """Start even game."""
    run_game(get_question_and_answer, description)


if __name__ == '__main__':
    main()
