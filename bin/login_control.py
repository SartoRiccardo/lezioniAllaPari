from user import User
from login_view import LoginView
from tkinter import *


class LoginControl:
    __CREDENTIALS = "config/login.csv"

    def __init__(self):
        root = Tk()
        root.grab_set()  # Blocca root
        root.withdraw()  # Nascondi finestra fino al login

        LoginView(root, self)

    def login(self, user: str, password: str):
        """
        Guarda se le credenziali sono corrette
        :param user: l'username dell'utente
        :param password: la password dell'utente
        :return: un oggetto User, None se i dati inseriti non sono validi
        """
        if user == "" or password == "":
            return None
        else:
            file = open(LoginControl.__CREDENTIALS, "r")
            file.readline()
            for line in file:
                line = line.replace("\n", "").split(";")
                if str(line[3]).lower() == str(user) and str(line[4]) == str(password):
                    ret = User(line[1], line[2], line[3], line[0])
                    for classroom in line[5:]:
                        ret.addClass(classroom)
                    return ret
