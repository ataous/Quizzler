from data import question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz_ui = QuizInterface(QuizBrain(question_bank))
