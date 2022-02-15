#!/usr/bin/env python

"""Yes or no game."""

from random import randint

import prompt


def main():
    """Greeting of user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    def welcome_user():
        """Return greeting with name."""
        print('Hello, {0}!'.format(name))
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def is_even():
      current_round = 1
      max_round = 3
      while current_round <= max_round:
        x = randint(1, 100)
        print('Question: {0}'.format(x))
        answer = prompt.string('Your answer: ')
        if (x % 2  == 0 and answer == 'yes') or (x % 2 != 0 and answer == 'no'):
          print('Correct!')
        elif x % 2 != 0 and answer == 'yes':
          print("'yes' is wrong answer ;(. Correct answer was 'no'. \
          \nLet's try again, {0}!".format(name))
        elif answer != 'no' or answer != 'yes':
          if x % 2  == 0:
            print("{a} is wrong answer ;(. Correct answer was 'yes'. \
            \nLet's try again, {b}!".format(a = answer, b = name))
          else:
            print("{a} is wrong answer ;(. Correct answer was 'no'. \
            \nLet's try again, {b}!".format(a = answer, b = name))
        current_round += 1
      else:
          print('Congratulations, {}!'.format(name))
    is_even()


if __name__ == '__main__':
    main()
