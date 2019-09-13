from view.test_view import TestView
from control.io_manager import getTest, saveTestResults, getCurrentAttemptBy, updateAttempt
import objects.result
import objects.question


class TestControl:
    def __init__(self, root, testId, user):
        self.__test = getTest(testId)
        self.__user = user
        self.__prevAnswers = []

        if len(self.__test.attemptsBy(self.__user)) < self.__test.getMaxAttempts() or \
                self.__test.isBeingAttemptedBy(self.__user):
            if not self.__test.isBeingAttemptedBy(self.__user):
                self.__test.registerAttempt(self.__user)
                saveTestResults(self.__test)
            self.__tv = TestView(root, self.__test, self)
        else:
            print("Hai già provato!")

    def saveResults(self, answers):
        if len(self.__prevAnswers) > 0:
            for i in range(len(answers)):
                for j in range(len(answers[i])):
                    if answers[i][j] != self.__prevAnswers[i][j]:
                        if isinstance(self.__test.getQuestion(i), objects.question.SingleAnswerQuestion):
                            self.__test.selectAnswer(i, answers[i][j])
                        else:
                            self.__test.selectAnswer(i, j)

        self.__prevAnswers = answers
        attempt = getCurrentAttemptBy(self.__user, self.__test)
        for i in range(self.__test.getNumberOfQuestions()):
            q = self.__test.getQuestion(i, True)
            attempt.setAnswer(i, q.getSelectedAnswers())
        updateAttempt(self.__test, attempt)
