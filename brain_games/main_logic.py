"""The main logic of all games with game_with_answers, description."""


import prompt


def main_logic(game_with_answers, description):
    """Greeting of user.

    Args:
        description: The description of game.
        game_with_answers: The logic of games.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(description)
    current_round = 1
    max_round = 3
    while current_round <= max_round:
        question, correct_answer = game_with_answers()
        print('Question: {0}'.format(question))
        given_answer = prompt.string('Your answer: ')
        if given_answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print("{a} is wrong answer ;(. Correct answer was '{b}'.".format(
                a=given_answer, b=correct_answer,
            ))
            print("Let's try again, {c}!".format(c=name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
