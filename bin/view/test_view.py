from tkinter import *
from control.io_manager import getTest
from objects.question import SingleAnswerQuestion


class TestView:
    def __init__(self, root: Tk, testId, control):
        def checkButtonControl(e):
            print(e.widget["value"])

        self.__root = root
        self.__control = control
        self.__testId = testId
        self.__test = getTest(self.__testId)

        self.__testView = Toplevel(root)
        answers = []
        for i in range(self.__test.getNumberOfQuestions()):
            question = self.__test.getQuestion(i)

            column = 0
            Label(self.__testView, text=question.getText()).grid(row=i, column=column)

            if isinstance(question, SingleAnswerQuestion):
                answers.append([IntVar()])
            else:
                answers.append([IntVar() for _ in range(question.getNumberOfAnswers())])

            for j in range(question.getNumberOfAnswers()):
                column += 1
                answer = question.getAnswer(j)
                if isinstance(question, SingleAnswerQuestion):
                    Radiobutton(self.__testView, text=answer, value=j, variable=answers[i][0]) \
                        .grid(row=i, column=column)
                else:
                    Checkbutton(self.__testView, text=answer, onvalue=1, offvalue=0, variable=answers[i][j]) \
                        .grid(row=i, column=column)

    def mainloop(self):
        self.__testView.mainloop()
