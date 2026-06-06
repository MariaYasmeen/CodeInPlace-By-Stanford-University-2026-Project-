"""
File: main.py
--------------------
This program prompts the user for a starting number and doubles it
repeatedly until the value reaches 100 or greater.
"""

def main():
    # 1. Ask the user for an initial number
    # We use int() to convert the input string into an integer
    curr_value = int(input("Enter a number: "))

    # 2. Start the while loop
    # The loop will continue as long as curr_value is less than 100
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2
        
        # Print the result of the doubling
        print(curr_value)

if __name__ == '__main__':
    main()