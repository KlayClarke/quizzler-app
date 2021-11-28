from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 15, 'normal')
QUIZ_FONT = ('Arial', 13, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR, font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)
        self.quiz_text_window = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quiz_text_window.grid(row=1, column=0, columnspan=2, pady=40)
        self.quiz_text = self.quiz_text_window.create_text(150, 125, width=250, text=f'',
                                                           fill='black', font=QUIZ_FONT)
        self.true_image = PhotoImage(file='images/true.png')
        self.false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0,
                                  command=self.answer_true)
        self.false_button = Button(image=self.false_image, highlightthickness=0,
                                   command=self.answer_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.quiz_text_window.config(bg='white')
        self.score_text.config(text=f'Score: {self.quiz.score}')
        if self.quiz.question_number < 10:
            question = self.quiz.next_question()
            self.quiz_text_window.itemconfig(self.quiz_text, text=f'{question}')
        elif self.quiz.question_number == 10:
            self.quiz_text_window.itemconfig(
                self.quiz_text,
                text=f'You\'ve gotten {self.quiz.score} out of {self.quiz.question_number} correct!')

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if self.quiz.question_number <= 10:
            if is_right:
                self.quiz_text_window.config(bg='green')
            elif not is_right:
                self.quiz_text_window.config(bg='red')
        self.window.after(1000, self.get_next_question)