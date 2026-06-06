"""
File: main.py
--------------------
This program prompts the user for two numbers and 
prints the result of their multiplication.
"""

def main():
    print("This program multiplies two numbers.")
    
    # 1. Prompt the user to enter the first number and convert to integer
    num1 = input("Enter first number: ")
    num1 = int(num1)
    
    # 2. Prompt the user to enter the second number and convert to integer
    num2 = input("Enter second number: ")
    num2 = int(num2)
    
    # 3. Calculate the multiplication
    result = num1 * num2
    
    # 4. Print the final value
    print(result)

if __name__ == '__main__':
    main()