from datetime import datetime
from view.newLesson_view import NewLessonView
from control.io_manager import saveLesson, getLastID, setLastID
from objects.lesson import Lesson


class NewLessonControl:
    def __init__(self, control, root, username, classes):
        self.__control = control
        self.__root = root
        self.__username = username

        self.__newLesson = NewLessonView(root, classes, self)
        self.__newLesson.mainloop()

    def addNewLesson(self):
        newId = getLastID() + 1
        title = self.__newLesson.getTitle()
        startDate = int(datetime.timestamp(datetime.strptime(self.__newLesson.getDateStart(), "%Y-%m-%d %H:%M")))
        endDate = int(datetime.timestamp(datetime.strptime(self.__newLesson.getDateEnd(), "%Y-%m-%d %H:%M")))
        classes = self.__newLesson.getClassList()
        text = self.__newLesson.getLessonContent()
        owner = self.__username

        if title != "":
            lesson = Lesson(str(newId), title, startDate, endDate, owner)

            if len(classes) > 0:
                for c in classes:
                    lesson.addClass(c)
            else:
                lesson.addClass("None")

            saveLesson(lesson, text)
            setLastID(newId)  # Salva nuovo Ultimo ID
            self.__control.refresh()  # Ricaricare Listbox
            self.__newLesson.quit()
        else:
            self.__newLesson.warning("Errore", "Inserire un Titolo")
