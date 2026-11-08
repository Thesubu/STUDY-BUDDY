"""
Study Buddy - A beginner-friendly Python quiz assistant.

Run:
    python main.py

No external packages are required.
"""

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B",
        "explanation": "Python uses the 'def' keyword to define a function.",
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. str", "B. int", "C. bool", "D. list"],
        "answer": "C",
        "explanation": "The bool type stores either True or False.",
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C",
        "explanation": "A hash symbol (#) starts a single-line comment.",
    },
    {
        "question": "Which function displays text on the screen?",
        "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
        "answer": "B",
        "explanation": "The print() function displays output.",
    },
    {
        "question": "Which collection uses key-value pairs?",
        "options": ["A. list", "B. tuple", "C. set", "D. dictionary"],
        "answer": "D",
        "explanation": "A dictionary stores data as key-value pairs.",
    },
]


def run_quiz():
    """Ask the quiz questions and show the final score."""
    score = 0
    print("\n=== Python Basics Quiz ===")
    print("Choose A, B, C, or D for each question.\n")

    for number, item in enumerate(QUESTIONS, start=1):
        print(f"{number}. {item['question']}")
        for option in item["options"]:
            print("   " + option)

        while True:
            choice = input("Your answer: ").strip().upper()
            if choice in {"A", "B", "C", "D"}:
                break
            print("Please enter only A, B, C, or D.")

        if choice == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}")
            print(f"Learn: {item['explanation']}\n")

    percentage = (score / len(QUESTIONS)) * 100
    print("=== Quiz Result ===")
    print(f"Your score: {score}/{len(QUESTIONS)} ({percentage:.0f}%)")

    if score == len(QUESTIONS):
        print("Excellent work! You got every question right.")
    elif score >= 3:
        print("Good effort! Review the explanations and try again.")
    else:
        print("Keep practising. You will improve one step at a time.")


def show_study_tips():
    """Display a few practical study tips."""
    tips = [
        "Study in short, focused sessions.",
        "Practise writing code instead of only reading it.",
        "Break big problems into smaller steps.",
        "Review mistakes and understand why they happened.",
        "Build small projects to apply what you learn.",
    ]

    print("\n=== Study Tips ===")
    for number, tip in enumerate(tips, start=1):
        print(f"{number}. {tip}")


def main():
    """Display the main menu."""
    print("Welcome to Study Buddy!")

    while True:
        print("\nChoose an option:")
        print("1. Take the Python basics quiz")
        print("2. Read study tips")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            show_study_tips()
        elif choice == "3":
            print("Thanks for using Study Buddy. Keep learning!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
