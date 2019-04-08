from tkinter import Tk, sys
from os import listdir
from login_view import LoginView
from view import View
from user import User
from lesson import Lesson


class Control:
    __LESSONS_DIR = "lessons/"
    __TEST_DIR = "test/"
    __CREDENTIALS = "config/login.csv"

    def __init__(self):

        self.__root = Tk()
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Controllo su chiusura della finestra
        self.__root.grab_set()  # Blocca root (non funziona, ma lo lascio)
        self.__root.withdraw()  # Nascondi finestra fino al login

        self.__view = View(self.__root)  # GUI

        self.__user = User()  # Oggetto Utente

        self.__login = LoginView(self.__root, self.__user, self)  # Apri login e carica dati User

        self.__lessons = self.__getElements(Control.__LESSONS_DIR)  # Carica lezioni
        #self.__lessons = self.__getElements(Control.__TEST_DIR)  # Carica test

        self.__view.setUser(self.__user, self.__lessons)  # Setta User e lezioni

        self.__root.mainloop()

    def close(self):
        sys.exit(0)

    def __getElements(self, dir):
        """
        Controlla la lista (lezioni o test), divide l'estensione, divide per '_' ed esegue i controlli
        :param dir: Directory
        :return: Lista dei file di proprieta o che può visualizzare
        """
        elements = listdir(dir)
        list = []

        for item in elements:
            item = item.split(".")
            item[0] = item[0].split("_")

            if item[0][4] == "all":  # Tutte le classi
                right = True
            elif item[0][4] == "none":  # Nessuna classe
                continue
            else:
                right = self.__checkOwn(item)  # Proprietario
                if not right:
                    right = self.__checkClass(item)  # Visibile a classe

            if not right:
                continue

            lesson = Lesson(item[0][0], item[0][1], item[0][2], item[0][3])  # Crea oggetto Lezione
            for classroom in item[0][4:]:
                lesson.addClass(classroom)

            list.append(lesson)
        return list

    def login(self, user: str, password: str):
        """
        Guarda se le credenziali sono corrette
        :param user: l'username dell'utente
        :param password: la password dell'utente
        :return: un oggetto User, None se i dati inseriti non sono validi
        """
        if user == "" or password == "":
            return None
        else:
            file = open(Control.__CREDENTIALS, "r")
            file.readline()
            for line in file:
                line = line.replace("\n", "").split(";")
                if str(line[3]).lower() == str(user) and str(line[4]) == str(password):
                    ret = User(line[1], line[2], line[3], line[0])
                    for classroom in line[5:]:
                        ret.addClass(classroom)
                    return ret

    def __checkClass(self, item):
        for classroom in item[0][4:]:
            for userClass in self.__user.getClass():
                if classroom == userClass:
                    return True
        return False

    def __checkOwn(self, item):
        if item[0][3] == self.__user.getUsername():
            return True
        return False
