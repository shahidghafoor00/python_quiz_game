from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    quiz = Question(question["question"], question["correct_answer"])
    question_bank.append(quiz)

q = QuizBrain(question_bank)

while q.still_have_questions():
    q.next_question()


q.final_scores(question_bank)