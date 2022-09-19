"""Creating function welcome_user."""

import prompt


def welcome_user():
    """Return greeting with name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
