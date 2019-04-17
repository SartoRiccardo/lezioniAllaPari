from copy import deepcopy


class User:
    def __init__(self, name="", surname="", username="", state="S", *classrooms):
        self.__name = name
        self.__surname = surname
        self.__username = username
        self.__state = state

        if len(classrooms) == 1 and isinstance(classrooms[0], list):
            self.__class = deepcopy(classrooms[0])
        else:
            self.__class = list(classrooms)

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getUsername(self):
        return self.__username

    def getState(self):
        return self.__state

    def getClass(self):
        return self.__class

    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname

    def setUsername(self, username):
        self.__username = username

    def setState(self, state):
        self.__state = state

    def addClass(self, classroom):
        self.__class.append(classroom)

    def isStudent(self):
        if self.__state == "S":
            return True
        else:
            return False

    def __str__(self):
        return "User nome={} cognome={} username={}".format(self.__name, self.__surname, self.__username)
