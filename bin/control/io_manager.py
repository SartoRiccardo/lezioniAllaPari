from datetime import datetime
import objects.user
import objects.lesson
from os import listdir


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

            loggedUser = objects.user.User(line[1], line[2], line[3], line[0])

            for classroom in line[5:]:
                loggedUser.addClass(classroom)
            return loggedUser


def getTest(test):
    pass


def saveTest(test):
    pass


def getLesson(lesson):
    """
    Accede e ritorna il contenuto della lezione passata in input
    :param lesson: Un oggetto Lezione
    :return: str, il contenuto della lezione
    """
    LESSONS_DIR = "file/lessons/"

    directory = LESSONS_DIR + lesson.getID() + ".txt"

    file = open(directory, "r")
    return file.read()


def saveLesson(lesson):
    pass


def getElementsVisibleTo(user):
    """
    Legge "index.csv", trova Lezione/Test visibile a user
    :param user: Un oggetto User
    :return: Lezione/Test visibile a User
    """
    def checkOwn(item, position):
        nonlocal user
        if item[position] == user.getUsername():
            return True
        return False

    def checkDate(item, position):
        nonlocal user
        if int(item[position]) <= datetime.timestamp(datetime.now()):
            return True
        else:
            return False

    def checkClass(item, position):
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
            element = objects.lesson.Lesson(line[0], line[2], line[3], line[4], line[5])  # Crea oggetto Lezione
            for classroom in line[6:]:
                element.addClass(classroom)
        elif line[1] == "T":  # Test
            pass

        array.append(element)
    return array
