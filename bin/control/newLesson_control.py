from datetime import datetime
from view.newLesson_view import NewLessonView
from control.io_manager import saveLesson, getLastID


class NewLessonControl:

    __MESI = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, root, user):
        self.__newLesson = NewLessonView(root, user, self)

        self.__newLesson.focus()

    def addNewLesson(self):
        # Data to Timestamp ↓
        # int(datetime.timestamp(datetime.strptime(str(self.__newLesson.getDateStart()), "%Y-%m-%d")))

        print("Nuova lezione: " + self.__newLesson.getTitle())

        print("Date: " + str(self.__newLesson.getDateStart()), end=" | ")
        print(self.__newLesson.getDateEnd())

        print("Classi: " + str(self.__newLesson.getClassList()))
        print("Testo: " + self.__newLesson.getLessonContent())
