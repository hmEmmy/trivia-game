import random


def main():
    print("Welcome to the Trivia Game!")
    print("Let's see how many questions you can answer correctly. Good luck!\n")

    score = 0
    random.shuffle(questions)

    for idx, question_data in enumerate(questions, 1):
        print(f"Question {idx}:")
        if ask_question(question_data):
            print("Nice job! That's the correct answer.\n")
            score += 1
        else:
            print(f"Oops! The correct answer was: {question_data['answer']}\n")

    print(f"\nGame Over! You scored {score}/{len(questions)}.")
    if score == len(questions):
        print("Perfect score! Well done!")
    elif score > len(questions) // 2:
        print("Good job! You got more than half right!")
    else:
        print("Better luck next time!")


def ask_question(question_data):
    print(f"\nHere's your question:")
    print(f"{question_data['question']}")
    print("Choose an option:")
    for idx, option in enumerate(question_data['options'], 1):
        print(f"{idx}. {option}")

    while True:
        try:
            user_answer = int(input("Your answer (1-4): ").strip())
            if 1 <= user_answer <= 4:
                break
            else:
                print("Oops, please choose a number between 1 and 4.")
        except ValueError:
            print("Hmm, that doesn't look like a valid number. Please enter a number between 1 and 4.")

    if question_data['options'][user_answer - 1] == question_data['answer']:
        return True
    return False


questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Fitzgerald"],
     "answer": "Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Mars", "Saturn"],
     "answer": "Jupiter"},
    {"question": "What is the square root of 64?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Ozone", "Ocelot"],
     "answer": "Oxygen"}
]


if __name__ == "__main__":
    main()