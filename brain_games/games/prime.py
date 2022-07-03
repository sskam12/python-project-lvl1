"""Prime game."""

from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Identify prime number.

    Args:
        number: random number from 1 to 100.

    Returns:
        True if the number is prime, else - False.
    """
    number_of_divider = 0
    if number == 1:
        return False
    for num in range(2, (number // 2 + 1)):
        if (number % num == 0):
            number_of_divider += 1
    return number_of_divider == 0


def get_question_and_answer():
    """Find prime number.

    Returns:
        The question and correct answer.
    """
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return question, correct_answer
