#!/usr/bin/env python


"""Finding the greatest common divisor."""


from brain_games.games.gcd import description, game_with_answers
from brain_games.main_logic import main_logic


def main():
    """Start gcd game."""
    main_logic(game_with_answers, description)


if __name__ == '__main__':
    main()
