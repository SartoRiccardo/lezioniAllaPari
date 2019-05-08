from datetime import datetime
from markdown import markdown
from bs4 import BeautifulSoup
from os import remove
import objects.user
import objects.lesson


def getTest(test):
    pass


def saveTest(test, content):
    pass


def getLesson(lesson):
    """
    Accede e ritorna il contenuto della lezione passata in input
    :param lesson: Un oggetto Lezione
    :return: str, il contenuto della lezione
    """
    LESSONS_DIR = "file/lessons/"

    directory = LESSONS_DIR + lesson.getID() + ".md"

    lesson_content = ""
    file = open(directory, "r", encoding="utf-8")
    for line in file:
        line = line.replace("\n", "")
        bs = BeautifulSoup(line, features="html.parser")
        line = str(bs.encode("ascii"))[2:-1]
        lesson_content += line + "\n"

    lesson_content = markdown(lesson_content)

    file.close()
    return lesson_content


def saveLesson(lesson, content):
    """
    Salva una lezione
    :param lesson: Lesson, la lezione da salvare
    :param content: il contenuto della lezione
    :return: None
    """
    LESSONS_DIR = "file/lessons/"
    INDEX_DIR = "file/index.csv"
    INDEX_BACKUP_DIR = INDEX_DIR.replace("index.csv", "index_backup.csv")

    out = open(LESSONS_DIR + lesson.getID() + ".md", "w")
    out.write(content)
    out.close()

    newline = "{};L;{};{};{};{};{}\n".format(
                lesson.getID(),
                lesson.getTitle(),
                lesson.getStart(),
                lesson.getEnd(),
                lesson.getOwner(),
                ";".join(lesson.getClass())
            )

    index = open(INDEX_DIR)
    index_backup = open(INDEX_BACKUP_DIR, "w")
    for ln in index:
        index_backup.write(ln)
    index.close()
    index_backup.close()

    index = open(INDEX_DIR, "w")
    index_backup = open(INDEX_BACKUP_DIR)
    found = False
    for ln in index_backup:
        if ln.split(";")[0] == newline.split(";")[0]:
            index.write(newline)
            found = True
        else:
            index.write(ln)

    if not found:
        index.write(newline)

    index.close()
    index_backup.close()

    remove(INDEX_BACKUP_DIR)


def getLastID():
    """
    Trova il più grande ID inserito (l'ultimo)
    :return: int
    """
    INDEX = "file/index.csv"
    last_ID = 0

    file = open(INDEX, "r")

    file.readline()  # Rimuove prima riga

    for line in file:
        line = line.split(";")
        if int(line[0]) > last_ID:
            last_ID = int(line[0])

    file.close()
    return last_ID


def getElementsVisibleTo(user):
    """
    Legge "index.csv", trova Lezione/Test visibile a user
    :param user: Un oggetto User
    :return: Lezione/Test visibile a User
    """
    def checkOwn(item, position):
        """
        Corrispondenza proprietario lezione/test
        :param item: Array
        :param position: Posizione elemento
        :return: Boolean
        """
        nonlocal user
        if user.getState() == "A" or item[position] == user.getUsername():
            return True
        return False

    def checkDate(item, position):
        """
        Corrispondenza data lezione/test
        :param item: Array
        :param position: Posizione elemento
        :return: Boolean
        """
        nonlocal user
        if int(item[position]) <= datetime.timestamp(datetime.now()):
            return True
        else:
            return False

    def checkClass(item, position):
        """
        Corrispondenza classe lezione/test
        :param item: Array
        :param position: Inizio posizione elementi
        :return: Boolean
        """
        nonlocal user
        for classroom in item[position:]:
            for userClass in user.getClass():
                if classroom == userClass:
                    return True
        return False

    INDEX = "file/index.csv"

    array = []
    file = open(INDEX, "r")

    file.readline()  # Rimuove prima riga

    for line in file:
        line = line.replace("\n", "").split(";")

        if line[6] == "all":  # Tutte le classi
            right = True
        elif line[6] == "none":  # Nessuna classe
            continue
        else:
            right = checkOwn(line, 5)  # Proprietario
            if not right:
                right = checkClass(line, 6)  # Visibile a classe
                if right:
                    right = checkDate(line, 3)  # Data superiore a corrente

        if not right:
            continue

        element = None
        if line[1] == "L":  # Lezione
            element = objects.lesson.Lesson(line[0], line[2], line[3],
                                            line[4], line[5], line[6:])  # Crea oggetto Lezione
        elif line[1] == "T":  # Test
            pass

        array.append(element)

    file.close()
    return array


def login(user: str, password: str):
    """
    Guarda se le credenziali sono corrette
    :param user: l'username dell'utente
    :param password: la password dell'utente
    :return: un oggetto User, None se i dati inseriti non sono validi
    """
    CREDENTIALS = "config/login.csv"

    file = open(CREDENTIALS, "r")
    file.readline()
    for line in file:
        line = line.replace("\n", "").split(";")
        if str(line[3]).lower() == str(user) and str(line[4]) == str(password):

            loggedUser = objects.user.User(line[1], line[2], line[3], line[0], line[5:])

            file.close()
            return loggedUser

    file.close()
    return None
