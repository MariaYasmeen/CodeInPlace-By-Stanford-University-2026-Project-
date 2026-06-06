"""
File: main.py
--------------------
This program prompts the user for their name and then 
prints a personalized greeting.
"""

def main():
    # 1. Prompt the user for their name and store it in a variable
    name = input("What is your name? ")
    
    # 2. Print "Hello" followed by the name
    # We can pass multiple arguments to the print function
    print("Hello", name)

if __name__ == '__main__':
    main()