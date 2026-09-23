import random

LETTERS = ["A", "B", "C", "D"]

def quiz_question():
    num2 = random.randint(1, 9)
    num1 = num2 * random.randint(1, 11)
    num3 = int(num1 / num2)
    num4 = random.randint(1, 9)
    correct_answer = num3 * num4
    wrong1 = correct_answer + random.randint(1, 10)
    wrong2 = correct_answer + random.randint(11, 20)
    wrong3 = correct_answer + random.randint(21, 30)
    options = [correct_answer, wrong1, wrong2, wrong3]
    random.shuffle(options)
    position = options.index(correct_answer)
    correct_letter = LETTERS[position]

    question_text = f"If {num1} / {num2} is {num3}, what is {num3} * {num4}?"
    return question_text, options, correct_letter


name = input("What is your name? ").strip().title()
while name == "":
    print("Name cannot be empty.")
    name = input("What is your name? ").strip().title()

print(f"Welcome, {name}!")

while True:
    choice = input("How many questions do you want? (1-50): ").strip()
    while not (choice.isdigit() and 1 <= int(choice) <= 50):
        print("Invalid choice. Enter a number from 1 to 50.")
        choice = input("How many questions do you want? (1-50): ").strip()
    total = int(choice)

    score = 0
    for question_number in range(total):
        question_text, options, correct_letter = quiz_question()
        print(f"\nQuestion {question_number + 1}/{total}")
        print(question_text)

        for letter, option in zip(LETTERS, options):
            print(f"{letter}. {option}")

        user_answer = input("Enter your answer (A-D): ").strip().upper()
        while user_answer not in LETTERS:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer (A-D): ").strip().upper()

        if user_answer == correct_letter:
            print("Correct!")
            score = score + 1
        else:
            print(f"Wrong! The correct answer is {correct_letter}.")

    print(f"\n{name}, your final score is {score}/{total}.")

    percentage = score / total * 100
    if percentage == 100:
        print("Excellent")
    elif percentage >= 60:
        print("Good")
    else:
        print("Needs Improvement")

    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print(f"Thanks for playing, {name}!")
        break