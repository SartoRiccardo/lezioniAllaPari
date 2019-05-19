class Score:
    """Una classe per tenere valori"""

    def __init__(self, unanswered=0.0, neutralScore=0.0, scorePerCorrect=0.0, scorePerIncorrect=0.0):
        """
        :param unanswered: punteggio se non si risponde alla domanda
        :param minScore: punteggio minimo in caso si rispoda alla domanda
        :param scorePerCorrect: aumento di punteggio per ogni risposta corretta
        :param scorePerIncorrect: diminuzione di punteggio per ogni risposta incorretta
        """
        self.__unanswered = unanswered
        self.__neutralScore = neutralScore
        self.__scorePerCorrect = scorePerCorrect
        self.__scorePerIncorrect = scorePerIncorrect if scorePerIncorrect >= 0 else scorePerIncorrect*-1

    def unanswered(self):
        return self.__unanswered

    def neutralScore(self):
        return self.__neutralScore

    def scorePerCorrect(self):
        return self.__scorePerCorrect

    def scorePerIncorrect(self):
        return self.__scorePerIncorrect
