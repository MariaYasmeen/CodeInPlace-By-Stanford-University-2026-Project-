"""
File: hailstone.py
--------------------
This program generates the Hailstone sequence for a given number.
If n is even, it is divided by 2.
If n is odd, it is multiplied by 3 and incremented by 1.
The process continues until n reaches 1.
"""

def main():
    # 1. Get the starting number from the user
    n = int(input("Enter a number: "))
    
    # 2. Continue the process until n is equal to 1
    while n != 1:
        if n % 2 == 1:
            # Case: n is odd
            next_n = n * 3 + 1
            print(f"{n} is odd, so I make 3n + 1: {next_n}")
            n = next_n
        else:
            # Case: n is even
            # Note: We cast to int() because / division creates a float
            next_n = int(n / 2)
            print(f"{n} is even, so I take half: {next_n}")
            n = next_n

if __name__ == '__main__':
    main()