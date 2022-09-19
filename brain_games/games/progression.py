"""Progression game."""

from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Progression game.

    Returns:
        The question and correct answer.
    """
    length = 10
    step = randint(1, 100)
    start = randint(1, 100)
    end = start + step * length
    progression = list(range(start, end, step))
    hidden_index = randrange(0, length)
    correct_answer, progression[hidden_index] = progression[hidden_index], '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
