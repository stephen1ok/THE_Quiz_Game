import random
import customtkinter as ctk

# Configure CustomTkinter theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

LETTERS = ["A", "B", "C", "D"]


# --- BACKEND LOGIC ---
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


# --- DESKTOP GUI APPLICATION ---
class MathQuizApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Math Quiz Game")
    self.geometry("600x520")
    self.resizable(False, False)

    # Game state variables
    self.player_name = ""
    self.total_questions = 5
    self.current_question_index = 0
    self.score = 0
    self.current_correct_letter = ""

    # Main container frame
    self.main_frame = ctk.CTkFrame(self, corner_radius=15)
    self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Launch Welcome Screen
    self.show_welcome_screen()

  def clear_frame(self):
    """Removes all current UI elements before loading a new screen."""
    for widget in self.main_frame.winfo_children():
      widget.destroy()

  # SCREEN 1: WELCOME / SETUP
  def show_welcome_screen(self):
    self.clear_frame()

    title_label = ctk.CTkLabel(
        self.main_frame,
        text="🧮 Math Quiz Game",
        font=("Helvetica", 24, "bold"),
    )
    title_label.pack(pady=(30, 20))

    name_label = ctk.CTkLabel(
        self.main_frame, text="Enter Your Name:", font=("Helvetica", 14)
    )
    name_label.pack(pady=5)

    self.name_entry = ctk.CTkEntry(
        self.main_frame, placeholder_text="e.g. Alex", width=250
    )
    self.name_entry.pack(pady=5)

    count_label = ctk.CTkLabel(
        self.main_frame,
        text="Number of Questions (1-50):",
        font=("Helvetica", 14),
    )
    count_label.pack(pady=(15, 5))

    self.count_entry = ctk.CTkEntry(
        self.main_frame, placeholder_text="5", width=250
    )
    self.count_entry.pack(pady=5)

    self.error_label = ctk.CTkLabel(
        self.main_frame, text="", text_color="#e74c3c", font=("Helvetica", 12)
    )
    self.error_label.pack(pady=5)

    start_btn = ctk.CTkButton(
        self.main_frame,
        text="Start Quiz",
        font=("Helvetica", 16, "bold"),
        command=self.start_quiz,
    )
    start_btn.pack(pady=20)

  def start_quiz(self):
    name = self.name_entry.get().strip().title()
    count = self.count_entry.get().strip()

    if not name:
      self.error_label.configure(text="Please enter your name!")
      return

    if not (count.isdigit() and 1 <= int(count) <= 50):
      self.error_label.configure(
          text="Enter a valid question count (1-50)!"
      )
      return

    self.player_name = name
    self.total_questions = int(count)
    self.current_question_index = 0
    self.score = 0

    self.show_question_screen()

  # SCREEN 2: ACTIVE QUESTION
  def show_question_screen(self):
    self.clear_frame()

    header_text = (
        f"Player: {self.player_name}  |  Question"
        f" {self.current_question_index + 1}/{self.total_questions}  |"
        f" Score: {self.score}"
    )
    header_label = ctk.CTkLabel(
        self.main_frame, text=header_text, font=("Helvetica", 13, "bold")
    )
    header_label.pack(pady=(15, 10))

    q_text, options, self.current_correct_letter = quiz_question()

    q_label = ctk.CTkLabel(
        self.main_frame,
        text=q_text,
        font=("Helvetica", 18, "bold"),
        wraplength=480,
    )
    q_label.pack(pady=20)

    self.option_buttons = []
    for letter, option in zip(LETTERS, options):
      btn_text = f"{letter}.  {option}"
      btn = ctk.CTkButton(
          self.main_frame,
          text=btn_text,
          font=("Helvetica", 15),
          width=320,
          height=40,
          command=lambda l=letter: self.handle_answer(l),
      )
      btn.pack(pady=6)
      self.option_buttons.append(btn)

    self.feedback_label = ctk.CTkLabel(
        self.main_frame, text="", font=("Helvetica", 14, "bold")
    )
    self.feedback_label.pack(pady=10)

  def handle_answer(self, chosen_letter):
    for btn in self.option_buttons:
      btn.configure(state="disabled")

    if chosen_letter == self.current_correct_letter:
      self.score += 1
      self.feedback_label.configure(
          text="Correct! 🎉", text_color="#2ecc71"
      )
    else:
      self.feedback_label.configure(
          text=f"Wrong! Correct answer was {self.current_correct_letter} ❌",
          text_color="#e74c3c",
      )

    self.current_question_index += 1

    if self.current_question_index < self.total_questions:
      self.after(1200, self.show_question_screen)
    else:
      self.after(1200, self.show_result_screen)

  # SCREEN 3: RESULTS SUMMARY
  def show_result_screen(self):
    self.clear_frame()

    percentage = (self.score / self.total_questions) * 100
    if percentage == 100:
      rating = "Excellent! 🏆"
    elif percentage >= 60:
      rating = "Good Job! 👍"
    else:
      rating = "Needs Improvement 📚"

    res_title = ctk.CTkLabel(
        self.main_frame, text="Quiz Completed!", font=("Helvetica", 24, "bold")
    )
    res_title.pack(pady=(30, 10))

    name_lbl = ctk.CTkLabel(
        self.main_frame,
        text=f"Great attempt, {self.player_name}!",
        font=("Helvetica", 16),
    )
    name_lbl.pack(pady=5)

    score_lbl = ctk.CTkLabel(
        self.main_frame,
        text=f"Final Score: {self.score} / {self.total_questions} ({percentage:.0f}%)",
        font=("Helvetica", 18, "bold"),
    )
    score_lbl.pack(pady=15)

    rating_lbl = ctk.CTkLabel(
        self.main_frame,
        text=rating,
        font=("Helvetica", 16, "bold"),
        text_color="#3498db",
    )
    rating_lbl.pack(pady=5)

    # Button Container (holds Play Again and Exit side-by-side)
    button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    button_frame.pack(pady=30)

    play_again_btn = ctk.CTkButton(
        button_frame,
        text="Play Again",
        font=("Helvetica", 15, "bold"),
        width=130,
        command=self.show_welcome_screen,
    )
    play_again_btn.pack(side="left", padx=10)

    exit_btn = ctk.CTkButton(
        button_frame,
        text="Exit Game",
        font=("Helvetica", 15, "bold"),
        width=130,
        fg_color="#e74c3c",  # Red accent
        hover_color="#c0392b",
        command=self.destroy,  # Closes app window
    )
    exit_btn.pack(side="left", padx=10)


if __name__ == "__main__":
  app = MathQuizApp()
  app.mainloop()