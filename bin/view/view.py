from tkinter import *
from objects.list import List


class View:
    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__root.title("Lezioni alla Pari")
        self.__root.geometry("800x500")
        self.__root.minsize(800, 500)
        # self.__root.resizable(width="False", height="False")

        self.__frame = Frame(self.__root)
        self.__frame.pack()

        self.__user = None
        self.__list = None

    def setUser(self, user, lessons):
        self.__user = user

        Label(self.__frame, text="Nome: " + self.__user.getName()).pack()
        Label(self.__frame, text="Cognome: " + self.__user.getSurname()).pack()
        Label(self.__frame, text="Username: " + self.__user.getUsername()).pack()

        Label(self.__frame, text="\nClasse:").pack()
        for classroom in self.__user.getClass():
            Label(self.__frame, text=classroom).pack()

        self.__list = List(self.__frame, lessons)  # Carica lista elementi

        if user.getState() == "T":
            addItemButton = Button(self.__frame, text="New Lesson", width=10, height=1)
            addItemButton.bind("<Button-1>", self.__control.addToList)
            addItemButton.pack()
