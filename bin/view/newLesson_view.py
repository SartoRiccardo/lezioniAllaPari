from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox


class NewLessonView:
    def __init__(self, root: Tk, classes, control):
        self.__root = root
        self.__control = control
        self.__classes = classes

        self.__newLesson = Toplevel(self.__root)
        self.__newLesson.title("Nuova lezione")
        self.__newLesson.geometry("1150x500")
        # self.__newLesson.minsize(width=500, height=350)
        self.__newLesson.resizable(False, False)
        self.__newLesson.grab_set()

        Label(self.__newLesson, text="\nNuova Lezione\n").grid(row=0, column=0, columnspan=4)

        Label(self.__newLesson, text="Titolo").grid(row=1, column=1, columnspan=1)
        self.__title = Entry(self.__newLesson, justify="center")
        self.__title.focus()
        self.__title.grid(row=1, column=2, columnspan=1)

        # Data Inizio
        Label(self.__newLesson, text="Data d'Inizio").grid(row=2, column=0, columnspan=2)

        self.__calcStart = DateEntry(self.__newLesson, width=20,
                        firstweekday="monday", showweeknumbers=False, showothermonthdays=False, locale="it_it",
                        selectmode="None", background='darkblue', foreground='white', borderwidth=2,
                        state="readonly")
        self.__calcStart.grid(row=3, column=1, columnspan=1)

        # Data Fine
        Label(self.__newLesson, text="Data di Fine").grid(row=2, column=2, columnspan=2)

        self.__calcEnd = DateEntry(self.__newLesson, width=20,
                         firstweekday="monday", showweeknumbers=False, showothermonthdays=False, locale="it_it",
                         selectmode="None", background='darkblue', foreground='white', borderwidth=2,
                         state="readonly")
        self.__calcEnd.grid(row=3, column=3, columnspan=1)

        # Classi
        self.__classiSel = []       # variabili di stato dei checkbox (1 se selezionato, altrimenti 0)
        Label(self.__newLesson, text="Classi").grid(row=6, column=0, columnspan=4)

        for lesson in self.__classes:
            index = self.__classes.index(lesson)
            self.__classiSel.append(IntVar())
            row = int(index / 5)
            column = index % 5
            Checkbutton(self.__newLesson, text=lesson, variable=self.__classiSel[index]).grid(row=7 + row,
                                                                                              column=column)

        # TextArea
        self.__scroll = Scrollbar(self.__newLesson)
        self.__scroll.grid(row=1, column=7, rowspan=10, sticky=N+S)

        self.__inputText = Text(self.__newLesson, width=75, yscrollcommand=self.__scroll.set)
        self.__inputText.grid(row=1, column=6, rowspan=10)
        self.__scroll.config(command=self.__inputText.yview)

        # Button Save
        self.__create = Button(self.__newLesson, text="Crea", width=10, height=1,
                               command=self.__control.addNewLesson)
        self.__create.grid(row=7 + len(self.__classiSel), column=0, columnspan=4)

        # Button Cancel
        self.__create = Button(self.__newLesson, text="Annulla", width=10, height=1, command=self.quit)
        self.__create.grid(row=7 + len(self.__classiSel), column=2, columnspan=4)

    def getTitle(self):
        return self.__title.get()

    def getDateStart(self):
        return self.__calcStart.get_date()

    def getDateEnd(self):
        return self.__calcEnd.get_date()

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
        classList = self.__classes
        r = []
        for c in range(len(self.__classiSel)):
            if self.__classiSel[c].get() == 1:
                r.append(classList[c])
        return r

    def mainloop(self):
        self.__newLesson.mainloop()

    def quit(self):
        self.__newLesson.grab_release()
        self.__newLesson.quit()
        self.__newLesson.destroy()

    def warning(self, title, message):
        messagebox.showwarning(title, message)
