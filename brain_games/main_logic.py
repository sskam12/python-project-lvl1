"""The main logic of all games with get_question_and_answer, description."""


import prompt

ROUND_COUNT = 3


def run_game(game):
    """Greeting of user.

    Args:
        game: run game.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(ROUND_COUNT):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        given_answer = prompt.string('Your answer: ')
        if given_answer == correct_answer:
            print('Correct!')
        if given_answer != correct_answer:
            print(
                f"'{given_answer}' is wrong answer ;(."
                + f" Correct answer was '{correct_answer}'.\n"
                + f"Let's try again, {name}!",
            )
            break
    else:
        print(f'Congratulations, {name}!')
