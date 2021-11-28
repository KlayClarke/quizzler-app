from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 15, 'normal')
QUIZ_FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_text = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR, font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)
        self.quiz_text_window = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quiz_text_window.grid(row=1, column=0, columnspan=2, pady=20)
        self.quiz_text = self.quiz_text_window.create_text(150, 125, text='Sample Quiz Text',
                                                           fill='black', font=QUIZ_FONT)
        self.true_image = PhotoImage(file='images/true.png')
        self.false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
