import random

"""
File: main.py
--------------------
This program simulates rolling a dice with a user-specified 
number of sides using the random.randint function.
"""

def main():
    # 1. Ask the user for the number of sides and convert to an integer
    num_sides = int(input("How many sides does your dice have? "))
    
    # 2. Generate a random roll between 1 and the number of sides
    # randint(min, max) includes both the min and the max in the possible outcomes
    roll = random.randint(1, num_sides)
    
    # 3. Print the result
    print("Your roll is", roll)

if __name__ == '__main__':
    main()