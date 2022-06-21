"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: There are holes on the pillars of the arched door.
    Post-condition: Karel will fill up the pillars and stand at the bottom right,
    facing East.
    """
    turn_left()
    check_from_south_to_north()
    check_from_west_to_east()
    check_from_east_to_west()
    check_from_west_to_east()
    check_from_east_to_west()
    check_for_the_last_time()


def check_beeper():
    """
    Karel will check if the pillar needs to be fixed,
    if so, Karel will put beeper to fill it up.
    """
    if on_beeper():
        pick_beeper()
        put_beeper()
    else:
        put_beeper()


def turn_right():
    """
    Karel will turn left three times.
    """
    for i in range(3):
        turn_left()


def check_from_west_to_east():
    """
    Karel will check if the pillar should be fixed from West to East.
    """
    while front_is_clear():
        check_beeper()
        for i in range(4):
            move()
    else:
        check_beeper()
        turn_right()
    move()
    turn_right()


def check_from_east_to_west():
    """
    Karel will check if the pillar should be fixed from East to West.
    """
    while front_is_clear():
        check_beeper()
        for i in range(4):
            move()
    else:
        check_beeper()
        turn_left()
    move()
    turn_left()


def check_from_south_to_north():
    """
    Karel will check if the pillar should be fixed from South to North.
    """
    while front_is_clear():
        check_beeper()
        move()
    else:
        turn_right()


def check_for_the_last_time():
    """
    Karel will check the bottom part of the pillars.
    """
    while front_is_clear():
        check_beeper()
        for i in range(4):
            move()
    else:
        check_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
