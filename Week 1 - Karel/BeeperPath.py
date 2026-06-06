from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel follows a trail of beepers and stops exactly 
one step past the last beeper to reach home.
"""

def main():
    # 1. Move until Karel finds the start of the beeper trail.
    # This handles any empty space at the beginning of the world.
    while no_beepers_present():
        move()
        
    # 2. Follow the trail of beepers.
    # As long as Karel sees a beeper, keep moving forward.
    while beepers_present():
        move()
    
    # Once the second loop ends, Karel is standing on the 
    # first empty square past the trail—which is home!

if __name__ == '__main__':
    main()