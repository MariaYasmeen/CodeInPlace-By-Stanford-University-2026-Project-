import random

def main():
    print("Khansole Academy")
    
    # 1. Generate two random 2-digit integers (10 through 99)
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    
    # 2. Calculate the correct answer
    correct_answer = num1 + num2
    
    # 3. Ask the user for their answer
    print(f"What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))
    
    # 4. Check if they are correct
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

if __name__ == '__main__':
    main()