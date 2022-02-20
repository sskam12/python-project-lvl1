"""Yes or no game."""


from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no"'


def game_with_answers():
    """Brain even game.

    Returns:
        The question and correct answer.
    """
    question = randint(1, 100)
    if question % 2 != 0:
        correct_answer = 'no'
    elif question % 2 == 0:
        correct_answer = 'yes'
    return question, correct_answer
