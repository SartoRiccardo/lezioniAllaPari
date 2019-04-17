from datetime import datetime
from copy import deepcopy


class Lesson:
    def __init__(self, id, title, start, end, owner, *classrooms):
        self.__id = id
        self.__title = title
        self.__start = start
        self.__end = end
        self.__owner = owner

        if len(classrooms) == 1 and isinstance(classrooms[0], list):
            self.__class = deepcopy(classrooms[0])
        else:
            self.__class = list(classrooms)

    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getClass(self):
        return self.__class

    def getStart(self):
        return datetime.fromtimestamp(int(self.__start))

    def getEnd(self):
        return datetime.fromtimestamp(int(self.__end))

    def getOwner(self):
        return self.__owner

    def setID(self, id):
        self.__id = id

    def setTitle(self, title):
        self.__title = title

    def addClass(self, classroom):
        self.__class.append(classroom)

    def setStart(self, start):
        self.__start = start

    def setEnd(self, end):
        self.__end = end

    def setOwner(self, owner):
        self.__owner = owner

    def __str__(self):
        return "{} - Scadenza: {}".format(self.__title, self.getEnd())
