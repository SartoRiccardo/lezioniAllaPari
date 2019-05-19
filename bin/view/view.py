from tkinter import *
from tk_html_widgets import HTMLLabel
from objects.list import List


class View:
    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__root.title("Lezioni alla Pari")
        self.__root.grab_set()  # Blocca root
        self.__root.withdraw()  # Nascondi finestra fino al login
        self.__root.geometry("1000x600")
        self.__root.minsize(800, 500)
        # self.__root.resizable(width="False", height="False")

        self.__frameInfo = Frame(self.__root)
        self.__frameInfo.pack(side=TOP, fill=X, padx=5, pady=10)

        self.__frameLesson = Frame(self.__root)
        self.__frameLesson.pack(side=BOTTOM, fill=BOTH, padx=5, pady=10, expand=True)

        self.__user = None
        self.__list = None
        self.__html = HTMLLabel(self.__frameLesson, html="<p>Doppio-Click su una lezione per aprirla</p>")

    def setView(self, user):
        """
        Setta utente e crea grafica
        :param user: User
        :param lessons: Lezioni visibile a User
        """
        self.__user = user

        text = "Ciao "+self.__user.getName()+" "+self.__user.getSurname()+"!"
        Label(self.__frameInfo, text=text, font=("Helvetica", 18)).pack(side=LEFT, anchor=NW)

        # classes = "Classi: " if len(self.__user.getClass()) > 1 else "Classe: "
        # for classroom in self.__user.getClass():
        #     classes += classroom
        #     if classroom != self.__user.getClass()[-1]:  # Non la prima del ciclo, allora ','
        #          classes += ", "
        # Label(self.__frame, text=classes).pack()

        self.__list = List(self.__frameLesson)
        self.__list.getObjectList().bind("<Double-Button-1>", self.__control.openElement)

        self.__html.pack(side=RIGHT, anchor=W, fill=BOTH, expand=True)

        if user.getState() != "S":
            Button(self.__frameInfo, text="Nuova Lezione", width=10, height=1, command=self.__control.newLesson).pack(
                anchor=NE, side=RIGHT)

    def setList(self, lessons):
        self.__list.setList(lessons)  # Carica lista elementi

    def getList(self):
        return self.__list

    def setHTML(self, content):
        self.__html.set_html(content, strip=True)
