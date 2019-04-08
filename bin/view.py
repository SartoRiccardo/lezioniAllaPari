from tkinter import *
from list import List


class View:
    def __init__(self, root):
        self.__root = root

        self.__root.title("Lezioni alla Pari")
        self.__root.geometry("800x500")
        self.__root.minsize(800, 500)
        # self.__root.resizable(width="False", height="False")

        self.__frame = Frame(self.__root)
        self.__frame.pack()

        self.__user = None
        self.__list = None

    def setUser(self, user, lessons):

        Label(self.__frame, text="Nome: " + user.getName()).pack()
        Label(self.__frame, text="Cognome: " + user.getSurname()).pack()
        Label(self.__frame, text="Username: " + user.getUsername()).pack()

        Label(self.__frame, text="\nClasse:").pack()
        for classroom in user.getClass():
            Label(self.__frame, text=classroom).pack()

        self.__list = List(self.__frame, lessons)  # Carica lista elementi
