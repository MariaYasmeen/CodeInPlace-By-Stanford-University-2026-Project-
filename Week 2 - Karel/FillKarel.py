from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel fills any size world with beepers, navigating through 
the gaps in the walls at the first column.
"""

def main():
    """
    Fills the world row by row.
    """
while left_is_clear():
        fill_row()
        reset_to_start_of_row()
        move_to_next_row()
    
fill_row()

def fill_row():
    """
    Places beepers across a single row until a wall is hit.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()  

def reset_to_start_of_row():
    """
    Turns around and moves back to the first column.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around() # Face East again

def move_to_next_row():
    """
    Moves up one row through the gap at the first column.
    """
    turn_left()
    move()
    turn_right()

def turn_right():
    """Standard turn right using three left turns."""
    for i in range(3):
        turn_left()

def turn_around():
    """Standard turn around using two left turns."""
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()