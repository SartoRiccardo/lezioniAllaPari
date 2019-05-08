from datetime import datetime
from view.newLesson_view import NewLessonView
from control.io_manager import saveLesson, getLastID
from objects.lesson import Lesson
from tkinter import messagebox


class NewLessonControl:

    def __init__(self, root, user):
        self.__user = user
        self.__newLesson = NewLessonView(root, user, self)
        self.__newLesson.focus()
        self.__newLesson.mainloop()

    def updateAccents(self, text):
        """
        Sostituisce le lettere accentate con i caratteri speciali dell'html
        :param text:
        :return:
        """
        accenti = {

        }

    def addNewLesson(self):
        newId = getLastID() + 1
        title = self.__newLesson.getTitle()
        startDate = int(datetime.timestamp(datetime.strptime(str(self.__newLesson.getDateStart()), "%Y-%m-%d")))
        endDate = int(datetime.timestamp(datetime.strptime(str(self.__newLesson.getDateEnd()), "%Y-%m-%d")))
        classes = self.__newLesson.getClassList()
        text = self.__newLesson.getLessonContent()
        proprietario = self.__user.getUsername()

        if title != "" and classes != "" and text != "":
            lessonObject = Lesson(str(newId), title, startDate, endDate, proprietario)
            for c in classes:
                lessonObject.addClass(c)
            saveLesson(lessonObject, text)
            self.__newLesson.quit()
        else:
            self.__newLesson.warning("Campi incompleti", "Verificare di aver completato tutti i campi necessari.")

