"""Prime game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    """Identify prime number.

    Args:
        question: random number from 1 to 100.

    Returns:
        True if the number is prime, else - False.
    """
    if question == 1:
        return False
    for num in range(2, (question // 2 + 1)):
        if (question % num == 0):
            return False
    return True


def get_question_and_answer():
    """Find prime number.

    Returns:
        The question and correct answer.
    """
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) is True else 'no'
    return str(question), correct_answer
