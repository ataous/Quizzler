from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        """
        :param quiz_brain: QuizBrain Class
        """
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        self.lbl_score = Label(self.root, text="Score: 0 / 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
        self.lbl_score.grid(row=0, column=1)

        self.cnv_question = Canvas(self.root, width=300, height=250, bg="white")
        self.cnv_question_txt = self.cnv_question.create_text(150, 125,
                                                              text="Some Question Text",
                                                              width=280,
                                                              fill=THEME_COLOR,
                                                              font=("Arial", 16, "italic"),
                                                              justify=CENTER)
        self.cnv_question.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.btn_true = Button(self.root, image=true_img, bg=THEME_COLOR, relief=FLAT, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.btn_false = Button(self.root, image=false_img, bg=THEME_COLOR, relief=FLAT, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self) -> None:
        """
        Get Next Question And Set To UI And Reset Canvas Color Tp White
        """
        self.cnv_question.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.cnv_question.itemconfig(self.cnv_question_txt, text=q_text)
        else:
            self.cnv_question.itemconfig(self.cnv_question_txt, text="You've reached the end of the quiz.")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self) -> None:
        """
        Check user answer and call give_feedback method
        :return: None
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self) -> None:
        """
        Check user answer and call give_feedback method
        :return: None
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        """
        Change canvas color base on user answer and set get_next_question for 1000 ms later to reset
        :param is_right: is user answer is correct
        :return: None
        """
        if is_right:
            self.cnv_question.config(bg="green")
        else:
            self.cnv_question.config(bg="red")
        self.lbl_score.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        self.root.after(1000, self.get_next_question)
