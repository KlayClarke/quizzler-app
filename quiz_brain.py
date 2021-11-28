import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        formatted_q_text = html.unescape(self.current_question.text)
        question = f"Q.{self.question_number}: {formatted_q_text} (True/False): "
        return question
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if self.question_number == 10:
            self.current_question.answer = None
        elif user_answer.lower() == correct_answer.lower():
            self.score += 1
        print(f'Correct answer is {self.current_question.answer}')
        return self.score
