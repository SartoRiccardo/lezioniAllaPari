from tkinter import Tk, sys
from control.login_control import LoginControl
from view.view import View
from control.io_manager import getLesson, getElementsVisibleTo
from view.lesson_view import LessonView
from control.newLesson_control import NewLessonControl


class Control:
    def __init__(self):
        self.__root = Tk()
        # self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Controllo su chiusura della finestra

        self.__view = View(self.__root, self)  # GUI root

        self.__login = LoginControl(self.__root)  # Login
        self.__user = self.__login.getLoggedUser()

        self.__visibleElements = getElementsVisibleTo(self.__user)  # Carica lezioni/test da visualizzare

        self.__view.setUser(self.__user, self.__visibleElements)  # Setta User e lezioni

        self.__list = self.__view.getList()  # Oggetto Lista
        self.__list.getList().bind("<Double-Button-1>", self.__openElement)

        self.__root.mainloop()

    def __openElement(self, e=None):
        lessonTitle = self.__list.getSelectedElement().getTitle()
        lessonContent = getLesson(self.__list.getSelectedElement())  # Lezione
        LessonView(self.__root, lessonTitle, lessonContent)

    def newLesson(self, e=None):
        NewLessonControl(self.__root)

    def close(self, e=None):
        sys.exit(0)
