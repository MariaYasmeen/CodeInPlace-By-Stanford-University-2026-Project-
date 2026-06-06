from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel completes a beeper puzzle by picking up the final 
piece and placing it in the correct empty slot.
"""

def main():
    # Step 1: Pick up the piece at (3, 1)
    get_puzzle_piece()
    
    # Step 2: Place the piece at (4, 3)
    put_piece_in_place()
    
    # Step 3: Return to (1, 1) facing East
    return_to_start()

def get_puzzle_piece():
    """
    Moves Karel from (1, 1) to (3, 1) to pick up the beeper.
    Pre-condition: Karel at (1, 1), facing East.
    Post-condition: Karel at (3, 1), facing East, carrying a beeper.
    """
    move()
    move()
    pick_beeper()

def put_piece_in_place():
    """
    Moves Karel from (3, 1) to (4, 3) to drop the beeper.
    Pre-condition: Karel at (3, 1), facing East.
    Post-condition: Karel at (4, 3), facing East, beeper dropped.
    """
    move()
    turn_left()
    move()
    move()
    put_beeper()

def return_to_start():
    """
    Moves Karel from (4, 3) back to (1, 1) facing East.
    Pre-condition: Karel at (4, 3), facing North.
    Post-condition: Karel at (1, 1), facing East.
    """
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around() # Face East to admire the puzzle

def turn_right():
    """Helper to turn Karel 90 degrees right."""
    for i in range(3):
        turn_left()

def turn_around():
    """Helper to turn Karel 180 degrees."""
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()