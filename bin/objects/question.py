from abc import abstractmethod, ABC
import random


class Question(ABC):
    def __init__(self, text):
        self._text = text

    @abstractmethod
    def getScore(self):
        """
        Ritorna il punteggio ottenuto nella domanda
        :return: il punteggio: float
        """
        pass


class ClosedQuestion(Question):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers):
        Question.__init__(self, text)
        self._shuffle = shuffle
        self._pointEvaluator = pointEvaluator

        self._answers = answers
        if self._shuffle:
            self._shuffledAnswers = random.shuffle(self._answers)
        else:
            self._shuffledAnswers = self._answers

    @abstractmethod
    def getScore(self):
        pass

    @abstractmethod
    def selectAnswer(self, i):
        """
        Seleziona una risposta
        :param i: l'indice della risposta nelle risposte mescolate
        """
        pass


class SingleAnswerQuestion(ClosedQuestion):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers, correct):
        ClosedQuestion.__init__(self, text, shuffle, pointEvaluator, answers)
        self.__correct = correct
        self.__selectedAnswer = None

    def getScore(self):
        if self.__selectedAnswer is None:
            return self._pointEvaluator.unanswered()
        elif self.__selectedAnswer == self.__correct:
            return self._pointEvaluator.neutralScore() + self._pointEvaluator.scorePerCorrect()
        else:
            return self._pointEvaluator.neutralScore() - self._pointEvaluator.scorePerIncorrect()

    def selectAnswer(self, i):
        correctIndex = self._answers.index(self._shuffledAnswers[i])
        self.__selectedAnswer = self._answers[correctIndex]


class MultipleAnswerQuestion(ClosedQuestion):
    def __init__(self, text, shuffle: bool, pointEvaluator, answers, correct):
        ClosedQuestion.__init__(self, text, shuffle, pointEvaluator, answers)
        self.__correct = correct
        self.__selectedAnswers = []

    def getScore(self):
        if len(self.__selectedAnswers) == 0 and len(self.__correct) > 0:
            return self._pointEvaluator.unanswered()
        else:
            score = self._pointEvaluator.neutralScore()
            for answer in self.__selectedAnswers:
                if answer in self.__selectedAnswers:
                    score += self._pointEvaluator.scorePerCorrect()
                else:
                    score += self._pointEvaluator.scorePerIncorrect()
            return score

    def selectAnswer(self, i):
        correctIndex = self._answers.index(self._shuffledAnswers[i])
        if correctIndex in self.__selectedAnswers:
            self.__selectedAnswers.remove(correctIndex)
        else:
            self.__selectedAnswers.append(correctIndex)


class OpenQuestion:
    pass
