"""GCD game."""

from random import randint

description = 'Find the greatest common divisor of given numbers.'


def game_with_answers():
    """Find GCD.

    Returns:
        The question and correct answer.
    """
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    question = '{a} {b}'.format(
        a=random_number1, b=random_number2,
    )
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 >= random_number2:
            random_number1 %= random_number2
        else:
            random_number2 %= random_number1
    correct_answer = str(random_number1 or random_number2)
    return question, correct_answer
