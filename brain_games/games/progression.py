"""Progression game."""

from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Progression game.

    Returns:
        The question and correct answer.
    """
    length = 10
    step = randint(1, 100)
    start = randint(1, 100)
    progression = range(
        start, start + step * length, step,
    )
    progression = list(progression)
    correct_answer = choice(progression)
    progression[progression.index(correct_answer)] = str('..')
    correct_answer = str(correct_answer)
    question = ' '.join(map(str, progression))
    return question, correct_answer
