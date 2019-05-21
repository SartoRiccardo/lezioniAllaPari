from abc import abstractmethod, ABC
import random
import copy


class Question(ABC):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers):
        self._text = text
        self._shuffle = shuffle
        self._pointEvaluator = pointEvaluator

        self._answers = answers
        self._shuffledAnswers = copy.copy(self._answers)
        if self._shuffle:
            random.shuffle(self._shuffledAnswers)

    @abstractmethod
    def getScore(self):
        """
        Ritorna il punteggio ottenuto nella domanda
        :return: il punteggio: float
        """
        pass

    @abstractmethod
    def selectAnswer(self, i):
        """
        Seleziona una risposta
        :param i: l'indice della risposta nelle risposte mescolate
        """
        pass


class SingleAnswerQuestion(Question):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers, correct):
        Question.__init__(self, text, shuffle, pointEvaluator, answers)
        self.__correct = correct
        self.__selectedAnswer = -1

    def getScore(self):
        if self.__selectedAnswer == -1:
            return self._pointEvaluator.unanswered()
        elif self.__selectedAnswer == self.__correct:
            return self._pointEvaluator.neutralScore() + self._pointEvaluator.scorePerCorrect()
        else:
            return self._pointEvaluator.neutralScore() - self._pointEvaluator.scorePerIncorrect()

    def selectAnswer(self, i):
        self.__selectedAnswer = self._answers.index(self._shuffledAnswers[i])

    def __str__(self):
        ret = self._text + "\n"
        shuffledIndex = self._shuffledAnswers.index(self._answers[self.__selectedAnswer]) \
                            if self.__selectedAnswer >= 0 else -1
        for i in range(len(self._shuffledAnswers)):

            if i == shuffledIndex:
                ret += f">>> {self._shuffledAnswers[i]}\n"
            else:
                ret += f">   {self._shuffledAnswers[i]}\n"
        return ret[:-1]


class MultipleAnswerQuestion(Question):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers, correct):
        Question.__init__(self, text, shuffle, pointEvaluator, answers)
        self.__correct = correct
        self.__selectedAnswers = []

    def getScore(self):
        if len(self.__selectedAnswers) == 0 and len(self.__correct) > 0:
            return self._pointEvaluator.unanswered()
        else:
            score = self._pointEvaluator.neutralScore()
            for answer in self.__selectedAnswers:
                if answer in self.__correct:
                    score += self._pointEvaluator.scorePerCorrect()
                else:
                    score -= self._pointEvaluator.scorePerIncorrect()
            return score

    def selectAnswer(self, i):
        correctIndex = self._answers.index(self._shuffledAnswers[i])
        if correctIndex in self.__selectedAnswers:
            self.__selectedAnswers.remove(correctIndex)
        else:
            self.__selectedAnswers.append(correctIndex)

    def __str__(self):
        ret = self._text + "\n"
        shuffledIndexes = [self._shuffledAnswers.index(self._answers[i]) for i in self.__selectedAnswers]
        for i in range(len(self._shuffledAnswers)):
            if i in shuffledIndexes:
                ret += f"+ {self._shuffledAnswers[i]}\n"
            else:
                ret += f"- {self._shuffledAnswers[i]}\n"
        return ret[:-1]
