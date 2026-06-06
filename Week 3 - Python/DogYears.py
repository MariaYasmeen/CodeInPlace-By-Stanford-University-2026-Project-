"""
File: main.py
--------------------
This program converts human years into dog years by 
multiplying the input by a factor of 7.18.
"""

def main():
    # 1. Get the age from the user
    # We use float() because the age might be a decimal (e.g., 2.5 years)
    human_years = float(input("Enter an age in calendar years: "))
    
    # 2. Perform the conversion
    # On average, 1 human year = 7.18 dog years
    dog_years = human_years * 7.18
    
    # 3. Report the result
    # We use a comma or an f-string to combine the text and the number
    print("That's", dog_years, "in dog years!")

if __name__ == '__main__':
    main()