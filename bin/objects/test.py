import random


class Test:
    def __init__(self, name, shuffle=True, questions=None):
        """
        Una classe che raprresenta un test o una verifica
        :param name: Il nome del test
        :param shuffle: Un flag che determina se l'ordine delle domande è randomizzato
        :param questions:
        """
        self.__name = name
        self.__shuffle = shuffle
        if questions is None:
            self.__questions = []
        else:
            self.__questions = questions
        self.__order = None
        self.shuffleQuestions()

    def evaluate(self):
        """
        Ritorna i punti presi
        :return: il punteggio (int)
        """
        ret = 0
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
        if self.__shuffle:
            self.__order = [i for i in range(len(self.__questions))]
            random.shuffle(self.__order)

    # Get & Set
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def addQuestion(self, q):
        self.__questions.append(q)
        self.shuffleQuestions()

    def removeQuestion(self, q):
        if q in self.__questions:
            self.__questions.remove(q)
            self.shuffleQuestions()

    def popQuestion(self, i):
        if 0 <= i < len(self.__questions):
            self.__questions.pop(i)
            self.shuffleQuestions()

    def getQuestion(self, i):
        if 0 <= i < len(self.__questions):
            return self.__questions[i]

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
