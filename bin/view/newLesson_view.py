from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry


class NewLessonView:
    def __init__(self, root: Tk, classes, control):
        self.__root = root
        self.__control = control
        self.__classes = classes

        self.__newLesson = Toplevel(self.__root)
        self.__newLesson.title("Nuova lezione")
        self.__newLesson.geometry("1150x500")
        self.__newLesson.minsize(width=1000, height=500)
        # self.__newLesson.resizable(False, False)
        self.__newLesson.grab_set()

        self.__fInfo = Frame(self.__newLesson)  # Frame Info

        self.__fTitle = Frame(self.__fInfo)  # Frame Titolo
        Label(self.__fTitle, text="\nNuova Lezione\n").pack(side=TOP, anchor=N)

        # Titolo
        Label(self.__fTitle, text="Titolo").pack(side=LEFT, anchor=N)
        self.__title = Entry(self.__fTitle, justify="center")
        self.__title.focus()
        self.__title.pack(side=LEFT, anchor=N)

        self.__fTitle.pack(side=TOP, anchor=N, padx=10, pady=20)  # Fine Frame Titolo

        # Data
        self.__fData = Frame(self.__fInfo)  # Frame Data

        # Data Inizio
        self.__fDataStart = Frame(self.__fData)  # Frame Data Start
        Label(self.__fDataStart, text="Data d'Inizio").pack(side=TOP, anchor=N)

        self.__calcStart = DateEntry(self.__fDataStart, width=20,
                                     firstweekday="monday", showweeknumbers=False, showothermonthdays=False,
                                     locale="it_it",
                                     selectmode="None", background='darkblue', foreground='white', borderwidth=2,
                                     state="readonly")
        self.__calcStart.pack(side=TOP, anchor=N)
        self.__fDataStart.pack(side=LEFT, anchor=N, padx=20)  # Fine Frame Data Start

        # Data Fine
        self.__fDataEnd = Frame(self.__fData)  # Frame Data End
        Label(self.__fDataEnd, text="Data di Fine").pack(side=TOP, anchor=N)

        self.__calcEnd = DateEntry(self.__fDataEnd, width=20,
                                   firstweekday="monday", showweeknumbers=False, showothermonthdays=False,
                                   locale="it_it",
                                   selectmode="None", background='darkblue', foreground='white', borderwidth=2,
                                   state="readonly")
        self.__calcEnd.pack(side=TOP, anchor=N)
        self.__fDataEnd.pack(side=LEFT, anchor=N, padx=20)  # Fine Frame Data End

        self.__fData.pack(side=TOP, anchor=N, padx=10, pady=20)  # Fine Frame Data

        # Classi
        self.__fClass = Frame(self.__fInfo, relief=FLAT)  # Frame Class

        self.__classSel = []  # variabili di stato dei checkbox (1 se selezionato, altrimenti 0)
        Label(self.__fClass, text="Classi").pack(side=TOP, anchor=N)

        n = len(self.__classes)
        frames = []
        for i in range(int(n / 5) + (1 if n % 5 != 0 else 0)):
            frame = Frame(self.__fClass)
            frames.append(frame)
            frames[i].pack(side=TOP, anchor=NW, padx=2, pady=2)

        j, k = 0, 0
        for i in range(n):
            self.__classSel.append(IntVar())
            checkbtn = Checkbutton(frames[j], text=self.__classes[i], variable=self.__classSel[i])
            checkbtn.pack(side=LEFT, anchor=N, padx=10)
            if k < 4:
                k += 1
            else:
                j += 1
                k = 0

        self.__fClass.pack(side=TOP, anchor=N, padx=10, pady=20)  # Fine Frame Class

        # TextArea
        self.__fText = Frame(self.__newLesson)  # Frame TextArea

        self.__scroll = Scrollbar(self.__fText)
        self.__scroll.pack(side=RIGHT, anchor=SE, fill=Y)

        self.__inputText = Text(self.__fText, width=75, yscrollcommand=self.__scroll.set)
        self.__inputText.pack(side=LEFT, anchor=N, fill=BOTH, expand=True)
        self.__scroll.config(command=self.__inputText.yview)

        # Button
        self.__fButton = Frame(self.__fInfo)  # Frame Button

        # Button Save
        self.__create = Button(self.__fButton, text="Crea", width=10, height=1, command=self.__control.addNewLesson)
        self.__create.pack(side=LEFT, padx=10, pady=20)

        # Button Cancel
        self.__create = Button(self.__fButton, text="Annulla", width=10, height=1, command=self.quit)
        self.__create.pack(side=LEFT, padx=10, pady=20)

        self.__fButton.pack(side=BOTTOM)  # Fine Frame Button

        self.__fInfo.pack(side=LEFT, anchor=N, fill=Y, padx=10, pady=20)  # Fine Frame Info
        self.__fText.pack(side=LEFT, anchor=N, fill=BOTH, expand=True, padx=10, pady=10)  # Fine Frame Text

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
        for c in range(len(self.__classSel)):
            if self.__classSel[c].get() == 1:
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
