from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=400, height=500)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)


        self.window.mainloop()
