import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions with answer choices
quiz_questions = {
    "What is the capital of France?": ["Paris", "Berlin", "Rome", "Madrid"],
    "What is the largest planet in our solar system?": ["Jupiter", "Mars", "Saturn", "Earth"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    "What is the powerhouse of the cell?": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"],
    "Which country is famous for kangaroos?": ["Australia", "Brazil", "Canada", "India"],
    "What is the chemical symbol for gold?": ["Au", "Ag", "Fe", "Cu"],
    "Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter", "Saturn"],
    "Who wrote 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    "Which instrument measures earthquakes?": ["Seismograph", "Thermometer", "Barometer", "Microscope"],
    "Which is the largest ocean on Earth?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
}

# Define correct answers for all questions
correct_answers = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the powerhouse of the cell?": "Mitochondria",
    "Which country is famous for kangaroos?": "Australia",
    "What is the chemical symbol for gold?": "Au",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "Which instrument measures earthquakes?": "Seismograph",
    "Which is the largest ocean on Earth?": "Pacific Ocean"
}

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("400x450")
        self.master.configure(bg="#333333")  # Background dark grey

        self.score = 0
        self.questions = list(quiz_questions.items())
        random.shuffle(self.questions)
        self.current_question = -1  # Start with the first question

        # Score label positioned at the top of the frame
        self.score_label = tk.Label(self.master, text=f"Score: {self.score} | Question {self.current_question + 1} of {len(self.questions)}", font=("Helvetica", 10), fg="#ffffff", bg="#333333")
        self.score_label.pack(anchor=tk.N, padx=10, pady=10)

        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 14), fg="#00bfff", bg="#333333", wraplength=380)
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 12), fg="#ffffff", bg="#1f1f1f", relief="ridge",
                               borderwidth=2, padx=20, pady=10, command=lambda i=i: self.submit_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.next_question()  # Display the first question

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            question, answer_choices = self.questions[self.current_question]
            self.question_label.config(text=question)

            # Shuffle answer choices to randomize their order
            random.shuffle(answer_choices)

            for i, button in enumerate(self.answer_buttons):
                button.config(text=answer_choices[i], bg="#1f1f1f", activebackground="#1f1f1f")

            # Update score label with current score and question progress
            self.score_label.config(text=f"Score: {self.score} | Question {self.current_question + 1} of {len(self.questions)}")

            # Set the correct answer for the current question
            self.correct_answer = correct_answers[question]

        else:
            self.show_result()

    def submit_answer(self, answer_index):
        if self.current_question < len(self.questions):
            selected_answer = self.answer_buttons[answer_index]["text"]

            if selected_answer == self.correct_answer:
                self.answer_buttons[answer_index].config(bg="#00bfff")  # Glow blue for correct answer
                self.score += 1
            else:
                self.answer_buttons[answer_index].config(bg="#ff0000")  # Glow red for incorrect answer
                # Find the index of the correct answer in the shuffled answer choices
                correct_index = self.answer_buttons.index(next(button for button in self.answer_buttons if button["text"] == self.correct_answer))
                self.answer_buttons[correct_index].config(bg="#00bfff")  # Glow blue for correct answer

            self.master.after(1000, self.next_question)

    def show_result(self):
        result_message = f"Quiz completed!\nYour final score is: {self.score}/{len(self.questions)}"
        choice = messagebox.askquestion("Quiz Completed", result_message + "\n\nDo you want to play again?", icon='question')

        if choice == 'yes':
            # Reset quiz for replay
            self.score = 0
            self.current_question = -1
            random.shuffle(self.questions)
            self.next_question()  # Restart quiz
        else:
            # Exit the quiz application
            self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
