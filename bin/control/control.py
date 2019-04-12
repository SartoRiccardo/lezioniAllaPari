from tkinter import Tk, sys
from control.login_control import LoginControl
from view.view import View
from control.newLesson_control import NewLessonControl
from control.io_manager import *


class Control:
    def __init__(self):
        self.__root = Tk()
        self.__root.grab_set()  # Blocca root
        self.__root.withdraw()  # Nascondi finestra fino al login
        # self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Controllo su chiusura della finestra

        self.__login = LoginControl(self.__root)
        self.__user = self.__login.getLoggedUser()

        self.__view = View(self.__root, self)  # GUI

        self.__visibleElements = getElementsVisibleTo(self.__user)  # Carica lezioni/test

        self.__view.setUser(self.__user, self.__visibleElements)  # Setta User e lezioni

        self.__list = self.__view.getList()  # Oggetto Lista
        self.__list.getList().bind("<Double-Button-1>", self.__openElement)

        self.__root.mainloop()

    def __openElement(self, e=None):
        content = getLesson(self.__list.getSelectedElement())
        for ln in content.split("\n"):
            print(ln)

    def newLesson(self, e=None):
        NewLessonControl(self.__root)

    def close(self, e=None):
        sys.exit(0)
