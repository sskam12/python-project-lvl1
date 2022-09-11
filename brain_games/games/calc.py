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
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    random_operation = choice(list(operations.keys()))
    question = f'{random_number1} {random_operation} {random_number2}'
    correct_answer = operations[random_operation](
        random_number1, random_number2,
    )
    return question, str(correct_answer)
