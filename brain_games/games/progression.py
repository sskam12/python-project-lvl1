"""Progression game."""

from random import choice, randint

description = 'What number is missing in the progression?'


def get_question_and_answer():
    """Progression game.

    Returns:
        The question and correct answer.
    """
    number_of_elements = 11
    step = randint(1, 100)
    first_element = randint(1, 100)
    arithm_prog = range(
        first_element, first_element + step * (number_of_elements - 1), step,
    )
    arithm_prog = list(arithm_prog)
    correct_answer = choice(arithm_prog)
    arithm_prog[arithm_prog.index(correct_answer)] = str('..')
    correct_answer = str(correct_answer)
    question = '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(*arithm_prog)
    return question, correct_answer
