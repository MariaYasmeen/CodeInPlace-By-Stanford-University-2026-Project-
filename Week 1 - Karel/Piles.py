from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel cleans the first row, picking up every beeper in 
each pile until the wall is reached.
"""

def main():
    # Loop across the row until the wall
    while front_is_clear():
        clean_entire_pile()
        move()
    
    # Final check for the last corner
    clean_entire_pile()

def clean_entire_pile():
    """
    While there is at least one beeper on the current square,
    Karel will keep picking them up. This handles piles of 10.
    """
    while beepers_present():
        pick_beeper()

if __name__ == '__main__':
    main()