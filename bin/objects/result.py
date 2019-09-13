

class Result:
    def __init__(self, id, username, date):
        self.__id = id
        self.__username = username
        self.__date = date
        self.__answers = []

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getDate(self):
        return self.__date

    def setDate(self, date):
        self.__date = date

    def getAnswer(self, i):
        if 0 <= i < len(self.__answers):
            return self.__answers[i]

    def setAnswer(self, i, answer):
        if 0 <= i < len(self.__answers):
            self.__answers[i] = answer

    def addAnswer(self, answer, i=None):
        if i is None or i > len(self.__answers) or 0 > i:
            i = len(self.__answers)
        self.__answers.insert(i, answer)

    def length(self):
        return len(self.__answers)

    def __str__(self):
        return '{' + f"\"id\": {self.__id}, \"username\": \"{self.__username}\", " \
                     f"\"date\": {self.__date}, \"answers\": {self.__answers}" + '}'

    def __eq__(self, other):
        return self.__id == other.getId()
