"""Calculator game."""

import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    """Game with operators.

    Returns:
        The question and correct answer.
    """
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operations, operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    random_operation = choice(list(operations.keys()))
    question = '{a} {b} {c}'.format(
        a=random_number1, b=random_operation, c=random_number2,
    )
    correct_answer = operators[random_operation](random_number1, random_number2)
    return question, str(correct_answer)
