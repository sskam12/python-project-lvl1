#!/usr/bin/env python


"""Finding the greatest common divisor."""


from brain_games.games.gcd import DESCRIPTION, get_question_and_answer
from brain_games.main_logic import run_game


def main():
    """Start gcd game."""
    run_game(get_question_and_answer, DESCRIPTION)


if __name__ == '__main__':
    main()
