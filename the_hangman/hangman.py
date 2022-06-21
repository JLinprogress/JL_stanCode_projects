"""
File: hangman.py
Name: Jerry Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    secret = random_word()
    print(secret)
    h = hyphen(secret)
    counter = 7
    print('The word looks like ' + h)
    print('You have ' + str(counter) + ' wrong guesses left.')

    letter_guessed = ''
    while counter != 0:
        guess = input('Your guess: ').upper()
        s = secret.find(guess)
        if s >= 0:
            letter_guessed += guess
            answer = hang(secret, letter_guessed)
            if answer != secret:
                print('You are correct!\nThe word looks like ' + hang(secret, letter_guessed))
                print('You have ' + str(counter) + ' wrong guesses left.')
            else:
                print('You are correct!\nYou win!!\nThe word was: ' + str(secret))
                break
        else:
            counter -= 1
            print('There is no ' + guess + '\'s in the word.')
            if counter > 0:
                print('The word looks like ' + hang(secret, letter_guessed))
                print('You have ' + str(counter) + ' wrong guesses left.')

    print('You are completely hung :（\nThe word was: ' + str(secret))


def hang(x, y):
    """
    This function returns hint strings after player enters the right guesses.
    """
    secret = x
    letter_guessed = y
    ans = ''
    for letter in secret:
        if letter in letter_guessed:
            ans += letter
        else:
            ans += '-'
    return ans


def hyphen(x):
    """
    This function turns each character of the secret word into '-'
    """
    ans = ''
    for i in range(len(x)):
        ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
