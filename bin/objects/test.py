from objects.element import Element
import random


class Test(Element):
    def __init__(self, title, start, end, owner, shuffle=True, questions=[]):
        """
        Una classe che raprresenta un test o una verifica
        :param title: Il nome del test
        :param shuffle: Un flag che determina se l'ordine delle domande deve essere random
        :param questions:
        """
        super(Test, self).__init__(id, title, start, end, owner)

        self.__shuffle = shuffle
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
        ret = super().getTitle() + "\n"
        for i in self.__order:
            ret += str(self.__questions[i]) + "\n"
        return ret[:-1]
        # return "{} - Scadenza: {}".format(super().getTitle(), super().getEnd())


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

    t = Test("Numeri", 0, 0, "s")
    print(t, "\n")

    t.addQuestion(q0)
    print(t, "\n")

    t.addQuestion(q1)
    print(t, "\n")

    print(t.getQuestion(1), "\n")
