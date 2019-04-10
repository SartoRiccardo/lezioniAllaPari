from tkinter import Tk, sys
# from os import listdir
from control.login_control import LoginControl
from view.view import View
from objects.lesson import Lesson


class Control:
    __INDEX = "file/index.csv"
    __LESSONS_DIR = "file/lessons/"
    __TEST_DIR = "file/test/"

    def __init__(self):
        self.__root = Tk()
        self.__root.grab_set()  # Blocca root
        self.__root.withdraw()  # Nascondi finestra fino al login
        # self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Controllo su chiusura della finestra

        self.__login = LoginControl(self.__root)
        self.__user = self.__login.getLoggedUser()

        self.__view = View(self.__root)  # GUI

        self.__lessons = self.__getElements()  # Carica lezioni
        # self.__lessons = self.__getElements(Control.__LESSONS_DIR)  # Carica lezioni
        # self.__lessons = self.__getElements(Control.__TEST_DIR)  # Carica test

        self.__view.setUser(self.__user, self.__lessons)  # Setta User e lezioni

        self.__root.mainloop()

    def close(self):
        sys.exit(0)

    def __getElements(self):
        list = []
        file = open(Control.__INDEX, "r")

        file.readline()  # Rimuove prima riga

        for line in file:
            line = line.replace("\n","").split(";")

            if line[6] == "all":  # Tutte le classi
                right = True
            elif line[6] == "none":  # Nessuna classe
                continue
            else:
                right = self.__checkOwn(line, 5)  # Proprietario
                # if not right:
                #     right = self.__checkDate(line)  # Data superiore a corrente
                if not right:
                    right = self.__checkClass(line, 6)  # Visibile a classe

            if not right:
                continue

            element = None
            if line[1] == "L":  # Lezione
                element = Lesson(line[2], line[3], line[4], line[5])  # Crea oggetto Lezione
                for classroom in line[6:]:
                    element.addClass(classroom)

            elif line[1] == "T":  # Test
                pass

            list.append(element)
        return list

    # def __getElements(self, dir):
    #     """
    #     Controlla la lista (lezioni o test), divide l'estensione, divide per '_' ed esegue i controlli
    #     :param dir: Directory
    #     :return: Lista dei file di proprieta o che può visualizzare
    #     """
    #     elements = listdir(dir)
    #     list = []
    #
    #     for item in elements:
    #         item = item.split(".")
    #         item[0] = item[0].split("_")
    #
            # if item[0][4] == "all":  # Tutte le classi
            #     right = True
            # elif item[0][4] == "none":  # Nessuna classe
            #     continue
            # else:
            #     right = self.__checkOwn(item)  # Proprietario
            #     if not right:
            #         right = self.__checkClass(item)  # Visibile a classe
            #
            # if not right:
            #     continue
            #
            # lesson = Lesson(item[0][0], item[0][1], item[0][2], item[0][3])  # Crea oggetto Lezione
            # for classroom in item[0][4:]:
            #     lesson.addClass(classroom)
            #
            # list.append(lesson)
    #     return list

    def __checkOwn(self, item, position):
        if item[position] == self.__user.getUsername():
            return True
        return False

    def __checkDate(self, item):
        pass

    def __checkClass(self, item, position):
        for classroom in item[position:]:
            for userClass in self.__user.getClass():
                if classroom == userClass:
                    return True
        return False
