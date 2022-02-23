"""Prime game."""

from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_with_answers():
    """Find prime number.

    Returns:
        The question and correct answer.
    """
    question = randint(1, 100)
    number_of_divider = 0
    for number in range(2, question):
        if (question % number == 0):
            number_of_divider += 1
    if number_of_divider == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
