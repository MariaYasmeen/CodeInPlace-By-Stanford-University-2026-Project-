from karel.stanfordkarel import *

"""
File: main.py
--------------------
Karel celebrates 2026 by placing 20 beepers, moving, 
placing 26 beepers, and moving one last time.
"""

def main():
    # Place 20 beepers at the starting corner
    for i in range(20):
        put_beeper()
    
    # Move to the next corner
    move()
    
    # Place 26 beepers at the second corner
    for i in range(26):
        put_beeper()
        
    # Move to the final corner to finish the sequence
    move()

if __name__ == '__main__':
    main()