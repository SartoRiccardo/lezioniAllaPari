from tkinter import Tk, sys
from os import *
from login import Login
from view import View
from user import User
from lesson import Lesson

class Control():
    def __init__(self):
        self.__lessonsDir = "lessons/"
        self.__testDir = "test/"

        self.__root = Tk()
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Controllo su chiusura della finestra
        self.__root.grab_set()  # Blocca root (non funziona, ma lo lascio)
        self.__root.withdraw()  # Nascondi finestra fino al login

        self.__view = View(self.__root)  # GUI

        self.__user = User()  # Oggetto Utente

        self.__login = Login(self.__root, self.__user)  # Apri login e carica dati User

        self.__lessons = self.__getElements(self.__lessonsDir)  # Carica lezioni
        #self.__lessons = self.__getElements(self.__lessonsDir)  # Carica test

        self.__view.setUser(self.__user, self.__lessons)  # Setta User e lezioni

        self.__root.mainloop()

    def close(self):
        sys.exit(0)

    def __getElements(self, dir):
        '''
        Controlla la lista (lezioni o test), divide l'estensione, divide per '_' ed esegue i controlli
        :param dir: Directory
        :return: Lista dei file di proprieta o che può visualizzare
        '''
        elements = listdir(dir)
        list = []

        for item in elements:
            item = item.split(".")
            item[0] = item[0].split("_")

            if(item[0][4] == "all"):  # Tutte le classi
                right = True
            elif(item[0][4] == "none"):  # Nessuna classe
                continue
            else:
                right = self.__checkOwn(item)  # Proprietario
                if not(right):
                    right = self.__checkClass(item)  # Visibile a classe

            if not(right):
                continue

            lesson = Lesson(item[0][0],item[0][1],item[0][2],item[0][3])  # Crea oggetto Lezione
            for classroom in item[0][4:]:
                lesson.addClass(classroom)

            list.append(lesson)
        return list

    def __checkClass(self, item):
        for classroom in item[0][4:]:
            for userClass in self.__user.getClass():
                if (classroom == userClass):
                    return True
        return False

    def __checkOwn(self, item):
        if (item[0][3] == self.__user.getUsername()):
            return True
        return False