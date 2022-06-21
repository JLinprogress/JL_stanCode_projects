"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1,1), facing East.
    Post-condition: Karel will stand on the midpoint of a world.
    """
    move_to_the_east_side()
    # facing West

    move_to_the_west_side()
    # facing East

    find_mind()


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


def move_ball():
    """
    Karel will pick up the beeper and move it towards the midpoint of the world.
    """
    pick_beeper()
    turn_around()
    move()
    put_beeper()


def move_to_the_east_side():
    """
    Karel moves from the start point to the East corner.
    """
    while front_is_clear():
        move()
    else:
        turn_around()
        put_beeper()


def move_to_the_west_side():
    """
    Karel moves from the East corner to the West one.
    """
    while front_is_clear():
        move()
    else:
        turn_around()
        put_beeper()


def find_mind():
    """
    Karel starts finding the midpoint by moving beepers closer towards the midpoint.
    """
    while front_is_clear():
        move()
        if on_beeper():
            move_ball()
    else:
        turn_around()

    while not on_beeper():
        move()
    else:
        pick_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
