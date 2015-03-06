#!/usr/bin/python

import random

def computeWinner(choice1, choice2):
    if (choice1 == choice2):
        return 'tie'

    if (choice1 == 'paper'):
        if (choice2 == 'rock'):
            return 'paper'
        else:
            return 'rock'

    elif (choice1 == 'rock'):
        if (choice2 == 'paper'):
            return 'paper'
        else:
            return 'rock'

    else:
        if (choice1 == 'rock'):
            return 'rock'
        else:
            return 'scissors'


def game():
    valid_choices = ['rock', 'paper', 'scissors']
    user_choice = raw_input('Choose paper, scissors or rock: ')

    while (user_choice not in valid_choices):
        user_choice = raw_input('That is not a valid choice, try again: ')

    rand = random.randint(0, 2)
    computer_choice = valid_choices[rand]

    winner = computeWinner(user_choice, computer_choice)

    print 'You: ' + user_choice
    print 'Computer: ' + computer_choice
    if (winner == 'tie'):
        print 'The game is tied.'
    else:
        print winner + ' wins!'


if __name__ == '__main__':
    while(True):
        game()
