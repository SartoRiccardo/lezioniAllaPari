from objects.user import User
from view.login_view import LoginView
from exceptions import EmptyFieldException


class LoginControl:
    __CREDENTIALS = "config/login.csv"

    def __init__(self, root):

        self.__view = LoginView(root, self)
        self.__loggedUser = None

        self.__view.mainloop()

    def login(self, user: str, password: str):
        """
        Guarda se le credenziali sono corrette
        :param user: l'username dell'utente
        :param password: la password dell'utente
        :return: un oggetto User, None se i dati inseriti non sono validi
        """
        if user == "":
            raise EmptyFieldException("Username should not be an empty string")
        if password == "":
            raise EmptyFieldException("Password should not be an empty string")

        file = open(LoginControl.__CREDENTIALS, "r")
        file.readline()
        for line in file:
            line = line.replace("\n", "").split(";")
            if str(line[3]).lower() == str(user) and str(line[4]) == str(password):

                loggedUser = User(line[1], line[2], line[3], line[0])

                for classroom in line[5:]:
                    loggedUser.addClass(classroom)
                return loggedUser

    def logInAs(self, user: User):
        """
        Effettua la procedura di login
        :param user: l'utente loggato
        """
        if not isinstance(user, User):
            raise TypeError("Expected user, got {} instead".format(type(user).__name__))
        self.__loggedUser = user
        self.__view.quit()

    def getLoggedUser(self):
        return self.__loggedUser

    def setLoggedUser(self, user: User):
        if not isinstance(user, User):
            raise TypeError("Expected User, got {} instead".format(type(user).__name__))
        self.__loggedUser = user
