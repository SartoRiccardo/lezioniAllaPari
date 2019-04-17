from tkinter import *
from tkinter import ttk as box
from datetime import datetime
from control.io_manager import saveLesson


class NewLessonView:
    __MESI = [
        "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
        "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
    ]

    def __init__(self, root: Tk, user, control):
        self.__root = root
        self.__control = control
        self.__user = user

        self.__newLesson = Toplevel(self.__root)
        self.__newLesson.title("Nuova lezione")
        self.__newLesson.geometry("1150x500")
        # self.__newLesson.minsize(width=500, height=350)
        self.__newLesson.resizable(False, False)

        Label(self.__newLesson, text="\nNUOVA LEZIONE\n").grid(row=0, column=0, columnspan=4)

        Label(self.__newLesson, text="Titolo").grid(row=1, column=1, columnspan=1)
        self.__title = Entry(self.__newLesson, justify="center")
        self.__title.focus()
        self.__title.grid(row=1, column=2, columnspan=1)

        # Data Inizio
        Label(self.__newLesson, text="DATA DI INIZIO").grid(row=2, column=0, columnspan=2)

        # Anno
        Label(self.__newLesson, text="Anno").grid(row=3, column=0, columnspan=1)

        self.__yearStart = box.Combobox(self.__newLesson, values=self.__getYears(), state="readonly")
        self.__yearStart.current(0)
        self.__yearStart.bind("<<ComboboxSelected>>", self.__control.setYearStart)
        self.__yearStart.grid(row=3, column=1, columnspan=1)

        # Mese
        Label(self.__newLesson, text="Mese").grid(row=4, column=0, columnspan=1)

        self.__monthStart = box.Combobox(self.__newLesson, values=self.__MESI, state="readonly")
        self.__monthStart.bind("<<ComboboxSelected>>", self.__control.setMonthStart)
        self.__monthStart.grid(row=4, column=1, columnspan=1)

        # Giorno
        Label(self.__newLesson, text="Giorno").grid(row=5, column=0, columnspan=1)

        self.__dayStart = box.Combobox(self.__newLesson, values=[1], state="readonly")
        self.__dayStart.current(0)
        self.__dayStart.bind("<<ComboboxSelected>>", self.__control.setDayStart)
        self.__dayStart.grid(row=5, column=1, columnspan=1)

        # Data Fine
        Label(self.__newLesson, text="DATA DI FINE").grid(row=2, column=2, columnspan=2)

        # Anno
        Label(self.__newLesson, text="Anno").grid(row=3, column=2, columnspan=1)

        self.__yearEnd = box.Combobox(self.__newLesson, values=self.__getYears(), state="readonly")
        self.__yearEnd.current(0)
        self.__yearEnd.bind("<<ComboboxSelected>>", self.__control.setYearEnd)
        self.__yearEnd.grid(row=3, column=3, columnspan=1)

        # Mese
        Label(self.__newLesson, text="Mese").grid(row=4, column=2, columnspan=1)

        self.__monthEnd = box.Combobox(self.__newLesson, values=self.__MESI, state="readonly")
        self.__monthEnd.current(0)
        self.__monthEnd.bind("<<ComboboxSelected>>", self.__control.setMonthEnd)
        self.__monthEnd.grid(row=4, column=3, columnspan=1)

        # Giorno
        Label(self.__newLesson, text="Giorno").grid(row=5, column=2, columnspan=1)

        self.__dayEnd = box.Combobox(self.__newLesson, values=[1], state="readonly")
        self.__dayEnd.current(0)
        self.__dayEnd.bind("<<ComboboxSelected>>", self.__control.setDayEnd)
        self.__dayEnd.grid(row=5, column=3, columnspan=1)

        self.__classiSel = []       # variabili di stato dei checkbox (1 se selezionato, altrimenti 0)
        Label(self.__newLesson, text="Classi").grid(row=6, column=0, columnspan=4)
        for lesson in self.__user.getClass():
            index = self.__user.getClass().index(lesson)
            self.__classiSel.append(IntVar())
            riga = int(index / 5)
            colonna = index % 5
            Checkbutton(self.__newLesson, text=lesson, variable=self.__classiSel[index]).grid(row=7+riga, column=colonna)

        self.__create = Button(self.__newLesson, text="CREA", width=10, height=1, command=self.__control.addNewLesson)  # Nuova lezione
        self.__create.grid(row=7+len(self.__classiSel), column=0, columnspan=4)

        self.__scroll = Scrollbar(self.__newLesson)
        self.__scroll.grid(row=1, column=7, rowspan=10, sticky=N+S)

        self.__inputText = Text(self.__newLesson, width=75, yscrollcommand=self.__scroll.set)
        self.__inputText.grid(row=1, column=6, rowspan=10)

        self.__scroll.config(command=self.__inputText.yview)

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

    def getTitle(self):
        return self.__title.get()

    def getLessonContent(self):
        """
        Restituisce il contenuto dell'oggetto self.__inputText di tipo Text
        :return: (stringa)
        """
        return self.__inputText.get("1.0", END)

    def getClassList(self):
        """
        Restituisce un array di stringhe con le classi selezionate
        :return: r (array di stringhe)
        """
        classList = self.__user.getClass()
        r = []
        for c in range(len(self.__classiSel)):
            if self.__classiSel[c].get() == 1:
                r.append(classList[c])
        return r

    def focus(self):
        self.__newLesson.grab_set()

    def quit(self):
        pass
