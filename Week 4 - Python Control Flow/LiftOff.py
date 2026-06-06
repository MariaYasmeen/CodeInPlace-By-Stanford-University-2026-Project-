"""
File: main.py
--------------------
This program prints a countdown from 10 to 1, followed by "Liftoff!"
"""

def main():
    # The loop runs 10 times (i goes from 0 to 9)
    for i in range(10):
        # Calculate the countdown:
        # When i=0, 10 - 0 = 10
        # When i=9, 10 - 9 = 1
        countdown_value = 10 - i
        print(countdown_value)
    
    # After the loop finishes, print the final message
    print("Liftoff!")

if __name__ == '__main__':
    main()