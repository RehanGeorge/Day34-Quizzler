from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white", borderwidth=5)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        button_true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=button_true_image, highlightthickness=0, command=self.tick_button)
        self.true_button.grid(column=0, row=2)

        button_false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=button_false_image, highlightthickness=0, command=self.cross_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"That was the last question. Your score is {self.quiz.score} / {self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif is_right == False:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(500, self.get_next_question)


    def tick_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

