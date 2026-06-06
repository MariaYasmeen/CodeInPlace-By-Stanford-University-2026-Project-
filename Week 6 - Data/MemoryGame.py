import random
import os

NUM_PAIRS = 3  

def main(): 
    truth = []
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)
         
    random.shuffle(truth) 
    displayed = []
    for i in range(len(truth)):
        displayed.append('*') 
    while '*' in displayed: 
        print(displayed) 
        index1 = get_valid_index(displayed)
        index2 = get_valid_index(displayed, first_index=index1)
         
        if truth[index1] == truth[index2]: 
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
            print("Match!")
            clear_terminal()
        else: 
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue... ")
            clear_terminal()
             
    print(displayed)
    print("Congratulations! You won!")


def get_valid_index(displayed, first_index=None):
    """
    Repeatedly prompts the user for an index until they enter a valid integer
    that is in-bounds, unrevealed, and distinct from the first choice.
    """
    while True:
        user_input = input("Enter an index: ")
         
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue
            
        index = int(user_input)
         
        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue
             
        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue 
        if first_index is not None and index == first_index:
            print("You entered the same index twice. Try again.")
            continue 
        return index


def clear_terminal():
    """Clears the terminal screen for a cleaner card-flipping look.""" 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    main()