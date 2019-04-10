from tkinter import *
from tkinter import ttk as box
from datetime import datetime

class NewLessonView:
    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__newLesson = Toplevel(self.__root)
        self.__newLesson.title("Nuova lezione")
        self.__newLesson.geometry("500x350")
        self.__newLesson.resizable(False, False)

        Label(self.__newLesson, text="NUOVA LEZIONE\n").grid(row=0, column=0, columnspan=4)

        Label(self.__newLesson, text="Titolo").grid(row=1, column=0, columnspan=1)
        self.__title = Entry(self.__newLesson, justify="center")
        self.__title.focus()
        self.__title.grid(row=1, column=1, columnspan=1)

        # DATA INIZIO
        Label(self.__newLesson, text="DATA DI INIZIO").grid(row=2, column=0, columnspan=2)

        self.__annoLabelStart = Label(self.__newLesson, text="Anno")
        self.__annoLabelStart.grid(row=3, column=0, columnspan=1)
        self.__annoStart = box.Combobox(self.__newLesson, values=self.__getYears())
        self.__annoStart.bind("<<ComboboxSelected>>", self.__control.yearStartInserted)
        self.__annoStart.grid(row=3, column=1, columnspan=1)

        self.__meseLabelStart = Label(self.__newLesson, text="Mese")
        self.__meseLabelStart.grid(row=4, column=0, columnspan=1)
        self.__meseStart = box.Combobox(self.__newLesson, values=["NA"])
        self.__meseStart.current(0)
        self.__meseStart.bind("<<ComboboxSelected>>", self.__control.MonthStartInserted)
        self.__meseStart.grid(row=4, column=1, columnspan=1)

        self.__giornoLabelStart = Label(self.__newLesson, text="Giorno")
        self.__giornoLabelStart.grid(row=5, column=0, columnspan=1)
        self.__giornoStart = box.Combobox(self.__newLesson, values=["NA"])
        self.__giornoStart.current(0)
        self.__giornoStart.bind("<<ComboboxSelected>>", self.__control.DayStartInserted)
        self.__giornoStart.grid(row=5, column=1, columnspan=1)

        # DATA FINE
        Label(self.__newLesson, text="DATA DI FINE").grid(row=2, column=2, columnspan=2)

        self.__annoLabelEnd = Label(self.__newLesson, text="Anno")
        self.__annoLabelEnd.grid(row=3, column=2, columnspan=1)
        self.__annoEnd = box.Combobox(self.__newLesson, values=self.__getYears())
        self.__annoEnd.bind("<<ComboboxSelected>>", self.__control.yearEndInserted)
        self.__annoEnd.grid(row=3, column=3, columnspan=1)

        self.__meseLabelEnd = Label(self.__newLesson, text="Mese")
        self.__meseLabelEnd.grid(row=4, column=2, columnspan=1)
        self.__meseEnd = box.Combobox(self.__newLesson, values=["NA"])
        self.__meseEnd.current(0)
        self.__meseEnd.bind("<<ComboboxSelected>>", self.__control.MonthEndInserted)
        self.__meseEnd.grid(row=4, column=3, columnspan=1)

        self.__giornoLabelEnd = Label(self.__newLesson, text="Giorno")
        self.__giornoLabelEnd.grid(row=5, column=2, columnspan=1)
        self.__giornoEnd = box.Combobox(self.__newLesson, values=["NA"])
        self.__giornoEnd.current(0)
        self.__giornoEnd.bind("<<ComboboxSelected>>", self.__control.DayEndInserted)
        self.__giornoEnd.grid(row=5, column=3, columnspan=1)

    def __getDays(self, n):
        days = []
        for i in range(n):
            days.append(i+1)
        return days

    def __getMonths(self, bisestile=False):
        months = [
            ("Gennaio", 31),
            ("Febbraio", 29 if bisestile else 28),
            ("Marzo", 31),
            ("Aprile", 30),
            ("Maggio", 31),
            ("Giugno", 30),
            ("Luglio", 31),
            ("Agosto", 31),
            ("Settembre", 30),
            ("Ottobre", 31),
            ("Novembre", 30),
            ("Dicembre", 31)
        ]
        return months

    def addMonthView(self, box):
        mesi = []
        for m in self.__getMonths():
            mesi.append(m[0])
        box.config(value=mesi)

    def addDayView(self, n, box):
        box.config(value=self.__getDays(n))

    def __getYears(self):
        years = []
        thisYear = int(datetime.now().year)
        for i in range(5):
            years.append(i+thisYear)
        return years

    def getMeseStart(self):
        return self.__meseStart

    def getMeseEnd(self):
        return self.__meseEnd

