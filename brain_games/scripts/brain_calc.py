#!/usr/bin/env python


"""Calculator game."""


from brain_games.games.calc import description, game_with_answers
from brain_games.main_logic import main_logic


def main():
    """Start calculator game."""
    main_logic(game_with_answers, description)


if __name__ == '__main__':
    main()
