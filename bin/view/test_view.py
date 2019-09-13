from tkinter import *
from objects.question import SingleAnswerQuestion


class TestView:
    def __init__(self, root: Tk, test, control):
        def save(e=None):
            selected = []
            for i in range(len(self.__answers)):
                selected.append([x.get() for x in self.__answers[i]])
            self.__control.saveResults(selected)

        self.__root = root
        self.__control = control
        self.__test = test

        self.__testView = Toplevel(root)
        self.__answers = []
        row = 0
        for i in range(self.__test.getNumberOfQuestions()):
            question = self.__test.getQuestion(i)

            column = 0
            Label(self.__testView, text=question.getText(), wraplength=300) \
                .grid(sticky="WN", row=row, column=column)
            answerFrame = Frame(self.__testView)

            if isinstance(question, SingleAnswerQuestion):
                self.__answers.append([IntVar()])
                self.__answers[-1][0].set(-1)
            else:
                self.__answers.append([IntVar() for _ in range(question.getNumberOfAnswers())])

            column = 1
            for j in range(question.getNumberOfAnswers()):
                answer = question.getAnswer(j)
                button = None
                if isinstance(question, SingleAnswerQuestion):
                    button = Radiobutton(answerFrame, text=answer, value=j, variable=self.__answers[i][0])
                else:
                    button = Checkbutton(answerFrame, text=answer, onvalue=1, offvalue=0, variable=self.__answers[i][j])

                button.bind("<Button-1>", save)
                button.grid(sticky="W", row=j)

            answerFrame.grid(row=row, column=column)
            self.__testView.grid_rowconfigure(row+1, minsize=30)
            row += 2

        Button(self.__testView, text="Consegna").grid(row=row)

    def getAnswers(self):
        return self.__answers
