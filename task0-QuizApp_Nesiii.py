import random

# List of quiz data as dictionaries
questions_data = [
    {
        "text": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "correct": "A"
    },
    {
        "text": "Which data type is immutable in Python?",
        "choices": ["List", "Dictionary", "Tuple", "Set"],
        "correct": "C"
    },
    {
        "text": "What does 'len()' do in Python?",
        "choices": ["Adds numbers", "Prints to screen", "Returns length", "Exits program"],
        "correct": "C"
    },
    {
        "text": "Which of the following is a loop structure in Python?",
        "choices": ["if", "for", "elif", "def"],
        "correct": "B"
    },
    {
        "text": "Which keyword is used to define a function in Python?",
        "choices": ["func", "define", "function", "def"],
        "correct": "D"
    }
]

def display_question(question):
    print(f"\n{question['text']}")
    option_labels = ['A', 'B', 'C', 'D']
    
    for label, choice in zip(option_labels, question["choices"]):
        print(f"  {label}) {choice}")
    
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in option_labels:
            return answer == question["correct"]
        print("❌ Invalid input. Please enter A, B, C, or D.")

def display_result(score, total):
    percentage = (score / total) * 100
    print(f"\n🎯 You got {score}/{total} correct! ({percentage:.1f}%)")

    if percentage >= 80:
        print("🌟 Excellent!")
    elif percentage >= 50:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

def start_quiz():
    score = 0
    total = len(questions_data)
    shuffled_questions = random.sample(questions_data, total)

    for q in shuffled_questions:
        if display_question(q):
            score += 1

    display_result(score, total)

def main():
    print("Welcome to my Python Console Quiz App!")

    while True:
        start_quiz()
        again = input("\nWould you like to try again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("thanks for playing!")
            break

if __name__ == "__main__":
    main()
