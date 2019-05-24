from tkinter import Tk, sys
from control.login_control import LoginControl
from view.view import View
from control.io_manager import getLesson, getElementsVisibleTo
from control.newLesson_control import NewLessonControl
from objects.lesson import Lesson
from control.test_control import TestControl
from objects.test import TestLink


class Control:
    def __init__(self):
        #self.__root = Tk()
        self.__loginA()
        # self.__root.withdraw()  # Nascondi finestra fino al login
        #
        # self.__view = View(self.__root, self)  # GUI root
        #
        # self.__login = LoginControl(self.__root)  # Login
        # self.__user = self.__login.getLoggedUser()
        #
        # self.__view.setView(self.__user)  # Setta User e lezioni
        # self.__list = self.__view.getList()  # Oggetto Lista
        #
        # self.refresh()
        #
        # self.__root.mainloop()

    def __loginA(self):
        self.__root = Tk()
        self.__root.withdraw()  # Nascondi finestra fino al login

        self.__view = View(self.__root, self)  # GUI root

        self.__login = LoginControl(self.__root)  # Login
        self.__user = self.__login.getLoggedUser()

        self.__view.setView(self.__user)  # Setta User e lezioni
        self.__list = self.__view.getList()  # Oggetto Lista

        self.refresh()

        self.__root.mainloop()

    def openElement(self, e=None):
        currentElement = self.__list.getSelectedElement()
        if isinstance(currentElement, Lesson):
            lesson_content = getLesson(self.__list.getSelectedElement())
            self.__view.setHTML(lesson_content)
        else:
            pass

    def newLesson(self, e=None):
        NewLessonControl(self, self.__root, self.__user.getUsername(), self.__user.getClass())

    def refresh(self, e=None):
        self.__visibleElements = getElementsVisibleTo(self.__user)  # Carica lezioni/test da visualizzare
        self.__view.setList(self.__visibleElements)

    def logout(self, e=None):
        self.__root.destroy()
        self.__loginA()

    def close(self, e=None):
        sys.exit(0)
