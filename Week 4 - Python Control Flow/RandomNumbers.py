import random

def main():
    # We use a for loop to repeat the code 10 times
    # range(10) produces numbers 0 through 9, total 10 iterations
    for i in range(10):
        # Generate a random integer between 1 and 100 (inclusive)
        value = random.randint(1, 100)
        
        # Print the value to the console
        print(value)

if __name__ == '__main__':
    main()