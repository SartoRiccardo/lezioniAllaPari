from tkinter import *
from tkinter import ttk as box
from datetime import datetime


class NewLessonView:
    __MESI = [
        "Gennaio",
        "Febbraio",
        "Marzo",
        "Aprile",
        "Maggio",
        "Giugno",
        "Luglio",
        "Agosto",
        "Settembre",
        "Ottobre",
        "Novembre",
        "Dicembre"
    ]

    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__newLesson = Toplevel(self.__root)
        self.__newLesson.title("Nuova lezione")
        self.__newLesson.geometry("500x350")
        self.__newLesson.minsize(width=500,height=350)
        self.__newLesson.resizable(False, False)

        Label(self.__newLesson, text="\nNUOVA LEZIONE\n").grid(row=0, column=0, columnspan=4)

        Label(self.__newLesson, text="Titolo").grid(row=1, column=0, columnspan=1)
        self.__title = Entry(self.__newLesson, justify="center")
        self.__title.focus()
        self.__title.grid(row=1, column=1, columnspan=1)

        # Data Inizio
        Label(self.__newLesson, text="DATA DI INIZIO").grid(row=2, column=0, columnspan=2)

        # Anno
        Label(self.__newLesson, text="Anno").grid(row=3, column=0, columnspan=1)

        self.__yearStart = box.Combobox(self.__newLesson, values=self.__getYears())
        self.__yearStart.current(0)
        self.__yearStart.bind("<<ComboboxSelected>>", self.__control.setYearStart)
        self.__yearStart.grid(row=3, column=1, columnspan=1)

        # Mese
        Label(self.__newLesson, text="Mese").grid(row=4, column=0, columnspan=1)

        self.__monthStart = box.Combobox(self.__newLesson, values=self.__MESI)
        self.__monthStart.bind("<<ComboboxSelected>>", self.__control.setMonthStart)
        self.__monthStart.grid(row=4, column=1, columnspan=1)

        # Giorno
        Label(self.__newLesson, text="Giorno").grid(row=5, column=0, columnspan=1)

        self.__dayStart = box.Combobox(self.__newLesson, values=[1])
        self.__dayStart.current(0)
        self.__dayStart.bind("<<ComboboxSelected>>", self.__control.setDayStart)
        self.__dayStart.grid(row=5, column=1, columnspan=1)

        # Data Fine
        Label(self.__newLesson, text="DATA DI FINE").grid(row=2, column=2, columnspan=2)

        # Anno
        Label(self.__newLesson, text="Anno").grid(row=3, column=2, columnspan=1)

        self.__yearEnd = box.Combobox(self.__newLesson, values=self.__getYears())
        self.__yearEnd.current(0)
        self.__yearEnd.bind("<<ComboboxSelected>>", self.__control.setYearEnd)
        self.__yearEnd.grid(row=3, column=3, columnspan=1)

        # Mese
        Label(self.__newLesson, text="Mese").grid(row=4, column=2, columnspan=1)

        self.__monthEnd = box.Combobox(self.__newLesson, values=self.__MESI)
        self.__monthEnd.current(0)
        self.__monthEnd.bind("<<ComboboxSelected>>", self.__control.setMonthEnd)
        self.__monthEnd.grid(row=4, column=3, columnspan=1)

        # Giorno
        Label(self.__newLesson, text="Giorno").grid(row=5, column=2, columnspan=1)

        self.__dayEnd = box.Combobox(self.__newLesson, values=[1])
        self.__dayEnd.current(0)
        self.__dayEnd.bind("<<ComboboxSelected>>", self.__control.setDayEnd)
        self.__dayEnd.grid(row=5, column=3, columnspan=1)

        self.__create = Button(self.__newLesson, text="Crea", width=10, height=1)  # Nuova lezione

    def getDayStart(self):
        return self.__dayStart

    def getDayEnd(self):
        return self.__dayEnd

    def getMonthStart(self):
        return self.__monthStart

    def getMonthEnd(self):
        return self.__monthEnd

    def getYearsStart(self):
        return self.__yearStart

    def getYearsEnd(self):
        return self.__yearEnd

    def __getYears(self, n=5):
        years = []
        year = int(datetime.now().year)
        for i in range(n):
            years.append(i+year)
        return years