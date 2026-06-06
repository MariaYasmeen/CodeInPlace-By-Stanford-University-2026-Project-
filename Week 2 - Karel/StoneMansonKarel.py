from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel repairs the Temple of Artemis by building four columns 
spaced 4 squares apart, each 5 beepers high.
"""

def main():
    """
    Main loop to build 4 columns.
    """
    # Build 3 columns with movement in between
    for i in range(3):
        build_five_beeper_column()
        move_four_spaces()
    
    # Build the final 4th column
    build_five_beeper_column()

def build_five_beeper_column():
    """
    Builds a vertical column of 5 beepers and returns to the base.
    """
    turn_left()
    # Place 4 beepers with a move after each
    for i in range(4):
        put_beeper()
        move()
    # Place the 5th beeper at the top
    put_beeper()
    
    # Return to the bottom
    turn_around()
    for i in range(4):
        move()
    turn_left() 

def move_four_spaces():
    """
    Moves Karel 4 spaces forward to the next column.
    """
    for i in range(4):
        move()

def turn_around():
    """Helper function to turn Karel 180 degrees."""
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()