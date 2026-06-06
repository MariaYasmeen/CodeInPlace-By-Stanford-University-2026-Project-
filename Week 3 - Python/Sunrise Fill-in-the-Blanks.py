"""
File: main.py
--------------------
This program takes user input to fill in the blanks of a story template.
"""

def main():
    # 1. Collect inputs with the exact prompts required
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")
    
    # 2. Print the story using the variables
    # We use string concatenation (+) or f-strings to ensure the spacing is exact
    print("At dawn the sky turned " + color + ", and the air felt " + adjective + ". I decided today I will finally " + goal + ".")

if __name__ == '__main__':
    main()