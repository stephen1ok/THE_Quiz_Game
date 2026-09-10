# Python Quiz Game 

A console-based math quiz game built in Python. The game generates 5 random
math questions, presents 4 multiple-choice options for each, tracks the
player's score, and gives feedback at the end.

## What I Learned

### for and while loops
I used a for loop to run exactly 5 questions (for question_number in
range(5):), since I knew in advance how many times it needed to repeat.

I used while loops in two different places where I didn't know in advance
how many times something needed to repeat:
- To keep generating random numbers until they divided evenly
  (while num1 % num2 != 0:)
- To keep re-asking the player for input until they typed a valid option
  (while user_answer not in letters:)

That distinction — "I know exactly how many times" vs "I need to repeat until
a condition is met" — is what decided which loop to use each time.

### Functions and return values
My main function, quiz_question(), builds one full question: it generates
random numbers, calculates the correct answer, builds 3 wrong answers,
shuffles all 4 options, and figures out which letter (A/B/C/D) ended up
holding the correct one.

It returns three values at once:
python
return question_text, options, correct_letter

Those values are then unpacked and used in the main part of the program to
print the question, show the options, and check the player's answer:
python
question_text, options, correct_letter = quiz_question()


### How the quiz works
1. Two random numbers are generated, with a while loop guaranteeing they
   divide evenly (no messy decimal answers).
2. A question is built around them, e.g. "if 48 / 2 is 24, what is 24 * 9?"
3. The correct answer and 3 wrong answers are put in a list and shuffled
   with random.shuffle().
4. options.index(correct_answer) finds where the correct answer landed
   after shuffling, and that position is converted into a letter (A–D)
   using letters[position].
5. The player is asked to answer. If they type something that isn't A, B,
   C, or D, they're asked again instead of the program crashing or
   silently accepting it.

### How the score is tracked
score starts at 0 before the loop. Each time the player's answer matches
correct_letter, score = score + 1 runs. At the end, the score is shown
out of 5, along with a message:
- 5 → Excellent
- 3–4 → Good
- 0–2 → Needs Improvement

## Difficult Parts
 - I had to learn zip()
 - I learn if you dont save your editor it we not run the change