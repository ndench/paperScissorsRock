#!/usr/bin/python

# TODO: 
# 1. We need to get first_to from the command line
#   so the game can be customised
# 2. Add lizard
#   - scissors decapitates lizard
#   - lizard eats paper
#   - rock crushes lizard
# 3. Add spock
#   - spock smashes scissors
#   - lizard poisons spock
#   - paper disproves spock
#   - spock vaporises rock


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


def getUserChoice(choices):
    message = 'Choose one of ' + str(choices) + ': '
    user_choice = raw_input(message)

    while (user_choice not in choices):
        user_choice = raw_input('That is not a valid choice, try again: ')

    return user_choice


def game_start():
    first_to = 3
    print 'Let\' play paper, scissors, rock!'
    print 'First to ' + str(first_to) + ' wins'
    print ''

    valid_choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while (user_score < first_to and computer_score < first_to):
        winner = game(valid_choices)
        if (winner == 'user'):
            user_score += 1
        elif (winner == 'computer'):
            computer_score += 1

        print ''
        print 'Scores:'
        print '  You: ' + str(user_score)
        print '  Computer: ' + str(computer_score)

    print ''
    if user_score == first_to:
        print 'You win the game! :D'
    else:
        print 'Game Over. You lose :('


def game(valid_choices):
    user_choice = getUserChoice(valid_choices)

    rand = random.randint(0, 2)
    computer_choice = valid_choices[rand]

    winning_choice = computeWinner(user_choice, computer_choice)

    print ''
    print 'You: ' + user_choice
    print 'Computer: ' + computer_choice
    if (winning_choice == 'tie'):
        print 'The game is tied.'
        return 'tie'
    elif (winning_choice == user_choice):
        print 'You win!'
        return 'user'
    else:
        print 'The computer wins!'
        return 'computer'


if __name__ == '__main__':
    game_start()
