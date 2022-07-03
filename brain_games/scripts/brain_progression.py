#!/usr/bin/env python


"""Progression game."""


from brain_games.games.progression import DESCRIPTION, get_question_and_answer
from brain_games.main_logic import run_game


def main():
    """Start progression game."""
    run_game(get_question_and_answer, DESCRIPTION)


if __name__ == '__main__':
    main()
