#!/usr/bin/env python


"""Progression game."""


from brain_games.games.progression import description, game_with_answers
from brain_games.main_logic import main_logic


def main():
    """Сonnection to the main function."""
    main_logic(game_with_answers, description)


if __name__ == '__main__':
    main()
