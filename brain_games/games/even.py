"""Yes or no game."""


from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_question_and_answer():
    """Brain even game.

    Returns:
        The question and correct answer.
    """
    question = randint(1, 100)
    correct_answer = 'no' if question % 2 else 'yes'
    return question, correct_answer
