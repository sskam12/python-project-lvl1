"""Calculator game."""

import operator
from random import choice, randint

description = 'What is the result of the expression?'


def game_with_answers():
    """Game with operators.

    Returns:
        The question and correct answer.
    """
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_operation = choice(['+', '-', '*'])
    question = '{a} {b} {c}'.format(
        a=random_number1, b=random_operation, c=random_number2,
    )
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    correct_answer = operators[random_operation](random_number1, random_number2)
    correct_answer = str(correct_answer)
    return question, correct_answer
