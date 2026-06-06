"""
File: joke_bot.py
--------------------
A simple bot that tells a specific programmer joke if the user 
asks for one, otherwise it politely declines.
"""

# Constants: These are defined at the top of the program
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def main():
    # 1. Ask the user for input using the PROMPT constant
    user_input = input(PROMPT)
    
    # 2. Use an if statement to check if the input is exactly "Joke"
    if user_input == "Joke":
        print(JOKE)
    else:
        # 3. If they typed anything else, print the SORRY message
        print(SORRY)

if __name__ == '__main__':
    main()