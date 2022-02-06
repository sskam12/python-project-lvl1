"""Creating function welcome_user."""

import prompt


def welcome_user():
    """Return greeting with name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
