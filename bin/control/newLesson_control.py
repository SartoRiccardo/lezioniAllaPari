from datetime import datetime
from view.newLesson_view import NewLessonView
from control.io_manager import saveLesson
from objects.lesson import Lesson
from datetime import datetime


class NewLessonControl:

    __MESI = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, root, user):
        self.__newLesson = NewLessonView(root, user, self)

        # Inizio
        self.__yearStart = int(datetime.now().year)
        self.__monthStart = int(datetime.now().month)
        self.__dayStart = int(datetime.now().day)

        self.__newLesson.getMonthStart().current(self.__monthStart - 1)  # Mese corrente come prima scelta
        self.setViewDayStart()  # Setta giorni
        self.__newLesson.getDayStart().current(self.__dayStart - 1)  # Giorno corrente come prima scelta

        # Fine
        self.__yearEnd = int(datetime.now().year)
        self.__monthEnd = int(datetime.now().month)
        self.__dayEnd = int(datetime.now().day)

        self.__newLesson.getMonthEnd().current(self.__monthEnd - 1)  # Mese corrente come prima scelta
        self.setViewDayEnd()  # Setta giorni
        self.__newLesson.getDayEnd().current(self.__dayEnd - 1)  # Giorno corrente come prima scelta

        self.__newLesson.focus()

    def setDayStart(self, e):
        self.__dayStart = int(self.__newLesson.getDayStart().get())

    def setMonthStart(self, e):
        self.__monthStart = int(self.__newLesson.getMonthStart().current()+1)
        self.setViewDayStart()

    def setYearStart(self, e):
        self.__yearStart = int(self.__newLesson.getYearsStart().get())
        self.setViewDayStart()

    def setDayEnd(self, e):
        self.__dayEnd = int(self.__newLesson.getDayEnd().get())

    def setMonthEnd(self, e):
        self.__monthEnd = int(self.__newLesson.getMonthEnd().current()+1)
        self.setViewDayEnd()

    def setYearEnd(self, e):
        self.__yearEnd = int(self.__newLesson.getYearsEnd().get())
        self.setViewDayEnd()

    def setViewDayStart(self):
        """
        Setta giorni per mese/anno
        """
        day = self.__getDays(self.__monthStart, self.__yearStart)
        self.__newLesson.getDayStart().config(value=day)
        self.__newLesson.getDayStart().current(0)  # Evita un bug

    def setViewDayEnd(self):
        """
        Setta giorni per mese/anno
        :return:
        """
        day = self.__getDays(self.__monthEnd, self.__yearEnd)
        self.__newLesson.getDayEnd().config(value=day)
        self.__newLesson.getDayEnd().current(0)  # Evita un bug

    def __isBisestile(self, year):
        if year % 400 == 0 and year % 100 == 0:
            return True
        if year % 4 == 0:
            return True
        else:
            return False

    def __getDays(self, month, year):
        days = []
        n = self.__MESI[month-1]
        if month == 2 and self.__isBisestile(year):
            n += 1

        for i in range(n):
            days.append(i+1)
        return days

    def addNewLesson(self):
        pass
        # start =
        #
        #
        # lezione = Lesson(None, self.__newLesson.getTitle(), )
        # lezione.addClass(self.__newLesson.getClassList())
        #
        # saveLesson()
