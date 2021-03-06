from objects.element import Element
from objects.result import Result
import control.io_manager
import random
import time


class TestLink(Element):
    def __init__(self, id, title, start, end, owner, *classrooms):
        """
        Una classe che rappresenta il link che appare nella selezione delle lezioni.
        :param title: Il nome del test
        """
        super(TestLink, self).__init__(id, title, start, end, owner)

        for c in classrooms:
            self.addClass(c)


class Test:
    def __init__(self, id, name, duration, maxAttempts, shuffle=True, questions=None):
        """
        Una classe che rappresenta un test o una verifica
        :param name: Il nome del test
        :param shuffle: Un flag che determina se l'ordine delle domande è randomizzato
        :param questions:
        """
        self.__id = id
        self.__name = name
        self.__duration = duration
        self.__shuffle = shuffle
        self.__maxAttempts = maxAttempts
        if questions is None:
            self.__questions = []
        else:
            self.__questions = questions
        self.__order = []
        self.shuffleQuestions()

        self.__results = control.io_manager.getTestResults(self.__id)

    def evaluate(self):
        """
        Ritorna i punti presi
        :return: il punteggio (int)
        """
        ret = 0.0
        for q in self.__questions:
            ret += q.getScore()
        return ret

    def getMaxScore(self):
        """
        Ritorna il massimo punteggio ottenibile
        :return: il punteggio (int)
        """
        ret = 0
        for q in self.__questions:
            ret += q.getValue()
        return ret

    def shuffleQuestions(self):
        self.__order = [i for i in range(len(self.__questions))]
        if self.__shuffle:
            random.shuffle(self.__order)

    def attemptsBy(self, user):
        ret = []
        for r in self.__results:
            if r.getUsername() == user.getUsername():
                ret.append(r)

        return ret

    def registerAttempt(self, user):
        newResult = control.io_manager.registerAttempt(self, user)
        self.__results.append(newResult)

    def loadAttempt(self, result):
        pass

    def isBeingAttemptedBy(self, user):
        now = int(time.time())
        for attempt in self.attemptsBy(user):
            if now - attempt.getDate() < self.__duration:
                return attempt
        return None

    def selectAnswer(self, questionI, answerI):
        if 0 <= questionI < len(self.__questions):
            self.__questions[questionI].selectAnswer(answerI)

    def updateCurrentAttempt(self, user):
        attempt = self.isBeingAttemptedBy(user)

    # Get & Set
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getDuration(self):
        return self.__duration

    def setDuration(self, duration):
        self.__duration = duration

    def addQuestion(self, q):
        self.__questions.append(q)
        self.shuffleQuestions()

    def isShuffled(self):
        return self.__shuffle

    def setShuffle(self, shuffle):
        self.__shuffle = shuffle
        self.shuffleQuestions()

    def removeQuestion(self, q):
        if q in self.__questions:
            self.__questions.remove(q)
            self.shuffleQuestions()

    def popQuestion(self, i):
        if 0 <= i < len(self.__questions):
            self.__questions.pop(i)
            self.shuffleQuestions()

    def getQuestion(self, i, ignoreShuffle = False):
        if 0 <= i < len(self.__questions):
            index = i if ignoreShuffle else self.__order.index(i)
            return self.__questions[index]

    def getNumberOfQuestions(self):
        return len(self.__questions)

    def getMaxAttempts(self):
        return self.__maxAttempts

    def setMaxAttempts(self, maxAttempts):
        self.__maxAttempts = maxAttempts

    def getResult(self, i):
        if 0 <= i < len(self.__results):
            return self.__results[i]

    def lengthResults(self):
        return len(self.__results)

    def __str__(self):
        ret = self.__name + "\n"
        for i in self.__order:
            ret += str(self.__questions[i]) + "\n"
        return ret[:-1]


if __name__ == '__main__':
    from question import SingleAnswerQuestion, MultipleAnswerQuestion
    from score import Score

    answers = ["8", "16", "256", "1"]
    q0 = MultipleAnswerQuestion("Quali numeri sono >10?", False, Score(scorePerCorrect=1.0, scorePerIncorrect=-1.0),
                               answers, [1, 2])
    q0.selectAnswer(1)
    q0.selectAnswer(2)

    answers = ["10", "11", "12", "13"]
    q1 = SingleAnswerQuestion("Quanto vale 5+5?", False, Score(scorePerCorrect=1.0, scorePerIncorrect=-1.0), answers, 0)
    q1.selectAnswer(0)

    t = Test("Numeri")
    print(t, "\n")

    t.addQuestion(q0)
    print(t, "\n")

    t.addQuestion(q1)
    print(t, "\n")

    print(t.getQuestion(1), "\n")
