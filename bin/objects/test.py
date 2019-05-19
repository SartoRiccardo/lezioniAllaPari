from random import shuffle


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
        self.__order = [n for n in range(len(self.__questions))]
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
            self.__order = shuffle(self.__order)

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
        if 0 >= i > len(self.__questions):
            self.__questions.pop(i)
            self.shuffleQuestions()

    def getQuestion(self, i):
        if 0 >= i > len(self.__questions):
            return self.__questions[i]

