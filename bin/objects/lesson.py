class Lesson:
    def __init__(self, title, start, end, owner, *classrooms):
        self.__title = title
        self.__start = start
        self.__end = end
        self.__owner = owner

        self.__class = []
        for classroom in classrooms:
            self.__class.append(classroom)

    def getClass(self):
        return self.__class

    def getTitle(self):
        return self.__title

    def getEnd(self):
        return self.__end

    def getStart(self):
        return self.__start

    def getOwner(self):
        return self.__owner

    def addClass(self, classroom):
        self.__class.append(classroom)

    def setTitle(self, title):
        self.__title = title

    def setStart(self, start):
        self.__start = start

    def setEnd(self, end):
        self.__end = end

    def setOwner(self, owner):
        self.__owner = owner

    def __str__(self):
        return "{} - Scadenza: {}".format(self.__title, self.__end)
