"""GCD game."""

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Find GCD.

    Returns:
        The question and correct answer.
    """
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    question = f'{random_number1} {random_number2}'
    correct_answer = gcd(random_number1, random_number2)
    return question, str(correct_answer)
