"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will pick up the beeper(news paper) which is at S3,A6,
    and go back to the original spot to put down the beeper.
    Karel will face East after the whole movements.
    """

    pick_newspaper()
    return_home()


def pick_newspaper():
    """
    Karel will go to S3,A6 to collect the newspaper, facing East.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    """
    Karel will turn left three times.
    """
    for i in range(3):
        turn_left()


def return_home():
    """
    Karel will go back home, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
