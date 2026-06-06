def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    
    # Loop through each English word and its correct Spanish translation
    for english_word, spanish_translation in translations.items():
        # Prompt the user for input
        user_answer = input(f"What is the Spanish translation for {english_word}? ")
        
        # Clean up input by removing extra spaces and forcing lowercase
        if user_answer.strip().lower() == spanish_translation.lower():
            print("That is correct!")
            correct_count += 1  # Add 1 point for a correct answer
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.")
            
        # Prints a blank line after each question for visual clarity
        print()
        
    # Print the final score at the very end
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")

if __name__ == '__main__':
    main()