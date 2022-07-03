"""The main logic of all games with get_question_and_answer, description."""


import prompt

ROUND_COUNT = 3


def run_game(get_question_and_answer, description):
    """Greeting of user.

    Args:
        description: The description of game.
        get_question_and_answer: The logic of games.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(description)
    round_number = 1
    while round_number <= ROUND_COUNT:
        question, correct_answer = get_question_and_answer()
        print('Question: {0}'.format(question))
        given_answer = prompt.string('Your answer: ')
        if given_answer == correct_answer:
            print('Correct!')
            round_number += 1
        else:
            print("{a} is wrong answer ;(. Correct answer was '{b}'.".format(
                a=given_answer, b=correct_answer,
            ))
            print("Let's try again, {c}!".format(c=name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
