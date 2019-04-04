from tkinter import *

class View():
    def __init__(self, root, user):
        self.__root = root

        self.__frame = Frame(self.__root)
        self.__frame.pack()

        Label(self.__frame, text="Nome: " + user.getName()).pack()
        Label(self.__frame, text="Cognome: " + user.getSurname()).pack()
        Label(self.__frame, text="Username: " + user.getUsername()).pack()

        Label(self.__frame, text="\nClasse:").pack()
        for classe in user.getClassed():
            Label(self.__frame, text=classe).pack()