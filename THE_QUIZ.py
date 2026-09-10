import random

def quiz_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 9)
      
    while num1 % num2 != 0:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 9)
    
    num3 = int(num1 / num2)
    num4 = random.randint(1, 9)
    correct_answer = num3 * num4
    wrong1 = correct_answer + random.randint(1, 10)
    wrong2 = correct_answer + random.randint(11, 20)
    wrong3 = correct_answer + random.randint(21, 30)
    options = [correct_answer, wrong1, wrong2, wrong3]
    random.shuffle(options)
    position = options.index(correct_answer)
    letters = ["A", "B", "C", "D"]
    correct_letter = letters[position]
    
    question_text = f"if {num1} / {num2} is {num3} what is {num3} * {num4}?"
    return question_text, options, correct_letter

score = 0
for question_number in range(5):
    question_text, options, correct_letter = quiz_question()
    print(question_text)

    letters = ["A", "B", "C", "D"]
    for letter, option in zip(letters, options):
        print(f"{letter}. {option}")

    user_answer = input("Enter your answer (A-D): ").upper()
    while user_answer not in letters:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer (A-D): ").upper()

    if user_answer == correct_letter:
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong! The correct answer is {correct_letter}.")

print(f"Your final score is {score}/5.")

if score >= 5:
    print("Excellent")
elif score >= 3:
    print("Good")
elif score >= 1:
    print("Needs Improvement")
else:
    print("Needs Improvement")