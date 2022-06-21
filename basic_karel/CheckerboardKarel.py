"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Blank world.
    Post-condition: Karel fills up the world with beepers and turns it into a checkerboard.
    """
    put_beeper()
    while left_is_clear():
        fill_one_line()
        turn_left()
        if front_is_clear():
            move()
            turn_around()
            move()
            if on_beeper():
                turn_around()
                move()
                turn_left()
                fill_one_line()
            else:
                turn_around()
                move()
                turn_left()
                put_beeper()
                fill_one_line()
        turn_right()
        if front_is_clear():
            move()
            turn_around()
            move()
            if on_beeper():
                turn_around()
                move()
                turn_right()
                fill_one_line()
            else:
                turn_around()
                move()
                turn_right()
                put_beeper()
                fill_one_line()
    else:
        # activated in the world 1x8
        fill_one_line()


def fill_one_line():
    """
    Karel will put one beeper on every two dots.
    """

    while front_is_clear():
        if on_beeper():
            move()
            if front_is_clear():
                move()
                put_beeper()
            else:
                pass
        else:
            if front_is_clear():
                move()
                put_beeper()


def turn_around():
    """
    Karel will turn left twice.
    """
    for i in range(2):
        turn_left()


def turn_right():
    """
    Karel will turn left 3 times.
    """
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
