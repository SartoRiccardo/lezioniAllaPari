from view.newLesson_view import NewLessonView


class NewLessonControl:

    __MESI = {
            "Gennaio": 31,
            "Febbraio": 28,
            "Marzo": 31,
            "Aprile": 30,
            "Maggio": 31,
            "Giugno": 30,
            "Luglio": 31,
            "Agosto": 31,
            "Settembre": 30,
            "Ottobre": 31,
            "Novembre": 30,
            "Dicembre": 31
    }

    def __init__(self, root):
        self.__newLesson = NewLessonView(root, self)

    def yearStartInserted(self, e):
        self.__newLesson.addMonthView(self.__newLesson.getMeseStart())

    def MonthStartInserted(self, e):
        giorni = self.__MESI[self.__newLesson.getMeseStart().get()]
        self.__newLesson.addDayView(giorni, self.__newLesson.getMeseStart())

    def DayStartInserted(self, e):
        pass

    # ----------------------------------------------------

    def yearEndInserted(self, e):
        self.__newLesson.addMonthView(self.__newLesson.getMeseEnd())

    def MonthEndInserted(self, e):
        giorni = self.__MESI[self.__newLesson.getMeseEnd().get()]
        self.__newLesson.addDayView(giorni, self.__newLesson.getMeseEnd())

    def DayEndInserted(self, e):
        pass

