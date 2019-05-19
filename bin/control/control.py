from tkinter import Tk, sys
from control.login_control import LoginControl
from view.view import View
from control.io_manager import getLesson, getElementsVisibleTo
from control.newLesson_control import NewLessonControl


class Control:
    def __init__(self):
        self.__root = Tk()

        self.__view = View(self.__root, self)  # GUI root

        self.__login = LoginControl(self.__root)  # Login
        self.__user = self.__login.getLoggedUser()

        self.__view.setView(self.__user)  # Setta User e lezioni
        self.__list = self.__view.getList()  # Oggetto Lista

        self.refresh()

        self.__root.mainloop()

    def openElement(self, e=None):
        lesson_content = getLesson(self.__list.getSelectedElement())

        self.__view.setHTML(lesson_content)

    def newLesson(self, e=None):
        NewLessonControl(self, self.__root, self.__user.getUsername(), self.__user.getClass())

    def refresh(self, e=None):
        self.__visibleElements = getElementsVisibleTo(self.__user)  # Carica lezioni/test da visualizzare
        self.__view.setList(self.__visibleElements)

    def close(self, e=None):
        sys.exit(0)
