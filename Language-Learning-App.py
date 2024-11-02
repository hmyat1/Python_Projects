import random

# List of French to English words with their translations
words = [
    {"french": "le", "english": "the"},
    {"french": "de", "english": "of/from"},
    {"french": "que", "english": "that/which"},
    {"french": "et", "english": "and"},
    {"french": "à", "english": "to/at"},
    {"french": "dans", "english": "in/on"},
    {"french": "un", "english": "a/an"},
    {"french": "être", "english": "to be"},
    {"french": "se", "english": "oneself/itself"},
    {"french": "non", "english": "no/not"},
    {"french": "avoir", "english": "to have (auxiliary)"},
    {"french": "pour", "english": "for/by"},
    {"french": "avec", "english": "with"},
    {"french": "son", "english": "his/her/your/their"},
    {"french": "pour", "english": "for/to"},
    {"french": "comme", "english": "like/as"},
    {"french": "être", "english": "to be"},
    {"french": "avoir", "english": "to have"},
    {"french": "lui", "english": "him/her/you (indirect object)"},
    {"french": "le", "english": "it/him/you (direct object)"},
]

def quiz_user(words):
    """Quiz the user on French to English translations."""
    random.shuffle(words)  # Shuffle the word list for randomness
    score = 0  # Initialize the score

    for word in words:
        # Ask the user for the English translation of the French word
        print(f"What is '{word['french']}' in English?")
        user_answer = input("Your answer: ").strip().lower()  # Get user input
        correct_answer = word['english'].lower()  # Get the correct answer

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct!\n")  # Notify user of a correct answer
            score += 1  # Increment score
        else:
            print(f"Wrong! It's '{word['english']}'.\n")  # Notify user of the correct answer

    # Display the final score after the quiz
    print(f"Quiz complete! Score: {score}/{len(words)}")

def main():
    """Main function to start the quiz application."""
    print("Welcome to the Language Learning App!")  # Welcome message
    input("Press Enter to start...")  # Wait for user to start the quiz
    quiz_user(words)  # Start the quiz

if __name__ == "__main__":
    main()  # Run the main function
