import random

# French to English words
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
    """Quiz the user."""
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is '{word['french']}' in English?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! It's '{word['english']}'.\n")

    print(f"Quiz complete! Score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning App!")
    input("Press Enter to start...")
    quiz_user(words)

if __name__ == "__main__":
    main()