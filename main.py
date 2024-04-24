from data import question_data
from questions_model import Question
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")